#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;


int main(void)	{
	int C, N;
	cin >> C;
	FOR (nc, 1, C+1)	{
		cin >> N;
		string s;
		vector<int> v;

		//cout << "Input " << nc << endl;
		FOR (i, 0, N)	{
			cin >> s;
			//cout << s << endl;
			for (int j = s.SZ - 1; j >= 0; j--)	if (s[j] == '1')	{	v.PB(j);	break;	}
			if (v.SZ != i+1)	v.PB(0);
		}

		//cout << "Read input " << endl; 
		int ans = 0;
		FOR (i, 0, N)	{
			//FOR (j, 0, N)	{	cout << v[j] << endl;	}
			//cout << "--" << endl;
			FOR (j, i, N)	if (v[j] <= i)	{	//move j to i'th spot	
				int tmp = v[j];
				for (int k = j; k >= i+1; k--)	{
					v[k] = v[k-1];
					ans++;
				}
				v[i] = tmp;
				break;
			}
		}
		
		cout << "Case #" << nc << ": " << ans << endl;
	}
	
	
}
