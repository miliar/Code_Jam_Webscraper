#include <iostream>
#include <cstdio>
using namespace std;
int pip[1009];
long long mon[1000000];
int main()
{
	int t;
	cin >>t;
	for(int i=1;i<=t;i++)
	{
		int r,k,n;
		cin >> r >> k >> n;
		for(int j=1;j<=n;j++)
			scanf("%d",&pip[j]);
		long long mony=0;
		long long dast=0;
		long long jam=0;
		long long sar=1,tah=1;
		long long end=n;
		while(dast<r)
		{
			jam=0;
			while( tah<=end &&jam+pip[tah]<=k)
			{
				mony+=pip[tah];
				jam+=pip[tah];
				tah++;
			}
			dast++;
			for(int j=sar;j<tah;j++)
				pip[++end]=pip[j];
			sar=tah;
		}
		cout <<"Case #" << i << ": " <<  mony << endl;
	}
	return 0;
}
		
		
				
