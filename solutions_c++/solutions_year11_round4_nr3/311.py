#include <iostream>
#include <vector>
#include <algorithm>

#define ll long long

using namespace std;

int gcd(int a,int b) { return b==0 ? a : gcd(b,a%b); };

int calc(vector <int> & v)
{
	int ret=0;
	for(int i=0;i<v.size();i++)
	{
		int cur=1;
		for(int j=0;j<i;j++)
		{
			int g=gcd(v[j],v[i]),g1=gcd(g,cur);
			g/=g1; cur*=g;
		}
		if (cur!=v[i]||i==0) ret++;
	}
	return ret;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		int n,mn=0,mx=0;
		scanf("%d",&n);
		for(int i=2;i<=n;i++)
		{
			bool prime=true;
			for(int j=2;j*j<=i;j++)
				if (i%j==0)
				{
					prime=false;
					break;
				}
			if (prime) mn++;
		}
		if (n==1) mn++;
		vector <int> nums;
		for(int i=1;i<=n;i++)
			nums.push_back(i);
		mx=calc(nums);
/*		cout << mx << endl;
		for(int e=0;e<50;e++)
		{
			random_shuffle(nums.begin()+1,nums.end());
			if (calc(nums)>mx) cout << "fail\n";
		}
*/		printf("%d\n",mx-mn);
	}
	return 0;
}