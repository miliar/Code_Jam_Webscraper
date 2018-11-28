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

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);

    //freopen("A-small-attempt1.out", "r", stdout);
    //freopen("A-small-attempt1.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int numtest, test;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        string ans = "OFF";
        int N, K;
        cin >> N >> K;
        if ((K+1) % (1<<N) == 0) ans = "ON";
		cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}
