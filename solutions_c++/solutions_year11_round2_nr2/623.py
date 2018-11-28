#include <cstdio>
#include <cmath>
#include <algorithm>
#include <map>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <bitset>
#include <cstdlib>
using namespace std;

#define FI(x) (x).first
#define SE(x) (x).second
#define rep(i,a,b) for(int i=(a); i<(b); ++i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin();it!=(v).end(); ++it)

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef double fl;

vector<pii> data;
int C,D;

void solve(int tc)
{
	cout << "Case #" << tc << ": ";
	cin >> C >> D;
	data.resize(C);
	rep(i,0,C)
		cin >> FI(data[i]) >> SE(data[i]);
	sort(data.begin(), data.end());
	fl best=0;

	/*cout << "C = " << C << ", D = " << D << endl;
	rep(i,0,C)
		cout << FI(data[i]) << ", " << SE(data[i]) << endl;
*/
	int LL = FI(data[0]);
	rep(i,0,C)
	{
		fl tmp =  D*(SE(data[i])-1)*0.5;
		if(LL>FI(data[i]))
			tmp += (LL-FI(data[i]))*0.5;
		else
			LL = FI(data[i]);
		best = max(best, tmp);
		LL +=  D * (SE(data[i]));
	}

	cout << best << endl;
}

int main() {

	int T;
	cin >> T;
	rep(i,1,T+1)
		solve(i);

  return 0;
}
