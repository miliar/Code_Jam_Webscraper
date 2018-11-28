#include <stdio.h>
#include <memory.h>
#include <map>
#include <string>
#include <list>
#include <vector>
#include <functional>
#include <algorithm>
using namespace std;
#pragma warning(disable:4996)
//////////////////////////
//#define SMALL
//#ifdef SMALL
//#else
//#endif

#define MAX_SIZE 256

//////////////////////////
FILE *out;
int iCase = 1;
int N;
int n;
vector<int> x1, y1;
list<int> x, y;

//////////////////////////
int ReadFile(FILE *file)
{
	x1.clear(); y1.clear();

	int i, j;
	int num;
	char line[MAX_SIZE];	
		
	fscanf(file, "%d", &n);
	

	for(i = 1; i <= 2; ++i)
	{
		for(j = 0; j < n; ++j)
		{
			fscanf(file, "%d", &num);
			if (i == 1)
			{				
				x1.push_back(num);
			}
			else
			{
				y1.push_back(num);
			}
		}
	}
	
	sort<vector<int>::iterator>(x1.begin(), x1.end());
	sort<vector<int>::iterator>(y1.begin(), y1.end(), greater<int>());

	int v;
	v = 0;
	for(i = 0; i < n; ++i)
	{
		v += x1[i] * y1[i];
	}
	
	return v;
}


int main()
{
	char *InName = "A-small-attempt1.in";
	char *OutName = "A-small-attempt1.out";

	FILE *file = fopen(InName, "r");
	if (0 == file)
	{
		printf("File can't be opened!\n");
		exit(-1);
	}
	out = fopen(OutName, "w");


	int result;
	fscanf(file, "%d", &N);

	for(iCase = 1; iCase <= N; ++ iCase)
	{
		result = ReadFile(file);

		fprintf(out, "Case #%d: %d\n", iCase, result);
	}

	fclose(out);
	fclose(file);
	
	return 0;
}