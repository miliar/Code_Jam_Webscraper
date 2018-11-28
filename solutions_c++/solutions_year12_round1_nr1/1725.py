#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>
using namespace std;
double map[100000]  , k; 
int a, b;
double Try1(double sum)
{
	sum = k* (b-a+1) + (1-k)*(b-a+b+2);
	//printf("1 %lf\n",sum);
	return sum;
}

double Try2(double sum)
{
	
	int i , j ;
	double p = 1 , sum1 = 0;
	for(i = a-1 ; i > 0 ; i --)
	{
		k = k/map[i];
		//printf("%lf\n" , k);
		sum1 = k*(a-i +b - i + 1) + (1-k)*(a-i + b - i +2 + b);
		if(sum > sum1)
			sum = sum1;
	}
	return sum;
}

double Try3(double sum)
{
	if(sum < b+2)
		return sum ;
	return b+2;
}
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("a.out","w",stdout);
	int t , i , j;
	scanf("%d",&t);
	for(i = 1 ; i <= t ; i ++)
	{
		scanf("%d %d",&a,&b);
		for(j = 0 ; j < a ; j ++)
			scanf("%lf",&map[j]);
		k = 1 ;
		for(j = 0 ; j < a ; j ++ )
			k *= map[j];
		double sum = 0 ;
		sum = Try1(sum);
		sum = Try2(sum);
		sum = Try3(sum);
		printf("Case #%d: %.6lf\n",i,sum);
	}
	return 0;
}
