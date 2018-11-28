#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <fstream>

using namespace std;

typedef long long _ll;
typedef vector<int> _vi;
typedef vector<_ll> _vll;
typedef vector<string> _vs;
typedef istringstream _iss;
#define _a(v) (v).begin(),(v).end()
#define _e(x,y) (fabs((x)-(y))<1e-10)
#define _p push_back
#define _mp make_pair
#define _m(v) memset(v,0,sizeof(v));
#define _f(i,b,e) for(int i=b;i<e;i++)
#define _fl(i,n) for(int i=0;i<(n).length();i++)
#define _fs(i,n) for(int i=0;i<(n).size();i++)
#define _fe(t,i,n) for(t::iterator i=(n).begin();i!=(n).end();i++)
#define _fd(t,e) ((t).find(e)!=(t).end())
#define _s(x,y) {x+=y;y=x-y;x-=y;}
#define _st(x, y, t) {t _t_; _t_=x;x=y;y=_t_;}

#define FILE_INPUT

#ifdef FILE_INPUT
	#define is_ file_in
	#define os_ file_out
#else
	#define is_ cin
	#define os_ cout
#endif



int zcnt;

int main()
{
#ifdef FILE_INPUT
	ifstream file_in;
	ofstream file_out;
	file_in.open(L"in.txt");
	file_out.open(L"out.txt");
#endif

	is_>>zcnt;
	for(int zi=1; zi<=zcnt; zi++)
	{
		long long ans[1010], total = 0;
		long long A[1010], num[1010];
		long long n, m, X, Y, Z, t;
		is_>>n>>m>>X>>Y>>Z;
		for(int i=0; i<m; i++)
			is_>>A[i];
		for(int i=0; i<n; i++)
		{
			num[i] = A[i%m];
			A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
		}
		memset(ans, 0, sizeof(ans));
		total = n;
		for(int i=1; i<n; i++)
		{
			for(int j=0; j<i; j++)
			{
				if(num[i] > num[j])
					ans[i] += ans[j]+1;
				if(ans[i] > 1000000007)
					ans[i] -= 1000000007;
			}
			total += ans[i];
			if(total > 1000000007)
				total -= 1000000007;
		}
		os_<<"Case #"<<zi<<": "<<total % 1000000007<<endl;
	}


#ifdef FILE_INPUT
	file_in.close();
	file_out.close();
#endif
	return 0;
}