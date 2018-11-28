#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <sstream>
#include <memory>
#include <complex>
using namespace std;

static const double EPS = 1e-5;
typedef long long ll;

#define FOR(i,a,b)	for(int i=(a);i<(int)(b);++i)
#define REP(i,b)	FOR(i,0,b)
#define ALL(c)		(c).begin(),(c).end()
#define LET(v,x)	typeof(x) v = x
#define FOREACH(it,c)	for(LET(it,(c).begin());it!=(c).end();++it)

char buf[105];

struct comp_t{
	bool operator()(const char& a, const std::pair<const char, char>& b){
		return a == b.second;
	}
};

int main(){
	int T;
	scanf("%d ", &T);
	REP(i, T){
		int C;
		scanf("%d ", &C);
		std::map<std::pair<char, char>, char> trans;
		REP(c, C){
			scanf("%s ", buf);
			trans.insert(std::make_pair(std::make_pair(buf[0], buf[1]), buf[2]));
			trans.insert(std::make_pair(std::make_pair(buf[1], buf[0]), buf[2]));
		}
		int D;
		scanf("%d ", &D);
		std::multimap<char, char> clears;
		REP(d, D){
			scanf("%s ", buf);
			clears.insert(std::make_pair(buf[0], buf[1]));
			clears.insert(std::make_pair(buf[1], buf[0]));
		}
		int N;
		scanf("%d %s ", &N, buf);
		std::vector<char> elems;
		REP(p, N){
			char c = buf[p];
			if(elems.empty()){
				elems.push_back(c);
				continue;
			}
			char prev = elems.back();
			LET(t_it, trans.find(std::make_pair(prev, c)));
			if(t_it != trans.end()){
				elems.pop_back();
				elems.push_back(t_it->second);
				continue;
			}
			LET(its, clears.equal_range(c));
			LET(find, std::find_first_of(elems.begin(), elems.end(), its.first, its.second, comp_t()));
			if(find != elems.end()) elems.clear(); else elems.push_back(c);
		}
		const char *comma = "";
		printf("Case #%d: [", i + 1);
		FOREACH(it, elems) printf("%s%c", comma, *it), comma = ", ";
		printf("]\n");
	}
	return 0;
}
