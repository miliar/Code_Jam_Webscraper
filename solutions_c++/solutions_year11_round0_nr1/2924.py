#include <iostream>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

#define MAX_BUF_SIZE 4096


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
		char* toke = strtok(buf, " \n");
		int resttimeO = 0;
		int resttimeB = 0;
		int totaltime = 0;
		int prePosO = 1;
		int prePosB = 1;
		toke = strtok(NULL, " \n");
		while (toke)
		{
			if (strcmp(toke, "O") == 0)
			{
				toke = strtok(NULL, " \n");
				int pos = atoi(toke);
				int worktime = abs(pos - prePosO);
				if (worktime <= resttimeO)
				{
					totaltime += 1;
					resttimeB += 1;
				}
				else
				{
					totaltime += worktime-resttimeO+1;
					resttimeB +=  worktime-resttimeO+1;
				}
				resttimeO = 0;
				prePosO = pos;
			}
			else
			{
				toke = strtok(NULL, " \n");
				int pos = atoi(toke);
				int worktime = abs(pos - prePosB);
				if (worktime <= resttimeB)
				{
					totaltime += 1;
					resttimeO += 1;
				}
				else
				{
					totaltime += worktime-resttimeB+1;
					resttimeO +=  worktime-resttimeB+1;
				}
				resttimeB = 0;
				prePosB = pos;
			}
			toke = strtok(NULL, " \n");
		}
		fprintf(out, "Case #%d: %d\n", count, totaltime);
	}
	fclose(in);
	fclose(out);
}