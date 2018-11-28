#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

#define MWORD 15
#define MDIC 5000

int length;
int dicsize;
char dictionary[MDIC][MWORD+1];

int solve()
{
	bool tag[MDIC][MWORD]={false,}, isblock=false;
	int i, j, ilength, wlength=0, tempcnt, count=0;
	char input[512];
	scanf("%s", input);
	ilength=strlen(input);
	for(i=0; i<ilength; i++)
	{
		switch(input[i])
		{
		case '(':	isblock=true;
			break;
		case ')':	isblock=false;
			wlength++;
			break;
		default:	for(j=0; j<dicsize; j++)	if(dictionary[j][wlength]==input[i])	tag[j][wlength]=true;
			if(!isblock)	wlength++;
		}
	}
	if(wlength!=length)	return 0;
	for(i=0; i<dicsize; i++)
	{
		tempcnt=0;
		for(j=0; j<length; j++)	if(tag[i][j])	tempcnt++;
		if(tempcnt==length)	count++;
	}
	return count;
}

int main()
{
	int i, n;
	scanf("%d %d %d", &length, &dicsize, &n);
	for(i=0; i<dicsize; i++)	scanf("%s", dictionary[i]);
	for(i=0; i<n; i++)	printf("Case #%d: %d\n", i+1, solve());
	return 0;
}