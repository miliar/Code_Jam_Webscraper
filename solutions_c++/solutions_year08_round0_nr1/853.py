#include<cstdio>
#include<cstring>
const int ml=105,mh=397,ms=105;

struct node
{
	char s[ml];
	node *nxt;
}*h[mh],pool[ms];

char in[ml];
int T,n,q,pp;

unsigned hash(char *s)
{
	unsigned h=0;
	while(*s)h=(h<<6)+(h<<16)-h+*(s++);
	return h%mh;
}
bool insert(char *s)
{
	int hs=hash(s);
	for(node *p=h[hs];p;p=p->nxt)
		if(strcmp(s,p->s)==0)return 0;
	strcpy(pool[pp].s,s);
	pool[pp].nxt=h[hs];
	h[hs]=pool+pp++;
	return 1;
}
int main()
{
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int tn=1;tn<=T;tn++)
	{
		pp=0;
		memset(h,0,sizeof(h));
		scanf("%d",&n);	gets(in);
		for(int i=1;i<=n;i++)gets(in);
		scanf("%d",&q);	gets(in);
		int ans=0;
		for(int p=1,c=0;p<=q;p++)
		{
			gets(in);
			if(insert(in))c++;
			if(c==n)
			{
				ans++,pp=0,c=1;
				memset(h,0,sizeof(h));
				insert(in);
			}
		}
		printf("Case #%d: %d\n",tn,ans);
	}
	return 0;
}
