#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define max(a,b) (a > b ? a : b)
#define min(a,b) (a < b ? a : b)
int main()
{
	int T;
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	int d[10003],l[10003];
	int dp[10003];
	for(int ind=1;ind<=T;ind++)
	{
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>d[i]>>l[i];
		cin>>d[n];
		l[n]=0;
		memset(dp,0,sizeof(dp));
		bool res=false;
		int i=0,j=1;
		dp[0]=d[0];
		while(true)
		{
			if(res)break;
			if(i>=n)break;
			while(j<=n && d[j]-d[i]<=dp[i])
			{
				if(j==n){res=true;break;}
				if(d[j]-d[i]>l[j])dp[j]=l[j];
				else dp[j]=d[j]-d[i];
				j++;
			}
			i++;
		}
		//printf("Case #%d: %l\n",ind,res);
		string ret="NO";
		if(res)ret="YES";
		cout<<"Case #"<<ind<<": "<<ret<<endl;
		
	}
}