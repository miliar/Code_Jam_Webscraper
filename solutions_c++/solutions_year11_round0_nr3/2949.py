#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <map>
#include <set>
using namespace std;

#define MAX_BUF_SIZE 40960


int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		cout << "Usage:command.exe infile outfile" << endl;
		exit(1);
	}
	FILE* in = fopen(argv[1], "r");
	if (!in)
	{
		cout << "cannot open infile" << endl;
		exit(1);
	}
	FILE* out = fopen(argv[2], "w");
	if (!out)
	{
		cout << "cannot open outfile" << endl;
		exit(1);
	}
	char buf[MAX_BUF_SIZE];
	fgets(buf, MAX_BUF_SIZE, in);
	int count = 0;
	while (fgets(buf, MAX_BUF_SIZE, in))
	{
		count ++;
		printf("\r%d", count);
		fgets(buf, MAX_BUF_SIZE, in);
		vector<int> numVec;
		char* toke = strtok(buf, " \n");
		while (toke)
		{
			numVec.push_back(atoi(toke));
			toke = strtok(NULL, " \n");
		}
		int res = 0;
		for (int i = 0; i < numVec.size(); i++)
		{
			res ^= numVec[i];
		}
		if (res != 0)
		{
			fprintf(out, "Case #%d: NO\n", count);
			continue;
		}
		int minNum = INT_MAX;
		int sum = 0;
		int index = 0;
		for (int i = 0; i < numVec.size(); i++)
		{
			if (numVec[i] < minNum)
			{
				minNum = numVec[i];
			}
			sum += numVec[i];
		}
		fprintf(out, "Case #%d: %d\n", count, sum-minNum);
	}
	fclose(in);
	fclose(out);
}