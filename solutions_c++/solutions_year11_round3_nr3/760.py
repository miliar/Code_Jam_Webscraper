#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
 
using namespace std;

#define sz(a) (LL)a.size()
#define all(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair<int, int> pii;
#define LL long long
#define INF 1000000

int N, L, H;
int A[200];

bool okay(int num)
{
    int i;
    for (i=0; i<N; i++)
        if (A[i]%num!=0 && num%A[i]!=0) return false;
    return true;
}

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("C-small-attempt1.out", "w", stdout);

	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);

	int numtest, test, i, j;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        cin >> N >> L >> H;
        for (i=0; i<N; i++) cin >> A[i];

        bool ok = false;
        for (i=L; i<=H; i++) if (okay(i)) { ok=true; break; }

        if (ok) cout << "Case #" << (test) << ": " << i << endl;
        else cout << "Case #" << (test) << ": NO" << endl;
	}
	return 0;
}
