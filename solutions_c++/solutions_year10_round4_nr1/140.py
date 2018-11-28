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
#define INF 987654321

const int MAX = 300;
int ans;
int k;
int a__[MAX][MAX];
int a[MAX][MAX];

bool process(int x, int y, int N)
{
    int i, j, h, v;
    for (i=0; i<k; i++)
        for (j=0; j<k; j++)
        {
            h = y+j;
            v = x+i;
            if (h>=x && h<x+k && v>=y && v<y+k) if (a[i][j]!=a[h-x][v-y])
                return false;

            h = N-1-(y+j);
            int gap = h-(x+i);
            v = (y+j)+gap;
            if (h>=x && h<x+k && v>=y && v<y+k) if (a[i][j]!=a[h-x][v-y])
                return false;
        }
    return true;
}

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0a.out", "w", stdout);

    //freopen("A-small-attempt1.in", "r", stdin);
    //freopen("A-small-attempt1b.out", "w", stdout);

    //freopen("A-small-attempt2.in", "r", stdin);
    //freopen("A-small-attempt2.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int numtest, test, i, j, top;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        ans = INF;

        cin >> k;
        for (i=0; i<k*2-1; i++)
        {
            if (i<k) top=i+1; else top=k*2-1-i;
            for (j=0; j<top; j++) cin >> a__[i][j];
        }

        for (i=0; i<k; i++)
            for (j=0; j<k; j++)
            {
                a[i][j] = a__[i+j][min(j, k-1-i)];
            }
        
            process(1, 0, 4);
        int size = k;
        while (true)
        {
            bool ok = false;
            for (i=0; i<=size-k; i++)
            {
                for (j=0; j<=size-k; j++)
                    if (process(i, j, size))
                    {
                        ok=true;
                        break;
                    }
                if (ok) break;
            }
            if (ok) break;
            size++;
        }
   
        ans = size*size - k*k;
        cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}
