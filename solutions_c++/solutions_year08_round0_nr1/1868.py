#include<cstdio>
#include<string>
int t,n,m,i,j,k;
char a[101][100],b[1001][100];
int s[2][101],last,cur,min1,p1,min2,p2;
int _m(int x,int y)
{
	return x<y?x:y;
}
int min(int x,int y,int z)
{
	return _m(x,_m(y,z));
}
int main()
{
	freopen("Input.in","r",stdin);
	freopen("Output.out","w",stdout);
	scanf("%d",&t);
	while(t)
	{
		k++;
		scanf("%d ",&n);
		for(i=1;i<=n;i++)
		{
			gets(a[i]);
			s[cur][i]=0;
		}
		scanf("%d ",&m);
		for(i=1;i<=m;i++)
			gets(b[i]);
		for(j=1;j<=m;j++)
		{
			last=cur;
			cur^=1;
			min1=3000;min2=3000;
			for(i=1;i<=n;i++)
				if(min1>s[last][i]) 
				{
					min2=min1;
					p2=p1;
					min1=s[last][i];
					p1=i;
				}
				else
					if(min2>s[last][i])
					{
						min2=s[last][i];
						p2=i;
					}
			for(i=1;i<=n;i++)
				if(strcmp(a[i],b[j])==0)
					s[cur][i]=3000;
				else
				{
					s[cur][i]=min(s[last][i],min1+1,min2+1);
				}
		}
		min1=3000;
		for(i=1;i<=n;i++)
			if(s[cur][i]<min1) min1=s[cur][i];
		printf("Case #%d: %d\n",k,min1);
		t--;
	}
	fclose(stdout);
	return 0;
}
