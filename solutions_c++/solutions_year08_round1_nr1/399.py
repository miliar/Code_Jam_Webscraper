#include<ctime>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
typedef istringstream iss; typedef ostringstream oss; typedef long long int lli;
const double TOLL=1e-9;

int main()
{
	int t; cin>>t; vector<lli> x; vector<lli> y;
	int cn=0;
	while(t--)
	{
		cn++;
		int n; cin>>n;
		x.resize(n); y.resize(n);
		for(int i=0;i<n;i++) cin>>x[i];
		for(int i=0;i<n;i++) cin>>y[i];
		sort(x.begin(),x.end()); sort(all(y));
//		for(int i=0;i<n;i++) cout<<x[i]<<' '; cout<<endl;
//		for(int i=0;i<n;i++) cout<<y[i]<<' '; cout<<endl;

		int xind=0, yind=n-1;
		lli sum=0;
		while(xind<n)
		{
			sum+=x[xind]*y[yind];
			xind++; yind--;
		}
		cout<<"Case #"<<cn<<": "<<sum<<endl;
	}

	return 0;
}
