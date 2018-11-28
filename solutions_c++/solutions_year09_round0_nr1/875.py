#include<stdio.h>
#include<algorithm>
#include<string>
using namespace std;

int l,d,n;
char in[5003][17];
bool pat[17][27];

char ch[1000];

int main()
{
    freopen("my.in","r",stdin);
    freopen("my.out","w",stdout);

	int i,j,k;
    int ans;
	int len;
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++)
		scanf("%s",in[i]);
    for(k=1;k<=n;k++)
	{
	    scanf("%s",ch);
		len=strlen(ch);
	    for(i=0;i<l;i++)
			for(j=0;j<26;j++)
			{
			     pat[i][j]=false;
			}
	    j=0;
		for(i=0;i<len;)
		{
		    if(ch[i]!='(')
			{
			   pat[j++][ch[i]-'a']=true;
			   i++;
			}
			else
			{
			   i++;
			   while(ch[i]!=')')
			   {
				   pat[j][ch[i]-'a']=true;
			       i++;
			   }
			   i++;
			   j++;
			}
		}
		ans=0;
		for(i=0;i<d;i++)
		{
		    for(j=0;j<l;j++)
			{
			    if(pat[j][in[i][j]-'a']==false)
					break;
			}
			if(j==l)
				ans++;
		}
		printf("Case #%d: %d\n",k,ans);
	}
    return 0;
}