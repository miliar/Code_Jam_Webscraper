#include <cstdio>
#include <memory.h>
#include <cstring>
int L,D,N;
struct node
{
	node *d[32];
	node()
	{
		memset(d,0,sizeof(d));
	}
	void add(const char *x,int pos=0)
	{
		if(pos>=L)return;
		int y=x[pos]-'a';
		if(d[y]==0)
			d[y]=new node();
		d[y]->add(x,pos+1);
	}
};
node *root;
char A[16][32];
int lA[16];
int go(int pos=0,node *p=root)
{
	if(pos>=L)
	{
		return 1;
	}
	int r=0,y;
	for(int i=0;i<lA[pos];++i)
	{
		y=A[pos][i]-'a';
		if(p->d[y])
		{
			r+=go(pos+1,p->d[y]);
		}
	}
	return r;
}
void parse(const char *x)
{
	int pos=0;
	for(int i=0;i<L;++i)
	{
		lA[i]=0;
		if(x[pos]=='(')
		{
			while(x[++pos]!=')')
			{
				A[i][lA[i]++]=x[pos];
			}
		}
		else
		{
			A[i][0]=x[pos];
			lA[i]=1;
		}
		++pos;
	}
}
int main()
{
	scanf("%d%d%d",&L,&D,&N);
	root=new node();
	char buff[1024];
	for(int i=0;i<D;++i)
	{
		scanf("%s",buff);
		root->add(buff);
	}
	for(int i=1;i<=N;++i)
	{
		scanf("%s",buff);
		parse(buff);
		printf("Case #%d: %d\n",i,go());
	}
	return 0;
}

