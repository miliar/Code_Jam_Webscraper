//operator system:windows xp
//environment:vc++6.0
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<map>
#include <algorithm>
using namespace std;
#define Pi (4*atan(1))
const double eps = 1e-9;
template<class T> T sqr(T x){return x*x;}
void sort1(int a[],int n)
{
	int k,i,j;
	int t;
	for(i=0;i<n-1;i++)
	{
		k=i;
		for(j=i+1;j<n;j++)
			if(a[j]<a[k])k=j;
			t=a[i];a[i]=a[k];a[k]=t;
	}
}
void sort2(int a[100],int n)
{
	int k,i,j;
	int t;
	for(i=0;i<n-1;i++)
	{
		k=i;
		for(j=i+1;j<n;j++)
			if(a[j]>a[k])k=j;
			t=a[i];a[i]=a[k];a[k]=t;
	}
}
int main()
{
int N,m;
int i,j;
long sum;
FILE *fp;
fp=fopen("c:\\out.txt","w");
ifstream cin("in.txt");
cin>>N;
int a[10];
int b[10];
for(i=1;i<N+1;i++)
{
sum=0;
cin>>m;
for(j=0;j<m;j++)
cin>>a[j];
for(j=0;j<m;j++)
cin>>b[j];
sort1(a,m);
sort2(b,m);
for(j=0;j<m;j++)
sum+=a[j]*b[j];


fprintf(fp,"Case #%d: %ld\n",i,sum);
}
cin.close();
fclose(fp);
return 0;
}