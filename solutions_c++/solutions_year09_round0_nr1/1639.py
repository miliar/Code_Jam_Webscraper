#include<cstdio>
#include<cstring>
struct Tnode
{
	int next[26];
	bool end;
	void init()
	{
		end=0;
		memset(next,-1,sizeof(next));
	}
}Trie[5000*20];
int total=0;
void insert(char *str,int root)
{
	int i,x;
	for(i=0;str[i];++i)
	{
		x=str[i]-'a';
		if(Trie[root].next[x]==-1)
		{
			Trie[total].init();
			Trie[root].next[x]=total++;
		}
		root=Trie[root].next[x];
	}
	Trie[root].end=1;
}
int a[5000*20];
int c[5000*20];
int b[1000];
int ca,cb,cc;
char str[1000];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Alar.out","w",stdout);
	int L,D,N,i,j,cas,len,k;
	while(scanf("%d%d%d",&L,&D,&N)!=EOF)
	{
		Trie[0].init();
		total=1;
		for(i=0;i<D;++i)
		{
			scanf("%s",str);
			insert(str,0);
		}
		for(cas=1;cas<=N;cas++)
		{
			scanf("%s",str);
			len=strlen(str);
			k=0;ca=1;a[0]=0;
			while(k<len)
			{
				if(str[k]!='(')
				{
					cb=1;b[0]=str[k++]-'a';cc=0;
					for(i=0;i<ca;++i)
						for(j=0;j<cb;++j)
						if(Trie[a[i]].next[b[j]]!=-1)
							c[cc++]=Trie[a[i]].next[b[j]];
				}
				else
				{
					cb=0;k++;
					while(str[k]!=')')
					b[cb++]=str[k++]-'a';k++;
					cc=0;
					for(i=0;i<ca;++i)
						for(j=0;j<cb;++j)
						if(Trie[a[i]].next[b[j]]!=-1)
							c[cc++]=Trie[a[i]].next[b[j]];
				}
				ca=cc;
				for(i=0;i<cc;++i)a[i]=c[i];
			}printf("Case #%d: %d\n",cas,ca);
		}

	}

}
