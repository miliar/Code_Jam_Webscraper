#include<iostream>
using namespace std;
#define N 100
int o[N];
bool check(int a,int b)
{
	int c=a+b;
	a=(a>b)?a:b;
	b=c-a;
	if(a==b)
		return false;
	if(a<2*b)
	{
		return !check(a-b,b);
	}
	return true;

}
int main()
{
	int T;
	FILE * fi=fopen("D:\\C-small-attempt1.in","r");
	FILE * fo=fopen("D:\\1.out","w");
	fscanf(fi,"%d",&T);
	int cases=0;
	while(T-->0)
	{
		cases++;
		int a1,a2,b1,b2;
		fscanf(fi,"%d %d %d %d",&a1,&a2,&b1,&b2);
		int counts=0;
		for(int i=a1;i<=a2;i++)
		{
			for(int j=b1;j<=b2;j++)
				if(check(i,j))
					counts++;
		}
		fprintf(fo,"Case #%d: %d\n",cases,counts);
	}
 
	
	return 0;
}