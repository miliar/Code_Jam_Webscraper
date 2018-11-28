#include <string>
#include <iostream> 
#include <fstream>
#include <math.h>
#include <vector>
#include <time.h>
#include <algorithm>
#include <map>
#include <set>

using namespace std;
const double eps = 1e-8;
#define M_PI       3.14159265358979323846

#ifdef _MSC_VER
#else
typedef long long __int64;
#endif

__int64 graphSum[30][1000];
__int64 graphNext[30][1000];

__int64 solve(__int64 r, __int64 k, vector<__int64> vSz)
{
	__int64 sum = 0;
	int n = (int)vSz.size();
	for (int i=0;i<n;i++)
		sum += vSz[i];
	if (sum < k)
		return r*sum;
	memset(graphSum, 0, sizeof(graphSum));
	memset(graphNext, 0, sizeof(graphNext));
	vector<__int64> vSz2;
	for (int aaa=0;aaa<2;aaa++)
		for (int i=0;i<n;i++)
			vSz2.push_back(vSz[i]);
	for (int i=0;i<n;i++)
	{
		sum = 0;
		int j = i;
		for (;;j++)
		{
			if (sum + vSz2[j] > k)
				break;
			sum += vSz2[j];
		}
		graphSum[0][i] = sum;
		graphNext[0][i] = (j) % n;
	}
	for (int j = 1;j<30;j++)
		for (int i=0;i<n;i++)
		{
			graphNext[j][i] = graphNext[j-1][graphNext[j-1][i]];
			graphSum[j][i] = graphSum[j-1][i] + graphSum[j-1][graphNext[j-1][i]];
		}
	__int64 pos = 0;
	__int64 ans = 0;
	for (int i=30;i>=0;i--)
		if (r & (1LL << i))
		{
			ans += graphSum[i][pos];
			pos = graphNext[i][pos];
		}
	return ans;
}

int main()
{
/*	time_t ct = time(0);
	int dt = 10*60 + 0*1800 + 1*3600;//5*3600 + 1800;
	while (time(0) - ct < dt)
	{
		std::cout<<(dt + ct - time(0))<<' ';
	}
	for (;;)
	{
		std::cout<<char(7);
	}

	return 0;
*/
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t, tn = 0;
	cin>>t;
	while (tn < t)
	{
		++tn;
		__int64 r,k,n;
		cin>>r>>k>>n;
		vector<__int64> v(n);
		for (int i=0;i<n;i++)
			cin>>v[i];
		cout<<"Case #"<<tn<<": "<<solve(r, k, v);
		if (tn != t)
			cout<<endl;
	}




	return 0;
}