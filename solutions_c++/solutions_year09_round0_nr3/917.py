#include <iostream>
#include <cstring>
using namespace std;

char s[1000];
char p[50];
int res[1000][50];
int t, tt;
int ls, lp;
FILE *ifs;
FILE *ofs;

void readdata()
{
	fgets(s, 1000, ifs);
}

void work()
{
	int i, j;
	
	ls = strlen(s);
	lp = strlen(p);
	
	for (i = 0; i <= ls; ++i)
		for (j = 0; j <= lp; ++j)
			res[i][j] = 0;
	
	for (i = 0; i <= ls; ++i)
		res[i][0] = 1;
	
	for (i = 1; i <= ls; ++i)
		for (j = 1; j <= lp; ++j)
		{
			res[i][j] = res[i - 1][j];
			if (s[i - 1] == p[j - 1]) 
				res[i][j] += res[i - 1][j - 1];
			res[i][j] %= 10000;
		}
}

void print()
{
	fprintf(ofs, "%s%d%s", "Case #", (tt + 1), ": ");
	if (res[ls][lp] < 1000) 
		fprintf(ofs, "%s", "0");
	if (res[ls][lp] < 100)
		fprintf(ofs, "%s", "0");
	if (res[ls][lp] < 10)
		fprintf(ofs, "%s", "0");
	fprintf(ofs, "%d%s", res[ls][lp], "\n");
}

int main()
{
	ifs = fopen("qr3.in", "r");
	ofs = fopen("qr3.out", "w");
	
	fscanf(ifs, "%d", &t);
	fgets(s, 1000, ifs);
	
	sprintf(p, "%s", "welcome to code jam");
	
	for (tt = 0; tt < t; ++tt)
	{
		readdata();
		work();
		print();
	}
	
	fclose(ifs);
	fclose(ofs);
}
