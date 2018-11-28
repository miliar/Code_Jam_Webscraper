#include <iostream>
#include <string>
using namespace std;
#define  maxn 300
int index[maxn];
int flag[maxn];
int main()
{
	int i,j;
	int t;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>t;
	for(int cas=1;cas<=t;cas++)
	{
		string str;
		cin>>str;
		for(i=0;i<maxn;i++) 
		{
			index[i]=-1;
			flag[i]=0;
		}
		flag[1]=1;
		index[str[0]]=1;
		int base=2;
		for(i=1;i<str.size();i++)
		{
			if(index[str[i]]==-1)
			{
				for(j=0;j<maxn;j++)
				{
					if(flag[j]==0)
					{
						index[str[i]]=j;
						flag[j]=1;
						if(j+1>base) base=j+1;
						break;
					}
				}
			}
		}
		__int64 ans=0;
		for(i=0;i<str.size();i++)
		{
			ans=ans*base+index[str[i]];
		}
		printf("Case #%d: ",cas);
		printf("%I64d\n",ans);
		

	}
	return 0;

}