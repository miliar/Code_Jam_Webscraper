#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

#define abs(a) ((a>0)?(a):(-(a)))

int main() {
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int ok,n,l,h,i,j,t;
	int a[10010];
	scanf("%d", &t);
	For(test, 1, t)
    {
              cin>>n>>l>>h;
              For(i,0,n-1)cin>>a[i];
              For(i,l,h)
              {
                        ok = 1;
                        For(j,0,n-1)
                        if(i%a[j]!=0 && a[j]%i!=0)
                        {
                                     ok = 0;
                                     break;
                        }
                        if(ok)
                        {
                              printf("Case #%d: %d\n", test, i);
                              break;
                        }
              }
              if(ok) continue;
              printf("Case #%d: NO\n", test);
	}

	exit(0);
}
