#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

#define ll long long

using namespace std;

ll gcd(ll a,ll b) {return (b==0) ? a : gcd(b,a%b);}
ll lcd(ll a,ll b) {return (a/gcd(a,b))*b;}

int main()
{
//	ifstream dat("input.txt");
//	ofstream sol("output.txt");
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,n,r,k;
	scanf("%d",&t);
	for(int j=0;j<t;j++)
	{
		//dat >> r >> k >> n;
		scanf("%d%d%d",&r,&k,&n);
		ll Ans=0;
		vector <long> nums(n,0);
		for(int i=0;i<n;i++)
			scanf("%d",&nums[i]);
			//dat >> nums[i];
		vector <long> ans(n,0),next(n,0);
		for(int i=0;i<n;i++)
		{
			int h=i,num=0,sum=0;
			while(sum+nums[h]<=k&&num<n)
			{
				num++;
				sum+=nums[h++];
				h%=n;
			}
			ans[i]=sum;
			next[i]=h;
		}
		int cur=0;
		for(int i=0;i<r;i++)
		{
			Ans+=(ll)ans[cur];
			cur=next[cur];
		}
		printf("Case #%d: %I64d\n",j+1,Ans);
		//sol << "Case #" << j+1 << ": " << Ans << endl;
		/*for(int i=0;i<n;i++)
			sol << ans[i] << "	";
		sol << endl;
		for(int i=0;i<n;i++)
			sol << next[i] << "	";
		sol << endl;*/
	}
//	sol << gcd(26000000,gcd(11000000,6000000)) << endl;
//	sol << lcd(26000000+4000000,gcd(11000000+4000000,6000000+4000000)) << endl;
	return 0;
}
