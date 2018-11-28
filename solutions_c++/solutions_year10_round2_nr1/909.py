#include<stdio.h>
#include<string.h>
#include<map>
#include<string>
#include<algorithm>
#include<iostream>
#include<stdlib.h>
using namespace std;
struct Path
{
	int id;
	short next[10000];
}p[10000];
int top;
int n,m;
map<string,int> mp;
int cnt=0;
int pt;
void insert(int key)
{
	if(p[pt].next[key]==-1)
	{
		p[pt].next[key]=top;
		p[top].id=key;
		pt=top;
		top++;
	}
	else
		pt=p[pt].next[key];
}
int res;
void find(int key)
{
	if(p[pt].next[key]==-1)
	{
		p[pt].next[key]=top;
		p[top].id=key;
		pt=top;
		top++;
		res++;
	}
	else
		pt=p[pt].next[key];
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int i,j,k;
	int T;
	int case_cnt=1;
	scanf("%d",&T);
	char temp[200],ch;
	string str;
	int t;
	int min=0;
	while(T--)
	{
		cnt=1,res=0;;
		memset(p,-1,sizeof(p));
		p[0].id=0;
		mp.clear(),top=1;
		scanf("%d%d",&n,&m);
		getchar();
		for(i=0;i<n;i++)
		{
			t=0;
			pt=0;
			ch=getchar();
			while(1)
			{
				t=0;
				while(ch=getchar(),ch!='/'&&ch!='\n')
				{
					temp[t++]=ch;
				}
				temp[t]='\0';
				str=temp;
				if(mp.find(str)==mp.end())
				{
					mp[str]=cnt++;
				}
				insert(mp[str]);
				if(ch=='\n')
					break;
			}
		}
		
		for(i=0;i<m;i++)
		{
			t=0;
			ch=getchar();
			pt=0;
			while(1)
			{
				t=0;
				while(ch=getchar(),ch!='/'&&ch!='\n')
				{
					temp[t++]=ch;
				}
				temp[t]='\0';
				str=temp;
				if(mp.find(str)==mp.end())
				{
					mp[str]=cnt++;
				}
				find(mp[str]);
				if(ch=='\n')
					break;
			}
		}
		printf("Case #%d: %d\n",case_cnt++,res);
		if(top>min)
			min=top;
	}
	//printf("%d\n",min);
}