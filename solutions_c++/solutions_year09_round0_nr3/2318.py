#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char source[]="welcome to code jam";
char input[501];
int slength=19;
int length;
__int64 count;

void find(int loc, int index)
{
	while(loc<length)
	{
		if(input[loc]==source[index])
		{
			index++;
			if(index==slength)
			{
				count++;
			}
			else find(loc+1, index);
			index--;
		}
		loc++;
	}
}

void solve(int seq)
{
	char result[5]="0000";
	int i;
	gets(input);
	length=strlen(input);
	count=0;
	find(0, 0);
	i=3;
	while(i>=0&&count!=0)
	{
		result[i]=count%10+'0';
		count/=10;
		i--;
	}
	printf("Case #%d: %s\n", seq+1, result);
}

int main()
{
	int i, n;
	char temp[5];
	n=atoi(gets(temp));
	for(i=0; i<n; i++)	solve(i);
	return 0;
}