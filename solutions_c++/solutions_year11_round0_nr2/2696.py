#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <iostream>
using namespace std;
int i, j, c, d, n, t, e, count, start;
char combine[4], oppose[3], list[11], str[11];
void locate(char ch)
{
	int m=0;
	while (m<count&&list[m]!=ch) m++;
	if (m==count) start=-1;
	else start=m;
}
void main()////////////////////////////////////////////////only for small dataset
{
	FILE *rFile=fopen("D:\\B-small-attempt2.in", "r"); e=ferror(rFile); assert(e==0);
	FILE *wFile=fopen("D:\\B-out.txt", "w"); e=ferror(wFile); assert(e==0);
	fscanf(rFile, "%d", &t);
	for (i=0; i<t; i++)
	{
		fscanf(rFile, "%d", &c);
		if (c) fscanf(rFile, "%s", combine);
		fscanf(rFile, "%d", &d);
		if (d) fscanf(rFile, "%s", oppose);
		fscanf(rFile, "%d", &n);
		fscanf(rFile, "%s", str);
		count=0;
		for (j=0; j<n; j++)
		{
			list[count++]=str[j];
			if (count>1)
			{
				if ((c)&&((list[count-1]==combine[0]&&list[count-2]==combine[1])||(list[count-1]==combine[1]&&list[count-2]==combine[0])))
				{
					list[count-2]=combine[2];
					count--;
				}
				else if ((d)&&(list[count-1]==oppose[0]||list[count-1]==oppose[1]))
				{
					if (list[count-1]==oppose[0])
						locate(oppose[1]);
					else
						locate(oppose[0]);
					if (start>=0) count=0;
				}
			}
		}//for j=0
		for (j=0; j<count; j++) printf("%c", list[j]);
		cout << endl;
		fprintf(wFile, "Case #%d: [", i+1);
		if (count)
		{
			for (j=0; j<count-1; j++) fprintf(wFile, "%c, ", list[j]);
			fprintf(wFile, "%c", list[count-1]);
		}
		fprintf(wFile, "]\n");
	}//for i=0
	fclose(rFile); e=ferror(rFile); assert(e==0);
	fclose(wFile); e=ferror(wFile); assert(e==0);
	system("pause");
}