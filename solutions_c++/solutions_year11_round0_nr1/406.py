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
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t,test,a,b,n,i, op=1, bp=1, opt=0, bpt=0, time;
	char c,d;
	int ans = 0;
	scanf("%d", &t);
	For(test, 1, t)
    {
        cin>>n;
       // printf("%d\n", n);
        ans = 0;
        op=1, bp=1, opt=0, bpt=0;
        for(i=0; i<n; i++)
        {
               cin>>c>>a;
               //printf("%c %d\n", c, a);
               //if(i!=0 && c == d)ans++;
               if(c=='O')
               {
                         if(opt + abs(a-op) > ans) ans = opt + abs(a-op);
                         ans++;
                         op=a;
                         opt=ans;
               }
               if(c=='B')
               {
                         if(bpt + abs(a-bp) > ans) ans = bpt + abs(a-bp);
                         ans++;
                         bp=a;
                         bpt=ans;
               }
               d =c;
              // printf("Case #%d: %d %c\n", test, ans, c);
        }
               
		printf("Case #%d: %d\n", test, ans);
	}

	exit(0);
}
