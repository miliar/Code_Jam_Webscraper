#include <stdio.h>
#include <string.h>
struct Possible
{
	short c[30];
}pos[20];
int sum;
int l,d,n;
char dic[5010][20];
int main ()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);    
	scanf("%d%d%d",&l,&d,&n);
	int i;
	for (i=1;i<=d;i++)
	{
	    scanf("%s",dic[i]);
	}	
	for (i=1;i<=n;i++)
	{
		printf("Case #%d: ",i);
		memset(pos,0,sizeof(pos));
		char str[500];
		scanf("%s",str);

		int p=0;
		int j;
		for (j=1;j<=l;j++)		
		{
			if (str[p]=='(') 
			{
				int q;
				for (q=p+1;str[q]!=')';q++)
				{
					pos[j].c[str[q]-'a']=1;
				}
				p=q+1;
			}
			else 
			{				
				pos[j].c[str[p]-'a']=1;
				p++;
			}
		}
		sum=0;
		
		for (j=1;j<=d;j++)
		{
            int k;
            for (k=0;k<l;k++) if (!pos[k+1].c[dic[j][k]-'a']) break;
            if (k>=l) sum++;
        }

		printf("%d\n",sum);
	}
	return 0;
}











