#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

void solve(int probid)
{
	int numb, suprise, target, score[100] = {0,};
	int hit = 0;
	int abnormal = 0;
	scanf("%d %d %d", &numb, &suprise, &target);
	int value[3];
	for(int i = 0; i<numb; i++)
	{
		scanf("%d", &score[i]);
		value[0] = value[1]=value[2] = score[i]/3;
		if(score[i]%3>0)
			value[0]++;
		if(score[i]%3>1)
			value[1]++;
		if(value[0]>=target)
		{
			hit++;
			continue;
		}
		if(value[0] != 0 && value[0] == value[1] && value[0]+1 >= target)
			abnormal++;
	}
	if(abnormal>suprise)
		abnormal = suprise;
	printf("Case #%d: %d\n", probid, hit+abnormal);
}

int main()
{
	int numb = 0;
	char numbs[10] = {0,};
	gets(numbs);
	numb = atoi(numbs);
	for(int i = 0; i<numb; i++)
		solve(i+1);
	return 0;
}