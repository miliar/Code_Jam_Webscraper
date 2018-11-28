#include<stdio.h>
#include<string.h>
bool ok[5010],b[30],brace;
char s[5010][20],t[10000];
int ans,len,i,j,k,L,D,N,w,l,h;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Alarge.txt","w",stdout);
	while (scanf("%d%d%d",&L,&D,&N)==3)
	{
		for (i=0;i<D;i++) 
			scanf("%s",&s[i]);
		for (i=0;i<N;i++)
		{
			scanf("%s",t);
			len=strlen(t);
			memset(ok,1,sizeof ok);
			brace=0;
			for (w=j=0;j<len&&w<L;j++)
			{
				if (t[j]==')') 
				{
					brace=0;
					h=j;
					memset(b,0,sizeof b);
					for (k=l;k<h;k++) b[t[k]-'a']=1;
					for (k=0;k<D;k++)
						if (ok[k]) ok[k]=b[s[k][w]-'a'];
					//for (k=0;k<D;k++) printf("%d ",ok[k]);
					//printf("\n");
					w++;
				}
				else
				if (t[j]=='(') 
				{
					l=j+1;
					brace=1;
				}
				else
				{
					if (!brace)
					{
						for (k=0;k<D;k++)
							if (ok[k]) ok[k]=(s[k][w]==t[j]);
							//for (k=0;k<D;k++) printf("%d ",ok[k]);
							//printf("\n");
						w++;
					}
				}
				
			}
			if (j<len||w<L) ans=0;
			else
			for (ans=j=0;j<D;j++) if (ok[j]) ans++;
			printf("Case #%d: %d\n",i+1,ans);
		}
	}
}
