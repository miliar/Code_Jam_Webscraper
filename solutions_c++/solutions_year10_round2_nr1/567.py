#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <string>

using namespace std;

map<string,int>mymap;
int ans=0;
struct test
{
	string name;
	int son,right;
}build[2000000];
int tt=1;
char ss[110];
string zi[101];
int ro;

void solve(int k,int a)
{
	if(a>ro) return ;
	if(build[k].son==0)
	{
		ans++;
		build[k].son=tt;
		build[tt].name=zi[a];
		build[tt].right=0;build[tt].son=0;
		tt++;
		solve(tt-1,a+1);
	}
	else
	{
		int p,hea;
		for(p=build[k].son;p;p=build[p].right)
		{
			if(build[p].name==zi[a])
			{solve(p,a+1);break;}
			hea=p;
			
		}
		if(!p)
		{
			ans++;
			build[hea].right=tt;
			build[tt].name=zi[a];
			build[tt].right=0;build[tt].son=0;
			tt++;
			solve(tt-1,a+1);
		}
	}
}

int main()
{
	freopen("test.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int case_t;
	int i,j;
	int oop=1;
	scanf("%d",&case_t);
	while(case_t--)
	{
		mymap.clear();
		tt=1;
		ans=0;
		int n,m;
		int ppp=1;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;++i)
		{
			scanf("%s",ss);
			ro=0;
			j=0;
			ss[strlen(ss)]='#';
			while(ss[j]!='#')
			{
				if(ss[j]=='/')
				{ro++;zi[ro]="";}
				else
					zi[ro]+=ss[j];
				j++;
			}
			if(mymap[zi[1]]==0)
			{
				mymap[zi[1]]=tt;
				build[tt].name=zi[1];
				build[tt].right=0;
				build[tt++].son=0;
			}
			int hj=mymap[zi[1]];
			solve(hj,2);
		}
		ans=0;
		for(i=0;i<m;++i)
		{
			scanf("%s",ss);
			ro=0;
			j=0;
			ss[strlen(ss)]='#';
			while(ss[j]!='#')
			{
				if(ss[j]=='/')
				{ro++;zi[ro]="";}
				else
					zi[ro]+=ss[j];
				j++;
			}
			if(mymap[zi[1]]==0)
			{
				ans++;
				mymap[zi[1]]=tt;
				build[tt].name=zi[1];
				build[tt].right=0;
				build[tt++].son=0;
			}
			int hj=mymap[zi[1]];
			solve(hj,2);
		}
		printf("Case #%d: %d\n",oop++,ans);
	}
}