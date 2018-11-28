#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	
	int N;
	cin >> N;

	REP(test, N)
	{		
		unsigned long long n, m, X, Y, Z;
		cin >> n >> m >> X >> Y >> Z;
		vector<unsigned long long> sl;
		vector<unsigned long long> A(m);
		sl.clear();

		REP(i,m)
			cin >> A[i];
		for(unsigned long long i=0;i<n;i++)
		{
			sl.pb(A[i%m]);
			A[i%m] = ( X*A[i%m] + Y*(i + 1) )%Z;
		}

		vector<unsigned long long> r(n);
		for(int i=n-1;i>=0;i--)
		{
			r[i]=1;
			for(int j=i+1; j<n; j++)
			{
				if(sl[i]<sl[j])
					r[i] += r[j];
				r[i]%=1000000007ULL;
			}
		}

		unsigned long long sum=0;
		REP(i,n)
		{
			sum+=r[i];			
			sum%=1000000007ULL;
		}
		

		cout << "Case #" << test+1 << ": " << sum << endl;
	}
	return 0;
}