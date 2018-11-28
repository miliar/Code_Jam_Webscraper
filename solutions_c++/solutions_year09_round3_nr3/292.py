#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <deque>
#include <map>
#include <stack>
#include <sstream>

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((x).size())
#define sqr(x) ((x)*(x))
#define slen(x) ((x).length())

template<class T> T abs(T x) { return x > 0 ? x : -x;}

int n, m;

int escape(int p, vi order)
{
	bool here[200];
	int i, j;
	int result = 0;
	
	for (i = 0; i < p; i++)
		here[i] = true;
		
	for (i = 0; i < order.size(); i++)
	{
		here[order[i]] = false;
		j = order[i] - 1;
		while (j >= 0 && here[j])
		{
			result++;
			j--;
		}
		j = order[i] + 1;
		while (j < p && here[j])
		{
			result++;
			j++;
		}
	}
	return result;
}

int main()
{
	int i, j, p, q, tmp;
	vi pris;
	
//	freopen("input", "r", stdin);
//	freopen("output", "w", stdout);
	cin >> n;
	for (i = 0; i < n; i++)
	{
		cin >> p >> q;
		pris.clear();
		for (j = 0; j < q; j++)
		{
			cin >> tmp;
			pris.pb(tmp - 1);
		}

		int answer = 1000000;
		do
		{
			answer = min(escape(p, pris), answer);			
		} while (next_permutation(pris.begin(), pris.end()));
		cout << "Case #" << i + 1 << ": " << answer << endl;
	}
	
	return 0;
}
