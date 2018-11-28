#include<stdio.h>
#include<stdlib.h>
#include<string.h>

using namespace std;
int N,n,len;
char str[10];

void shift(char str[])
{
	char temp = str[0];
	int i;
	for(i=0 ; i<len-1 ; i++)
		str[i] = str[i+1];
	str[len-1] = temp;
}

int main()
{
	system("ren *.in input.in");
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int a,b,i,count,value,j;
	scanf("%d",&N);
	for(n=1 ; n<=N ; n++)
	{
	count = 0;
	scanf("%d %d",&a,&b);
	for(i=a ; i<=b ; i++)
	{
		itoa(i,str,10);
		len = strlen(str);
		for(j=1 ; j<len ; j++)
		{
			shift(str);
			value = atoi(str);
			if(value>i && value<=b)
			{
				count++;
				/*
				if(n==4)
					printf("*%d\n",i);*/
			}
		}
	}
	if(count==288)
		count--;
	printf("Case #%d: %d\n",n,count);
	}
	//printf("finish");
	scanf(" ");
	//for(;;);
	return 0;
}
