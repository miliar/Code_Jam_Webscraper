#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<cstring>
#include<memory.h>
using namespace std;
char a[10] , b[10], c[10];
int count[7];
int num , aa ,bb , len;
int make( char* t)
{
	int len = strlen(t) , i ,sum = 0;
	for(i = 0 ; i < len ; i ++)
		sum = sum*10 + t[i]-'0' ;
	return sum ;
}
bool Try(int s , int pl)
{
	int i  , j , jj,sum  , sum1 = 0;
	if(pl == len)
	{
		for(i = 0 ; i < len ; i ++)
			sum1 = sum1*10 + c[i] - '0';
		if(sum1 < aa)
			return true;
		if(sum1 >= bb)
			return false;
			jj = 0;
		for(i = 1 ; i < len ; i ++)
		{
			sum =0;
			for(j = i ; j < len ; j ++)
				sum = sum*10 + c[j] - '0';
			for(j = 0 ; j < i ; j ++)
				sum = sum*10 + c[j] - '0';
			//printf("%d %d\n",sum1,sum);scanf("%d",&jj);
			if(sum <= bb && sum > sum1 )
			{
				for(j = 0 ;  j < jj; j ++ )
				{
					if(count[j] == sum)
						goto next;
				}
				//printf("%d %d\n",sum1,sum);
				count[jj++] = sum;
				num ++;
				next:;
			}
		}
		return true;
	}
	for(i = s ; i <= 9 ; i ++)
	{
		c[pl] = '0' + i;
		if(Try(0 , pl+1) == false)
			return false;
	}
	return true;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int n  , i ;
	scanf("%d",&n);
	for(i = 1 ; i <= n ; i ++)
	{
		num = 0;
		scanf("%s %s",a, b);
		aa = make(a);
		bb = make(b);
		//printf("%d %d\n",aa,bb);
		len = strlen(a);
		Try(a[0] - '0' , 0 );
		printf("Case #%d: %d\n",i,num);
	}
	return 0;
}

