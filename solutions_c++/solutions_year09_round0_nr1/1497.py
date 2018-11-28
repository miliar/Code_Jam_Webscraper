#include<iostream>
using namespace std;
const int L=20;
const int D=5005;
const int N=505;
int l,d,n;
char txt[D][L],str[N];
int yes[D];
void mark(int k,int l,int r)
{
	int i,j;
	for(i=0;i<d;i++)
	{
		if(!yes[i])continue;
		int work=0;
		for(j=l;j<=r;j++)
		{
			if(str[j]==txt[i][k])
			{
				work=1;
				break;
			}
		}
		if(!work)
		{
			yes[i]=0;
		}
	}
}
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	while(scanf("%d%d%d",&l,&d,&n)!=EOF)
	{
		int i,j,k;
		for(i=0;i<d;i++)
		{
			scanf("%s",txt[i]);
		}
		for(k=1;k<=n;k++)
		{
			scanf("%s",str);
			int len=strlen(str);
			for(i=0;i<d;i++)yes[i]=1;
			for(j=0,i=0;i<len;)
			{
				int l,r;
				if(str[i]=='(')
				{
					l=r=i;
					while(str[r]!=')')r++;
					mark(j,l+1,r-1);
					j++;
					i=r+1;
				}
				else
				{
					mark(j,i,i);
					j++;
					i++;
				}
			}
			int ans=0;
			for(i=0;i<d;i++)
			{
				if(yes[i])ans++;
			}
			printf("Case #%d: %d\n",k,ans);
		}
	}
	return 0;
}