#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>
#include <queue>
#include <cstring>
#include <set>
#include <map>
#include <sstream>
#include <cmath>
#include <fstream>
#include <list>
using namespace std;
#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define pb push_back
#define L(s) (int)s.size()
#define mp make_pair
#define pii pair<int,int>
#define x first 
#define y second
#define inf 1000000000
#define VI vector<int>
#define ll long long
#define all(s) (s).begin(),(s).end()
#define C(u) memset((u),0,sizeof((u)))
#define ull unsigned ll
#define uint unsigned int
int pr[1111];
inline int gcd(int x,int y)
{
	while(x&&y)
		if (x>=y)
			x%=y;
		else
			y%=x;
	return x+y;
}
int was[1111];
inline int num(VI v)
{
	int ans=1;
	C(was);
	for(int i=0;i<L(v);++i)
	{
		bool ok=1;
		int x=v[i];
		for(int j=0;j<1111;++j)
			if (pr[j])
			{
				int cur=0;
				while(x%j==0)
				{
					x/=j;
					cur++;
				}
				if (cur>was[j])
					ok=0;
				was[j]=max(was[j],cur);
			}
		if (!ok || (i==0 && v[i]==1))
			ans++;
	}
	return ans;
}
VI v;
int tests,n;
int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tests;
	for(int test=1;test<=tests;++test)
	{
		cin>>n;
		VI v(1,1);
		VI v2(0);
		for(int i=2;i<=n;++i)
			pr[i]=1;
		for(int i=2;i<=n;++i)
			if (pr[i])
			{
				int x=i;
				for(x=i;x<=n;x*=i)
					v.pb(x);
				x/=i;
				v2.pb(x);
				for(int j=2*i;j<=n;j+=i)
						pr[j]=0;
			}
		cerr<<num(v)<<" "<<num(v2)<<endl;
		cout<<"Case #"<<test<<": ";
		if (n==1)
			cout<<"0\n";
		else
			cout<<num(v)-num(v2)<<endl;
	}
}
