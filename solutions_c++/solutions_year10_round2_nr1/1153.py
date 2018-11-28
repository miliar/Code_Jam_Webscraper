#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int n,m;

struct Node
{
	int id;
	Node *p[150];
	Node()
	{
		int i;
		id=-1;
		for(i=0;i<150;i++)
			p[i]=NULL;
	}
}root,root2;

int node_id;
int cnt;
int ans;

int getnum(char *s)
{
	int i;
	Node *r=&root;
	for(i=0;s[i];i++)
	{
		if(r->p[s[i]]==NULL)
		{
			r->p[s[i]]=new Node();
		}
		r=r->p[s[i]];
	}
	if(r->id==-1)
		r->id=cnt++;
	return r->id;
}


int getnum2(int *s,int len)
{
	int i;
	Node *r=&root2;
	int res=0;
	for(i=0;i<len;i++)
	{
		if(r->p[s[i]]==NULL)
		{
			r->p[s[i]]=new Node();
			res++;
		}
		r=r->p[s[i]];
	}
	return res;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,ca;
	ca=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&m);
		int i,p,q,z;
		char temp[1010];
		cnt=0;
		ans=0;
		for(i=0;i<n;i++)
		{
			scanf("%s",temp);
			int slen=strlen(temp);
			int templ=0;
			int s[1100];
			int snum=0;
			memset(s,0,sizeof(s));
			for(q=1;q<slen;q++)
			{
				char temps[1000];
				if(temp[q]!='/')
				{
					temps[templ++]=temp[q];
				}
				else
				{
					temps[templ]='\0';
					templ=0;
					int num=getnum(temps);
					s[snum++]=num;
				}
				if(q==slen-1)
				{
					temps[templ]='\0';
					templ=0;
					int num=getnum(temps);
					s[snum++]=num;
				}
			}
			getnum2(s,snum);
		}
		for(i=0;i<m;i++)
		{
			scanf("%s",temp);
			int slen=strlen(temp);
			int templ=0;
			int s[1100];
			int snum=0;
			memset(s,0,sizeof(s));
			for(q=1;q<slen;q++)
			{
				char temps[1000];
				if(temp[q]!='/')
				{
					temps[templ++]=temp[q];
				}
				else
				{
					temps[templ]='\0';
					templ=0;
					int num=getnum(temps);
					s[snum++]=num;
				}
				if(q==slen-1)
				{
					temps[templ]='\0';
					templ=0;
					int num=getnum(temps);
					s[snum++]=num;
				}
			}
			ans+=getnum2(s,snum);
		}
		printf("Case #%d: %d\n",ca++,ans);
		for(i=0;i<150;i++)
		{
			root.p[i]=NULL;
			root2.p[i]=NULL;
		}
	}
	return 0;
}