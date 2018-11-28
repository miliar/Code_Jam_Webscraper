#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
int a[1200];
char line[1200];
int k;
int mmin(int a,int b){return a<b?a:b;}
int apply()
{
	int i,j;
	char b[1200];
	for(i=0;line[i];i+=k)
	{
		for(j=0;j<k;++j)
		{
			b[i+j]=line[i+a[j]];
		}
	}
	b[i]=0;
	int res=1;
	
	for(i=1;b[i];++i)
	{
		if(b[i]!=b[i-1])
			++res;
	}
	//printf("%s:%d\n",b,res);
	return res;
}
int main()
{
	int n,t;
	freopen("in.txt","r",stdin);
	scanf("%d",&n);	
	for(t=1;t<=n;++t)
	{
		int i,j;
		scanf("%d",&k);
		scanf("%s",line);
		for(i=0;i<k;++i)
			a[i]=i;
		int m=1e9;
		do
		{
			m=mmin(apply(),m);			
		}while(next_permutation(a,a+k));
		printf("Case #%d: ",t);
		printf("%d\n",m);
	}
	return 0;
}