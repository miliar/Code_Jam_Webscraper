#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cmath>

#define forp(a,b,i) for (int i = a; i < b; i++)
#define pb push_back
#define mp make_pair

using namespace std;

vector<int> in;
long tn;
map< pair<long,int>, long> table;

long dp(long sp, int vi, long t1, long t2)	{
	
// 	cout << "sp " << sp << " vi " << vi << " " << t1 << " " << t2 << endl;
	long mv = 0;
	if (table.find(mp(sp,vi)) != table.end())	{
		return table[mp(sp,vi)];
	}
	
	if (vi == in.size())	{
		if (t1 == t2)
			mv = sp;
		table[mp(sp,vi)] = (sp == tn ? 0 : mv);
		return sp == tn ? 0 : mv;
	}
	
	mv = max(mv, dp(sp + in[vi], vi+1, t1 ^ in[vi], t2));
	mv = max(mv, dp(sp, vi+1, t1, t2 ^ in[vi]));
	
	table[mp(sp,vi)] = (sp == tn ? 0 : mv);
	return sp == tn ? 0 : mv;
}

void solve(int z)	{
	
	long res = dp(0, 0, 0, 0);
	cout << "Case #" << z << ": ";
	if (res == 0)	cout << "NO" << endl;
	else	cout << res << endl;
}

int main()	{

	int t;
	cin >> t;
	forp(0,t,z)	{
	
		in.clear();
		tn = 0;
		table.clear();
		
		int n;
		cin >> n;
		forp(0,n,i)	{
			int a;
			cin >> a;
			in.pb(a);
			tn += a;
		}
		
		solve(z + 1);
	}
}