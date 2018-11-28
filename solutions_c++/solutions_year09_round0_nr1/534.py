#include<iostream>
#include<string>
using namespace std;

char dict[5010][20];
int l,d,n;
bool flag[5010];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	int i,j,k,cas=1,len,tlen,ind;
	for(i=0;i<d;i++)
		scanf("%s",dict[i]);
	string s;
	while(n--)
	{
		printf("Case #%d: ",cas);
		cas++;
		cin>>s;
		len=s.size();
		memset(flag,0,sizeof(flag));
		i=0;
		ind=0;
		while(i<len)
		{
			if(s[i]!='(')
			{
				for(j=0;j<d;j++)
				{
					if(flag[j]==false&&dict[j][ind]!=s[i])
						flag[j]=true;
				}
			}
			else
			{
				string tmp="";
				i++;
				while(s[i]!=')')
				{
					tmp+=s[i];
					i++;
				}
				tlen=tmp.size();
				for(j=0;j<d;j++)
				{
					if(flag[j]==true)
						continue;
					for(k=0;k<tlen;k++)
						if(dict[j][ind]==tmp[k])
							break;
					if(k>=tlen)
						flag[j]=true;
				}
			}
			ind++;
			i++;
		}
		int sum=0;
		for(i=0;i<d;i++)
			if(flag[i]==false)
				sum++;
		printf("%d\n",sum);
	}
	return 0;
}