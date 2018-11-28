
#include<algorithm>
#include<bitset>
#include<iostream>
#include<string>
#include<cstdio>
#include<sstream>
#include<vector>
#include<stack>
#include<deque>
#include<map>
#include<iterator>
#include<cmath>
#include<complex>
#include<queue>
#include<cassert>
#include<set>
#include<cstring>
#include<list>
#include<numeric>
#include<cassert>

#define FOREACH(it ,c ) for( typeof((c).begin()) it= (c).begin();it!=(c).end();++it) 
#define debug(x) cerr<< #x << " = " << x << "\n";
#define debugv(x) cerr<< #x << " = " ; FOREACH(it,(x)) cerr << *it << "," ; cerr<< "\n" ;
#define MP make_pair
#define PB push_back
#define siz(w) (int)w.size()
#define fup(i,st,ko) for(int i=st;i<=ko;i++)
#define fdo(i,st,ko) for(int i=st;i>=ko;i--)
#define REP(i,w) for(int i=0;i<siz(w);i++)
#define inf 100000000

using namespace std;

typedef long long ll;


bool good(vector<int> &l, vector<int> &r)
{
	bool less = 0;
	if(l[0] < r[0]) less = 1;
	else if(l[0] == r[0]) return 0;
	else less = 0;
	
	REP(i, l)
	{
		if(less and l[i] >= r[i]) return 0;
		if(!less and l[i] <= r[i]) return 0;
	}
	return 1;
}

int best[1 << 20];
bool can_be[104][104];
vector<int> what[104];
bool is_good[1 << 20];

bool all_good(int x, int n)
{
	fup(i, 0, n - 1) fup(j, i + 1, n - 1)
	{
		if((x & (1 << i)) and (x & (1 << j)))
			if(!can_be[i][j]) return false;
	}
	return true;
}

int main()
{
	int cas;
	cin >> cas;
	fup(xx, 1, cas)
	{
		memset(can_be, 0, sizeof(can_be));

		int n,k;
		cin >> n >> k;
		fup(i, 0, n - 1)
		{
			vector<int> tt;
			fup(j, 1, k)
			{
				int x;
				cin >> x;
				tt.push_back(x);
			}
			what[i] = tt;
		}

		fup(i, 0, n - 1) fup(j, i + 1, n - 1)
		{
			if(good(what[i], what[j]))
			{
				can_be[i][j] = can_be[j][i] = 1;
			}
		}
		
		fup(i, 0, (1 << n) - 1)
			is_good[i] = all_good(i, n);
		
		memset(best, 32, sizeof(best));
		best[0] = 0;
		fup(i, 0, n - 1) best[1 << i] = 1;

		fup(i, 1, (1 << n) - 1)
		{
			int have = i;
			int nowy = have;
			while(nowy > 0)
			{
				if(is_good[nowy])
				{
			//		cout << have << " " << nowy << "dfsd" << endl;
					best[have] = min(best[have], best[have - nowy] + 1);
				}
				nowy = nowy - 1;
				nowy &= have;
			}
		//	cout << have << " " << best[have] << endl;
		}
		cerr << xx << endl;
		cout << "Case #" << xx << ": " << best[(1 << n) - 1] << endl;
	}

	return 0;
}



