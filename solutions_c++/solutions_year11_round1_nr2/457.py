#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#define MAXM 10000

using namespace std;

ifstream fin("B-small-attempt4.in.txt");
ofstream fout("B-small-attempt4.out");

bool hash[26];
int num[26]={1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,
524288,1048576,2097152,4194304,8388608,16777216,33554432};
char a[30],res[30];
int n,m;
struct In
{
	int vis[26];
	int len;
	char w[15];
}s[MAXM];
struct X
{
	bool mark;
	int visit[26];
}b[MAXM];

int check(int x)
{
	int i,j,k,ge=0;
	int tot=0;
	for(i=0;i<26;i++)
	b[tot].visit[i]=s[x].vis[i];
	tot++;
	for(i=0;i<n;i++)
	if(i!=x && s[i].len==s[x].len)
	{
		b[tot].mark=1;
		for(j=0;j<26;j++)
		b[tot].visit[j]=s[i].vis[j];
		tot++;
	}
	if(tot==1) return ge;
	for(i=0;a[i]!='\0';i++)
	{
		bool z=true;
		for(j=0;j<26;j++)
		{
			if(b[0].visit[j])
			{
				z=false;
			}
		}
		if(z) break;
		if(b[0].visit[a[i]-'a'])
		{
			for(j=1;j<tot;j++)
			if(b[j].mark && (b[j].visit[a[i]-'a']==0 || b[j].visit[a[i]-'a']!=b[0].visit[a[i]-'a']))
			{
				b[j].mark=0;
			}
			b[0].visit[a[i]-'a']=0;
		}
		else
		{
			bool q=false;
			for(j=1;j<tot;j++)
			if(b[j].mark && b[j].visit[a[i]-'a'])
			{
				b[j].mark=0;
				q=true;
			}
			if(q) ge++;
		}
	}
	return ge;
}

int main()
{
	int t,cas;
	while(fin>>t)
	{
		for(cas=1;cas<=t;cas++)
		{
			fin>>n>>m;
			int i,j,k;
			for(i=0;i<n;i++)
			{
				fin>>s[i].w;
				s[i].len=strlen(s[i].w);
				for(j=0;j<26;j++)
				s[i].vis[j]=0;
				for(j=0;s[i].w[j]!='\0';j++)
				s[i].vis[s[i].w[j]-'a']+=num[j];
			}
			fout<<"Case #"<<cas<<":";
			while(m--)
			{
				fin>>a;
				int maxs=-1,index;
				for(i=0;i<n;i++)
				{
					k=check(i);
					if(maxs<k)
					{
						maxs=k;
						index=i;
					}
				}
				fout<<' '<<s[index].w;
			}
			fout<<endl;
		}
	}
	return 0;
}
