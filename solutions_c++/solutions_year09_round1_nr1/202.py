#include <iostream>
#include <algorithm>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <string>


using namespace std;

char ff[12][1000000];

bool vst[1000];

void check(int base,int n)
{
	memset(vst,0,sizeof(vst));
	bool ok=false;
	while(1)
	{
		if(vst[n]==true) break;
		vst[n]=true;
		if(n==1)
		{
			ok=true;
			break;
		}
		int s=0;
		while(n)
		{
			int b=n%base;
			s+=b*b;
			n/=base;
		}
		n=s;
	}
	int i;
	for(i=2;i<1000;i++)
	{
		if(vst[i])
		{
			ff[base][i]=ok?1:0;
		}
	}
}

bool fun(int base,int n)
{
	if(n==1) return true;
	if(ff[base][n]!=-1) return ff[base][n]!=0;
	if(n<1000)
	{
		check(base,n);
		return ff[base][n]!=0;
	}
	int s=0;
	while(n)
	{
		int b=n%base;
		s+=b*b;
		n/=base;
	}
	return ff[base][s]=fun(base,s);
}
char buf[200];
bool kk[12];
int main()
{
	memset(ff,0xff,sizeof(ff));
	int t;
	scanf("%d",&t);
	gets(buf);
	int cse=0;
	while(t--)
	{
		cse++;
		gets(buf);
		istringstream is(buf);
		memset(kk,0,sizeof(kk));
		int x;
		while(is>>x)
		{
			kk[x]=true;
		}
		int i;
		for(i=2;;i++)
		{
			bool ok=true;
			int j;
			for(j=2;j<=10;j++)
			{
				if(kk[j]&&!fun(j,i))
				{
					ok=false;
					break;
				}
			}
			if(ok) break;
		}
		printf("Case #%d: %d\n",cse,i);
	}
	return 0;
}
