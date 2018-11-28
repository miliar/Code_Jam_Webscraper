#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;
#define maxn 2000000
int d[100];

void init()
{
	d[0]=1;
	for(int i=1;i<=10;i++)
		d[i]=10*d[i-1];
}
int a,b;
int weishu(int tmp)
{

	int n=0;
	while(tmp)
	{
		tmp/=10;
		n++;
	}
	return n;
}
	int fa[maxn];
int find(int tmp)
{
	memset(fa,0,sizeof(fa));
	int n=weishu(tmp);
	int ret=0;
	int t=tmp;
	int index;
	for(int i=0;i<n-1;i++)
	{
		index=t%10;
		t=t/10;
		t=t+index*d[n-1];
		if(t>tmp&&t<=b&&fa[t]==0)
		{
			ret++;
			fa[t]=1;
		}
	}
	return ret;
}
int main()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("data.out");
	init();
	int k=1;
	int N;
	cin>>N;
	while(N--)
	{
		cin>>a>>b;
		int ret=0;
		for(int i=a;i<=b;i++)
		{
			ret+=find(i);
		}
		cout<<"Case #"<<k++<<": "<<ret<<endl;
	}
	return 0;
}