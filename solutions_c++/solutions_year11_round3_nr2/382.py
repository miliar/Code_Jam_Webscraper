#include<fstream>
#include<cstdio>
#include<algorithm>
#include<vector>
typedef long long LL;
#define SBL_VAR(a) _SBL_VAR(a,__LINE__)
#define _SBL_VAR(a,b) __SBL_VAR(a,b)
#define __SBL_VAR(s,B) _sBl ## s ## B ## l
#define auto(i,a) __typeof(a)i(a)
#define REP(i,n) for(auto(SBL_VAR(end), (n)), i(0);i < SBL_VAR(end); ++i)
#define ALL(A) (A).begin(),(A).end()
#define SBL_FOREACH_REVERSE_1(c) \
	if(bool SBL_VAR(d) = false) {} else \
		for(auto(SBL_VAR(i), (c).end()); \
		!SBL_VAR(d) && SBL_VAR(i)-- != (c).begin(); ) 
#define SBL_FOREACH_1(c) \
	if(bool SBL_VAR(d) = false) {} else \
		for(auto(SBL_VAR(i), (c).begin()); \
		!SBL_VAR(d) && SBL_VAR(i) != (c).end(); \
		++SBL_VAR(i) )
#define SBL_FOREACH(v) \
	if(!(SBL_VAR(d) = true)) {} else \
		for(v = *SBL_VAR(i); SBL_VAR(d); SBL_VAR(d) = false)
#define SBL_FOREACH_AUTO(v) \
	if(!(SBL_VAR(d) = true)) {} else \
		for(auto(v, *SBL_VAR(i)); SBL_VAR(d); SBL_VAR(d) = false)
#define foreach(v,c) SBL_FOREACH_1(c) SBL_FOREACH(v)
#define foreach_auto(v,c) SBL_FOREACH_1(c) SBL_FOREACH_AUTO(v)
#define rforeach(v,c) SBL_FOREACH_REVERSE_1(c) SBL_FOREACH(v)
#define rforeach_auto(v,c) SBL_FOREACH_REVERSE_1(c) SBL_FOREACH_AUTO(v)
using namespace std;
ifstream fin("B-large.in");
ofstream fout("output.txt");
LL work()
{
	LL l, t, n, c;
	fin >> l >> t >> n >> c;
	vector<LL> a(c), d(n);
	for(LL i = 0; i < c; i++)
		fin >> a[i];
	for(LL i = 0; i < n; i++)
		d[i] = a[i % c] * 2;
	a.swap(d);
	bool b = 0;
	LL s = 0;
	for(LL i = 0; i < n; i++) {
		s += a[i];
		if(s >= t) {
			b = 1;
			a[i] = s - t;
			a.erase(a.begin(), a.begin() + i);
			break;
		}
	}
	if(!b)
		return s;
	if(a.size() <= size_t (l)) {
		for(size_t i = 0; i < a.size(); i++)
			a[i] /= 2;
	} else {
		sort(a.begin(), a.end());
		auto(i, a.rbegin());
		REP(j, l) {
			*i /= 2;
			i++;
		}
	}
	for(size_t i = 0; i < a.size(); i++)
		t += a[i];
	return t;
}
int main()
{
	LL T;
	fin >> T;
	for(LL i = 1; i <= T; i++)
		fout << "Case #" << i << ": " << work() << endl;
}
