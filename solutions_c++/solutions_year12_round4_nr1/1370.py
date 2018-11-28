#include <iostream>
#include <algorithm>
#include <limits>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <cmath>
#include <stack>
using namespace std;

#define forl(i, s, t) for(__typeof(s) i = s; i != t; i++)
#define rforl(i, s, t) for(__typeof(s) i = s; i != t; i--)
#define foreach(itr, c) forl(itr, (c).begin(), (c).end())
#define rforeach(itr, c) forl(itr, (c).rbegin(), (c).rend())

template<typename T> inline void step(T& i, T& t) { if(i < t) i++; else i--;}
template<typename T> inline int towards(T i, T t) { if(i < t) return ++i; else if(i > t) return --i; else return i;}
template<typename T> inline int away(T i, T t) { if(i < t) return --i; else if(i > t) return ++i; else return i;}
#define sforl(i, s, t) for(__typeof(s) i = s; i != t; step(i,t))

#define varcontent(v) #v << '=' << v
#define debug(v) cerr << varcontent(v) << endl
#define pdebug(v, w) cerr << '(' << varcontent(v) << ',' << varcontent(w) << ')' << endl

#define gcase int T; cin >> T; for(int gtest = 1; gtest <= T; gtest++)
#define gstate() cerr << "Case: " << gtest << '/' << T << endl
#define gout cout << "Case #" << gtest << ": "

int gcd(int a, int b) { if(b == 0) return a; return gcd(b, a % b); }

const int INF = numeric_limits<int>::max()/2;
const double EPS = INF*numeric_limits<double>::epsilon();

bool swing(vector<pair<int,int> >& vine, int D) {
	int pos = 0;
	bool reach = false;
	stack<pair<int,int> > s;
	s.push(pair<int,int>(pos++, 0));
	while(!s.empty()) {
		pair<int,int> i = s.top(); s.pop();
		int cur = i.first, dist = i.second;
		reach = vine[cur].first + min(vine[cur].first-dist, vine[cur].second) >= D;
		if(reach) break;
		int pos = cur+1;
		while(pos < vine.size() && vine[pos].first <= vine[cur].first + min(vine[cur].first-dist, vine[cur].second)) {
			//cerr << pos << ' ' << cur << vine[cur].first + min(vine[cur].first-dist, vine[cur].second) << endl;
			s.push(pair<int,int>(pos++, vine[cur].first));
		}
	}
	return reach;
}

/*bool swing2(vector<pair<int,int> >& vine, int D, int i, int j) {
	if(vine[i].first + min(vine[j].second, vine[j].first-vine[i].first) >= D) return true;
	
	
}*/

int main() {
	gcase {
		gstate();
		int N;
		cin >> N;
		vector<pair<int,int> > vine(N);
		forl(n, 0, N) cin >> vine[n].first >> vine[n].second;
		int D;
		cin >> D;
		//sort(vine.begin(), vine.end());
		
		bool can = swing(vine, D);
		
		if(can) gout << "YES" << endl;
		else gout << "NO" << endl;
	}
}
