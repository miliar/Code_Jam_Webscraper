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

struct blah	{
	int t1;
	int t2;
	int vi;
};

bool operator<(const blah &a, const blah &b)	{
	if (a.vi == b.vi)	{
		if (a.t1 == b.t1)	{
			return a.t2 - b.t2;
		}
		return a.t1 - b.t1;
	}
	return a.vi - b.vi;
}

vector<int> in;
vector<long> visum;
long tn;
map< blah, long> table;
long iter;
vector<long> vitable;
// bool startfresh = true;

long awsome(long sp, long other, int vi, long t1, long t2, bool startfresh)	{
	
// 	cout << "vi " << vi << " sp " << sp << endl;
	
	if (vi == in.size())	{
		if (t1 == t2 && other != 0 && sp != 0)
			return max(sp, other);
		return 0;
	}
	
	if (t1 == t2 && !startfresh)	{
		
		if (vitable[vi] != -1)
			return vitable[vi];

		vitable[vi] = awsome(0, 0, vi, 0, 0, true);
		if (other != 0)
			vitable[vi] = vitable[vi] == 0 ? sp : vitable[vi];
		return vitable[vi];
	}
	
	long res = max(awsome(sp + in[vi], other, vi+1, t1 ^ in[vi], t2, false), awsome(sp, other + in[vi], vi+1, t1, t2 ^ in[vi], false));
	
	return res;
}

long dp(long sp, int vi, long t1, long t2)	{
	
	long mv = 0;
	
	if (vi == in.size())	{
		if (t1 == t2)
			mv = sp;
		return sp == tn ? 0 : mv;
	}
	
	mv = max(mv, dp(sp + in[vi], vi+1, t1 ^ in[vi], t2));
	mv = max(mv, dp(sp, vi+1, t1, t2 ^ in[vi]));
	
	return sp == tn ? 0 : mv;
}

void solve(int z)	{
	
	iter = 0;
// 	long res = awsome(0,0,0,0,0, false);
	long res = dp(0,0,0,0);
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
		visum.clear();
		vitable.clear();
		
		int n;
		cin >> n;
		forp(0,n,i)	{
			int a;
			cin >> a;
			in.pb(a);
			tn += a;
			visum.pb(tn);
			vitable.pb(-1);
		}
		
		solve(z + 1);
	}
}