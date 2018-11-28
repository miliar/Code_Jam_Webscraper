#include <iostream>
using namespace std;
int D[20000],L[20000],n,TD,maxl[20000];
int main()
{
	freopen("A.txt","r",stdin);
	freopen("out.txt","w",stdout);
		
	int cn=0;
	scanf("%d",&cn);
	for (int cs=1;cs<=cn;cs++)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%d %d",&D[i],&L[i]);
		}
		scanf("%d",&TD);
		D[0]=0;
		memset(maxl,0,sizeof(maxl));
		maxl[0]=D[1];

		for (int i=1;i<=n;i++)
		{
			for (int j=0;j<i;j++)
			{
				if (maxl[j]+D[j]>=D[i])
					maxl[i]=max(maxl[i],min(L[i],(D[i]-D[j])));
			}
		}
		bool flag=false;
		for (int i=0;i<=n;i++)
		{
			if (maxl[i]+D[i]>=TD)
				flag=true;
		}
		cout<<"Case #"<<cs<<": ";
		if (flag)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}

	return 0;
}