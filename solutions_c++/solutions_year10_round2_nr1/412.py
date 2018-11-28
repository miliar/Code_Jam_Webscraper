#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
using namespace std;

const int mx=100010;

struct dir
{
	string s;
	vector<int> v;
}e[mx];

int pp;
int n,m,ans;
int root;

int cr(string s)
{
	e[pp].s=s;
	e[pp].v.clear();
	return pp++;
}

void init()
{
	pp=0;ans=0;
	root=cr("/");
}

char ss[11000];
int ps;
string str[10000];

void add_init(char *s)
{
	ps=0;
	int i=1,j,k,len=strlen(s);
	while(i<len)
	{
		j=i+1;
		str[ps]="";
		while(j<len&&s[j]!='/') j++;
		//printf("i=%d,j=%d\n",i,j);
		for(k=i;k<j;k++)
		{
			str[ps]+=(s[k]);
		}
		ps++;
		i=j+1;
	}
}

void add(char *s,bool aa)
{
	int i,j;
	add_init(s);
	/*
	for(i=0;i<ps;i++)
	{
		printf("%s ",str[i].c_str());
	}printf("\n");
	*/
	int p=root,q;
	for(i=0;i<ps;i++)
	{
		for(j=0;j<e[p].v.size();j++)
		{
			q=e[p].v[j];
			if(e[q].s==str[i])
			{
				break;
			}
		}
		if(j==e[p].v.size())
		{
			if(aa)ans++;
			q=cr(str[i]);
			e[p].v.push_back(q);
		}
		p=q;
	}
}

void show()
{
	int i,j;
	for(i=0;i<pp;i++)
	{
		for(j=0;j<e[i].v.size();j++)
		{
			printf("s=%s fa=%d\n",e[e[i].v[j]].s.c_str(),i);
		}
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int tt,ca=1;
	scanf("%d",&tt);
	while(tt--)
	{
		init();
		scanf("%d%d\n",&n,&m);
		int i;
		for(i=0;i<n;i++)
		{
			scanf("%s",ss);
			add(ss,false);
		}
		for(i=0;i<m;i++)
		{
			scanf("%s",ss);
			add(ss,true);
		}
		//show();
		printf("Case #%d: %d\n",ca++,ans);
	}

	return 0;
}
