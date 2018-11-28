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

int L, N, C;
LL solving[1000005];
LL ans, sum;
LL t;
LL A[1000005];

void solve0()
{
    int i;
    ans = sum;
    cout << ans << endl;
}

void calc_solveing()
{
    int s1, i;
    for (s1=0; s1<N; s1++)
    {
        LL res = 0;
        LL saving = 0;

        solving[s1] = 0;

        for (i=0; i<=s1; i++) res += A[i]*2;
        if (res <= t) continue;

        res -= A[s1]*2;
        if (res >= t) saving = A[s1];
        else
        {
            saving = (t - res) + (A[s1] - (t-res)/2);
            saving = A[s1]*2 - saving;
        }

        solving[s1] = saving;
    }
}

void solve1()
{
    calc_solveing();

    int s1;
    ans = sum;
    for (s1=0; s1<N; s1++)
    {
        if (ans > sum - solving[s1]) ans = sum - solving[s1];
    }
    cout << ans << endl;
}

void solve2()
{
    calc_solveing();

    int i, j, s1, s2;
    ans = sum;

    for (s1=0; s1<N; s1++)
    {
        if (ans > sum - solving[s1]) ans = sum - solving[s1];
    }

    for (s1=0; s1<N; s1++)
    for (s2=s1+1; s2<N; s2++)
    {
        if (ans > sum - solving[s1] - solving[s2]) ans = sum - solving[s1] - solving[s2];
    }
    cout << ans << endl;
}

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);

    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);

	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);

	int numtest, test, i, j;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        cin >> L >> t >> N >> C;

        for (i=0; i<C; i++) cin >> A[i];
        for (i=C; i<N; i++) A[i] = A[i%C];

        sum = 0;
        for (i=0; i<N; i++) sum += A[i]*2;

        cout << "Case #" << (test) << ": ";

        if (L==0) solve0();
        else if (L==1) solve1();
        else if (L==2) solve2();
        else 
        {
            cout << "I'M STUPID" << endl;
        }
	}
	return 0;
}
