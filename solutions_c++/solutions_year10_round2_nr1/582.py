#include <iostream>
#include <string>
#include <map>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	map<string,int> tmpMap;
	char A[200][200];
	char B[200][200];
	int t,i,j;
	int p,q;
	int n,m;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		tmpMap.clear();
		scanf("%d%d",&n,&m);
		for (j=0;j<n;j++)
		{
			scanf("%s",&A[j]);
		}
		for (j=0;j<m;j++)
		{
			scanf("%s",&B[j]);
		}
		for (p=0;p<n;p++)
		{
			int len=strlen(A[p]);
			string ss="";
			for (q=0;q<len;q++)
			{
				if (A[p][q]=='/')
				{
					tmpMap[ss]=1;
					//cout<<ss<<endl;
					//ss=ss+A[p][q];
				}
				ss=ss+A[p][q];
			}
			tmpMap[ss]=1;
		}
		int ans=0;
		for (p=0;p<m;p++)
		{
			int len=strlen(B[p]);
			string ss="";
			for (q=0;q<len;q++)
			{
				if (B[p][q]=='/')
				{
					if (ss!=""&&tmpMap[ss]!=1)
					{
						ans++;
			//			cout<<ans<<" "<<ss<<endl;
						tmpMap[ss]=1;
					}
				}
				ss=ss+B[p][q];
			}
			if (ss!=""&&tmpMap[ss]!=1)
			{
				ans++;
			//	cout<<ss<<endl;
				tmpMap[ss]=1;
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}