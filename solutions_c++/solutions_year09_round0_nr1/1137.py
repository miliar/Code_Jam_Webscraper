#include<stdio.h>
#include<string.h>

int l,d,n,c[5001];
char word[5001][20],lang[2000],poss[1000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	int i,j,k,p,len,cnt;
	for(i=0;i<d;i++)
	{
		scanf("%s",word[i]);
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<d;j++) c[j]=1;
		scanf("%s",lang);
		len=strlen(lang);
		j=0; p=0;
		while(j<len)
		{
			if(lang[j]!='(')
			{
				for(k=0;k<d;k++)
				{
					if(word[k][p]!=lang[j])
					{
						c[k]=0;
					}
				}
				j++; p++;
				continue;
			}
			for(k=0;k<1000;k++) poss[k]=0;
			while(lang[j]!=')')
			{
				j++;
				poss[lang[j]]=1;
			}
			for(k=0;k<d;k++)
			{
				if(poss[word[k][p]]==0)
				{
					c[k]=0;
				}
			}
			j++; p++;
		}
		cnt=0;
		for(j=0;j<d;j++) cnt+=c[j];
		printf("Case #%d: %d\n",i+1,cnt);
	}
	return 0;
}