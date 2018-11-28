#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int n ,T , p ,s ,t;
int main()
{
	freopen("b-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	int i , j;
	scanf("%d",&T);
	//getchar();
	for(i = 0 ; i < T ; i ++)
	{
		scanf("%d %d %d",&n , &s,&p);
		int sum = 0;
		for(j = 0 ; j < n ; j ++)
		{
			scanf("%d",&t);
			int a , b ,c , g;
			g = t /3 ;
			if(g*3 == t)
				a =b =c =g;
			else if(t-g*3 == 1)
			{
				a = b = g ;
				c = g+1;
			}
			else
			{
				a =g ;
				b = c = g+1;
			}
			if(c >= p)
				sum ++;
			else if(s > 0 && c+1>= p && (a!= 0 || b!= 0))
			{
				sum++;
				s--;
			}
		}
		printf("Case #%d: %d\n",i+1,sum);
	}
	return 0;
}
