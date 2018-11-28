#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>

// For each i from 0 to n
#define fe(i, n) for(int i = 0; i < n; i++)
// For each i from n to 0 inclusive
#define fd(i, n) for(int i = n; i >= 0; i--)
// Size as an integer
#define sz(n) (int)(n).size()
// For each i from 0 to size of n exclusive
#define fs(i, n) for(int i = 0; i < sz(n); i++)
// Traverse a STL container
#define tr(i, n) for((typeof((n).begin())) i = (n).begin(); i != (n).end(); i++)

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<vi> vvi;
typedef vector<ii> vii;

int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");
	
	string t;
	int Cases;
	getline(fin, t);
	istringstream ISS0(t);
	ISS0 >> Cases;
	fe(k, Cases)
	{
		fout << "Case #" << k+1 << ": ";
		int res = 0;
		int N, Q;
		getline(fin, t);
		istringstream ISS1(t);
		ISS1 >> N;
		map<string, int> M;
		fe(i, N)
		{
			getline(fin, t);
			M.insert(make_pair(t, i));
		}
		getline(fin, t);
		istringstream ISS2(t);
		ISS2 >> Q;
		vector<bool> S(N, true);
		fe(i, Q)
		{
			getline(fin, t);
			if (!M.count(t))
				continue;
			if (S[M[t]])
			{
				S[M[t]] = false;
				int reset = true;
				fs(j, S)
					if (S[j])
					{
						reset = false;
						break;
					}
				if (reset)
				{
					S = vector<bool>(N, true);
					res++;
					S[M[t]] = false;
				}
			}
		}
		fout << res << endl;
	}
	
	return 0;
}
