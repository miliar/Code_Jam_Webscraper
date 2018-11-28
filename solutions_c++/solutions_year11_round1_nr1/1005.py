#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <map>
#include <set>
using namespace std;

#define MAX_BUF_SIZE 40960

long long getfactor(long long m,long long n)  
{   
	long long temp;   
	if(m>n)   
	{   
		temp=m;   
		m=n;   
		n=temp;
	}   
	while(m!=0)   
	{   
		temp=n%m;   
		n=m;   
		m=temp;   
	}   
	return  n;   
}

int  main(int argc, char* argv[])
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
	long long count = 0;
	while (fgets(buf, MAX_BUF_SIZE, in))
	{
		count ++;
		printf("\r%d", count);
		char* toke = strtok(buf, " \n");
		long long n = _atoi64(toke);
		toke = strtok(NULL, " \n");
		long long pd = _atoi64(toke);
		if (pd > 100 || pd < 0)
		{
			fprintf(out, "Case #%d: Broken\n", count);
			continue;
		}
		toke = strtok(NULL, " \n");
		long long pg = _atoi64(toke);
		if (pg > 100 || pg < 0)
		{
			fprintf(out, "Case #%d: Broken\n", count);
			continue;
		}
		if (pd == 0)
		{
			if (pg == 100)
			{
				fprintf(out, "Case #%d: Broken\n", count);
			}
			else
			{
				fprintf(out, "Case #%d: Possible\n", count);
			}
			continue;
		}
		long long f = getfactor(pd, 100);
		long long mpd = 100/f;
		long long flag = 0;
		for (long long i = 1; i <= n; i++)
		{
			if (i % mpd == 0)
			{
				flag = 1;
				break;
			}
		}
		if (flag == 0)
		{
			fprintf(out, "Case #%d: Broken\n", count);
			continue;
		}
		if (pd != 100 && pg == 100)
		{
			fprintf(out, "Case #%d: Broken\n", count);
			continue;
		}
		if (pd != 0 && pg == 0)
		{
			fprintf(out, "Case #%d: Broken\n", count);
			continue;
		}
		fprintf(out, "Case #%d: Possible\n", count);
	}
	fclose(in);
	fclose(out);
}