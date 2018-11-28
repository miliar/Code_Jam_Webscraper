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

int C, ans;
map<int, int> mm;

void process()
{
    ans = 0;
    int i;
    while (true)
    {
        bool stop = true;
        map<int, int> mm2 = mm;
        for (map<int,int>::iterator it=mm2.begin(); it!=mm2.end(); it++)
        {
            int P = (*it).first;
            int V = (*it).second;
            if (V>1)
            {
                mm[P+1]++;
                mm[P-1]++;
                mm[P]-=2;
                stop=false;
                ans++;
            }
        }
        if (stop) break;
    }
}

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
	
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("C-small-attempt1.out", "w", stdout);

	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);

	int numtest, test;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        mm.clear();
        int i, P, V;
        cin >> C;
        for (i=0; i<C; i++)
        {
            cin >> P >> V;
            mm[P] = V;
        }
        process();

		cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}
