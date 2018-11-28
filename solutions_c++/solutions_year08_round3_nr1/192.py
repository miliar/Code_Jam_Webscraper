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
		long long p,k,l;
		long long res=0;
		cin >> p >> k >> l;
		vector<long long> freq(l);

		REP(i, l)
		{
			cin >> freq[i];
		}
		SORT(freq);


		long long kk=0;
		long long pp=0;

		while(!freq.empty())
		{
			long long tmp = freq.back();
			freq.pop_back();

			res+=tmp*(pp+1);

			kk++;
			if(kk==k)
			{
				pp++;
				kk=0;
			}
		}
		cout << "Case #" << test+1 << ": " << res << endl;
	}
	return 0;
}