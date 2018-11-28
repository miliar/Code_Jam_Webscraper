#include<cstdio>
#include<cstring>
struct Tnode
{
	Tnode *next[26];
}trie[100000];
Tnode* qq[2][100000];
char str[1000];
int upct,downct,up,down;
int main()
{
	int L,D,N,i,j,ct,x,k;
	Tnode *root;
	freopen("mdzlarge.in","r",stdin);
	freopen("mdza.out","w",stdout);
	while(scanf("%d%d%d",&L,&D,&N)!=EOF)
	{
		ct=0;
		for(i=0;i<26;++i)trie[ct].next[i]=NULL;
		ct++;
		for(i=0;i<D;++i)
		{
			scanf("%s",str);
			root=&trie[0];
			for(j=0;str[j];++j)
			{
				x=str[j]-'a';
				if(root->next[x]==NULL)
				{
					for(k=0;k<26;++k)trie[ct].next[k]=NULL;
					root->next[x]=&trie[ct++];
				}
				root=root->next[x];
			}
		}
		for(i=0;i<N;++i)
		{
			scanf("%s",str);up=0;down=1;
			downct=0;upct=1;qq[0][0]=&trie[0];
			int len=strlen(str);
			for(j=0;j<len;j++)
			{
				if(str[j]!='(')
				{
					x=str[j]-'a';
					for(int ii=0;ii<upct;++ii)
					{
						if(qq[up][ii]->next[x]!=NULL)
						qq[down][downct++]=qq[up][ii]->next[x];
					}
				}
				else
				{
					for(int ii=0;ii<upct;++ii)
						for(k=j+1;str[k]!=')';k++)
						{
							x=str[k]-'a';
							if(qq[up][ii]->next[x]!=NULL)
							qq[down][downct++]=qq[up][ii]->next[x];
						}
					j++;
					while(str[j]!=')')j++;
				}
				up=down;down=1-up;
				upct=downct;downct=0;
			}
			printf("Case #%d: %d\n",i+1,upct);
		}
	}
}
