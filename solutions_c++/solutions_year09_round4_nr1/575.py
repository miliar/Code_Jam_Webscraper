
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

int main()
{
	int cas;
	cin >> cas;
	fup(xx, 1, cas)
	{
		vector<int> how;
		int n;
		cin >> n;
		fup(i, 1, n)
		{
			string s;
			cin >> s;
			int far = 0;
			REP(j, s)
			{
				if(s[j] == '1') far = j;
			}
			how.push_back(far);
		}
		int score = 0;
		fup(i, 0, n - 1)
		{
			REP(k, how)
			{
				if(how[k] <= i)
				{
					score += k;
					vector<int> nn;
					REP(jj, how)
					{
						if(jj != k) nn.push_back(how[jj]);
					}
					how = nn;
					break;
				}
			}
		}
		cout << "Case #" << xx << ": " << score << endl;
	}


	return 0;
}



