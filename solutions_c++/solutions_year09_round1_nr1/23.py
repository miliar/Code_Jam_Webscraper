#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<map>
#include<set>
#include<algorithm>

using namespace std;

const int inf = 2147483647;
const double pi = acos(-1.0);
const double eps = 1e-7;

int base;

int D(int a)
{
	if(a==0) return 0;
	return D(a/base) + (a%base)*(a%base);
}

int u[100000000];

int get(int x)
{
	if(u[x]!=0) return u[x];
	u[x] = -1;
	return u[x]=get(D(x));
}

int mask[12000000];
int con[100000000],cnt,con2[100000000],cnt2;
int out[1<<10];

int main()
{
	base = 9;
		for(base=2;base<=10;base++)
		{
			memset(u,0,sizeof(u));
			fprintf(stderr,"%d\n",base);
			u[1]=1;
			for(int i=2;i<12000000;i++)
			{
				int x = get(i);
				//printf("%d\n",x);
				if(x==1)
				{
					mask[i] |= (1<<(base-2));
				}
			}
		}
	int ntest;
	string s;
	
	memset(out,-1,sizeof(out));
	cin>>ntest; getline(cin,s); 
	for(int test=1;test<=ntest;test++)
	{
		getline(cin,s);
		stringstream sin(s);
		int b = 0, ans=-1,x;
		while(sin>>x)
		{
			b |= (1<<(x-2));
		}
		if(out[b]!=-1) ans = out[b];
		else
		{
			for(int i=2;i<12000000;i++)
				if((mask[i]&b)==b)
				{
					ans = i;
					break;
				}
			out[b] = ans;
		}
		printf("Case #%d: %d\n",test,ans);
	}
	/*
	for(int b=0;b<(1<<9);b++)
	{
		int ans = -1;
		for(int i=2;i<12000000;i++)
			if((mask[i]&b)==b)
			{
				ans = i;
				break;
			}
		if(ans==-1)
		{
			bool first = true;
			for(int k=8;k>=0;k--) if(ans&(1<<k))
			{
				base = k+2;
				memset(u,0,sizeof(u)); u[1]=1;
				if(first)
				{
					fprintf(stderr,"begin! %d\n",b);
					cnt = 0;
					for(int i=2;i<100000000;i++)
						if(get(i)==1)
						{
							con[cnt++] = i;
						}
					fprintf(stderr,"finish! %d\n",cnt);
					first = false;
				}
				else
				{
					cnt2 = 0;
					for(int i=0;i<cnt;i++)
						if(get(con[i])==1)
						{
							con2[cnt2++] = con[i];
						}
					for(int i=0;i<cnt2;i++) con[i] = con2[i];
					cnt = cnt2;

					fprintf(stderr,"sub-finish! %d\n",cnt);
				}
			}
			if(cnt)
			{
				sort(con,con+cnt);
				ans = con[0];
			}
			else ans = -1;
		}
		if(ans==-1) printf("%d\n",b);
	}
	*/
	return 0;
}

