#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <ctime>
#include <sstream>
#include <iomanip>
#include <map>
#include <set>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef set<int> SI;
typedef set<string> SS;
typedef long long ll;
typedef unsigned long long ull;

#define REP(i,n) for(int i=0;i<(n);++i)
#define DREP(i,n) for(int i=(n)-1;i>=0;--i)
#define FOR(i,n,m) for(int i=(n);i<(m);++i)
#define DFOR(i,n,m) for(int i=(n);i>=(m);--i)
#define LOOP for(;;)
#define zero(n) memset((n),0,sizeof(n))
#define RMB(x) (x).erase((x).begin())
#define RME(x) (x).erase((x).end()-1)
#define SORT(x) sort((x).begin(),(x).end())
#define PB push_back
#define ISS istringstream
#define OSS ostringstream


int main()
{
	int t;

	cin >> t;
	REP ( i, t ) {
		set<string> dire;
		set<string> dire2;
		set<string> exist;
		set<string> wtm;

		int n, m;
		string tmp;

		cin >> n >> m;
		REP ( k, n ) {
			cin >> tmp;
			dire.insert(tmp);

		}
		REP ( k, m ) {
			cin >> tmp;
			dire2.insert(tmp);

		}

		set<string>::iterator it, it2;
		it = dire.begin();
		while ( it != dire.end() ) {
			int p = 1;
			string bef;
			string tm = *it;
			tmp = "";
			tm = tm + "/";
			REP ( j, tm.length() ) {
				tmp = tmp + tm[j];
				if ( tm[j] == '/' ) {
					bef = bef + tmp;
					if ( bef != "/" ) exist.insert( bef );
					tmp = "";

				}

			}
			++it;

		}

		it = dire2.begin();
		while ( it != dire2.end() ) {
			int p = 1;
			string bef;
			string tm = *it;
			tmp = "";
			tm = tm + "/";
			REP ( j, tm.length() ) {
				tmp = tmp + tm[j];
				if ( tm[j] == '/' ) {
					bef = bef + tmp;
					if ( bef != "/" ) wtm.insert( bef );
					tmp = "";

				}

			}
			++it;

		}

		int ans = 0;

		it = wtm.begin();
		while ( it != wtm.end() ) {
			int flag = 0;
			it2 = exist.begin();
			while ( it2 != exist.end() ) {
				if ( *it2 == *it ) {
					flag = 1;
					break;

				}
				it2++;

			}
			if ( flag == 0 ) ans++;
			it++;

		}

		cout << "Case #" << i+1 << ": " << ans << endl;

	}

	return 0;

}