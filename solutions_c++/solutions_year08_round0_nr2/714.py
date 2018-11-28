#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
struct mm
{
	int from ,to;
}A[105],B[105];
bool com(mm c, mm d)
{
	if(c.from != d.from)
		return c.from <d.from;
	else
		return c.to<d.to;
}
int add (char start[] )
{
	int i,j;
	int temp = 0,sum = 0 ;
	for(j = 0 ; j< strlen(start); j ++)
	{
		if(start[j] !=':')
			temp = temp * 10 +(start[j] - '0' );
		else
			break;
	}
	sum = temp * 60 ;
	temp = 0 ;
	for(i = j+1;i < strlen(start) ; i ++)
		temp = temp * 10 + (start[i] - '0');
	sum += temp;
	return sum;
}
int main()
{
	int test,z,i,j;
	freopen("B-large(1).in","r",stdin);
	freopen("B-large(1).out","w",stdout);

	scanf("%d",&test);
	for(z= 1;z <= test ;z ++)
	{
		int turn ,a,b;
		char start[100],end[100];
		scanf("%d",&turn);
		scanf("%d%d",&a,&b);
		int na =a ,nb = b;
		for(i = 0;i <a ;i ++ )
		{
			scanf("%s%s",&start,&end);
			A[i].from = add(start);
			A[i].to = add(end);
		}
		for(i = 0 ;i < b;i ++)
		{
			scanf("%s%s",&start,&end);
			B[i].from = add(start);
			B[i].to = add(end);
		}
		sort(&A[0],&A[a],com);
		sort(&B[0],&B[b],com);
		int sign[105]= {0};
		for(i = 0 ;i < a;i ++)
			for(j = 0 ;j < b; j++)
			{
				if(A[i].to + turn <= B[j].from && A[i].to + turn < 1440 && !sign[j])
				{
					nb --;
					sign[j] = 1;
					break;
				}
			}
		for(i = 0 ;i < 105;i ++)
			sign[i] = 0 ;
		for(j = 0 ;j < b; j++)
			for(i = 0 ;i < a;i ++)
			{
				if(B[j].to  + turn <= A[i].from&& B[i].to + turn < 1440&& !sign[i])
				{
					na--;
					sign[i] = 1;
					break;
				}
			}
			printf("Case #%d: %d %d\n",z,na,nb);
	}
	return 0;
}