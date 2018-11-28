#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <ctime>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <functional>
#include <iterator>
#include <utility>
#include <algorithm>
#include <numeric>
#include <complex>

using namespace std;

#define ALL(A) A.begin(), A.end()
#define EACH(it,A) for(typeof(A.begin()) t=A.begin();t!=A.end();t++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,a,b) for(i=(a);i<(b);i++)
#define SET(A,p) memset(A,p,sizeof(A))
#define CPY(A,B) memcpy(A,B,sizeof(A))

typedef vector<int> VI;
typedef vector<double> VD;
typedef long long ll;
typedef pair<int,int> ip;
typedef pair<ll,ll> llp;
#define probT ip
typedef vector<probT> VP;

#define sz size()
#define cl clear()
#define fi first
#define se second
#define pb push_back
#define ins insert

int R[1000001];

bool is_win(int A, int B)
{
	if(A>B) swap(A,B);
	if(A==0) return true;
	if(is_win(B%A,A))
		if(B >= 2*A) return true;
		else return false;
	return true;
}

ll calc(int A, int B)
{
	if(A>B) swap(A,B);
	ll res = 0;
	FOR(i,1,A+1) res += max(0,B-R[i]+1);
	FOR(i,1,B+1) res += max(0,A-R[i]+1);
	return res;
}

int main()
{
	int la=1;
	FOR(i,1,1000001) { while(!is_win(i,la)) la++; R[i]=la;}
	int T;
	cin >> T;
	FOR(te,0,T)
	{
		int A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;
		ll res = calc(A2,B2) - calc(A1-1,B2) - calc(A2,B1-1) + calc(A1-1,B1-1);
		cout << "Case #" << te+1 << ": " << res << endl;
	}
	return 0;
}
