#include<iostream>
#include<algorithm>
#include<cmath>

using namespace std;

#define MAX 105
#define M 16141

struct Hash
{
	char key[MAX];
	int next;
}h[10005];
int p[M],q[M];
char s[MAX];
int nh;

int ELFhash(char*key)
{
	unsigned long h=0;
	while(*key)
	{
		h=(h<<4)+*key++;
		unsigned long g=h & 0xf0000000L;
		if(g)
			h^=g>>24;
		h&=~g;
	}
	return h%M;
}
void insert(char*key)
{
	int u=ELFhash(key);
	strcpy(h[++nh].key,key);
	if(p[u]==0)
		p[u]=nh;
	else h[q[u]].next=nh;
	q[u]=nh;
	h[nh].next=0;
	return;
}
int find(char*key)
{
	int u,i;
	u=ELFhash(key);
	for(i=p[u];i;i=h[i].next)
	{
		if(strcmp(h[i].key,key)==0)
			return i;
	}
	return -1;
}

int main()
{
	int t,cas=1,n,m,i,j,k,l,ans;
	freopen("in.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&m);
		memset(p,0,sizeof(p));
		for(nh=i=0;i<n;i++)
		{
			scanf("%s",s);
			l=strlen(s);
			for(j=1;j<l;j++)
			{
				if(s[j]=='/')
				{
					s[j]='\0';
					if(find(s)==-1)
						insert(s);
					s[j]='/';
				}
			}
			if(find(s)==-1)
				insert(s);
		}
		for(ans=i=0;i<m;i++)
		{
			scanf("%s",s);
			l=strlen(s);
			for(j=1;j<l;j++)
			{
				if(s[j]=='/')
				{
					s[j]='\0';
					if(find(s)==-1)
					{
						insert(s);
						ans++;
					}
					s[j]='/';
				}
			}
			if(find(s)==-1)
			{
				insert(s);
				ans++;
			}
		}
		printf("Case #%d: %d\n",cas++,ans);
	}
	return 0;
}
