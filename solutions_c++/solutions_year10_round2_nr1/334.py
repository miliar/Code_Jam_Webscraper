#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#define oo 200005


int sign=0,num=0,root=0,g=0,len,p,Node=0,Ans=0,n,m,Test;
bool flag;
char dic[oo],s[oo],d[oo];
int Edge[oo],st[oo],Next[oo],Head[oo],length[oo];

void Add(int u,int v)
{
	Edge[++num]=v,Next[num]=Head[u],Head[u]=num;
	length[num]=g,st[num]=sign+1;
	for (int i=1;i<=g;++i) dic[++sign]=s[i];
}

bool Cmp(int k)
{
	for (int i=1;i<=g;++i)
	if (dic[st[k]+i-1]!=s[i]) return 0;
	return 1;
}

void Build()
{
	len=strlen(d),p=root;
	d[len]='/';
	for (int i=1,j,k;i<=len;){
		g=0,flag=0;
		for (j=i;d[j]!='/';++j)
			s[++g]=d[j];
			
		for (k=Head[p];k;k=Next[k])
		if (length[k]==g){
			if (Cmp(k)){
				p=Edge[k];
				flag=1;break;
			}
		}
		
		if (!flag){
			Add(p,++Node);
			p=Node;
		}
		i=j+1;
		
	}
}

void Ask()
{
	len=strlen(d),p=root;
	d[len]='/';
	for (int i=1,j,k;i<=len;){
		g=0,flag=0;
		for (j=i;d[j]!='/';++j)
			s[++g]=d[j];
			
		for (k=Head[p];k;k=Next[k])
		if (length[k]==g){
			if (Cmp(k)){
				p=Edge[k];
				flag=1;break;
			}
		}
		
		if (!flag){
			Add(p,++Node);
			p=Node;
			++Ans;
		}
		i=j+1;
		
	}
}


void Solve()
{
	num=0,sign=0,Node=0;
	memset(dic,0,sizeof(dic));
	memset(Head,0,sizeof(Head));
	
	scanf("%d%d",&n,&m);
	Ans=0;
	for (int i=1;i<=n;++i){
		memset(d,0,sizeof(d));
		scanf("%s",d);
		Build();
	}
	
	for (int i=1;i<=m;++i){
		memset(d,0,sizeof(d));
		scanf("%s",d);
		Ask();
	}
	
	printf("%d\n",Ans);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&Test);
	
	for (int i=1;i<=Test;++i){
		printf("Case #%d: ",i);
		Solve();
	}
	
	return 0;
}
