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
	
	int t,i,j,no,m,n;
	char a[55][55];

	scanf("%d", &t);
	For(test, 1, t)
    {
        no = 0;
        cin>>m>>n;
        For(i, 0, m-1)
        For(j, 0, n-1)
        {
               cin>>a[i][j];
        }
        
        For(i, 0, m-1)
        {
               if(no)break;
               For(j, 0, n-1)
               {
                if(a[i][j] == '#')
                {
                          if(i == m-1 || j == n-1)
                          {
                               no = 1;
                               break;
                          }
                          if(a[i+1][j] == '#' && a[i][j+1] == '#' && a[i+1][j+1] == '#')
                          {
                                       a[i][j]='/';
                                       a[i][j+1]='\\';
                                       a[i+1][j]='\\';
                                       a[i+1][j+1] = '/';
                          }
                          else
                          {
                              no = 1;
                              break;
                          }
                }
               }
        }
                                          
		printf("Case #%d:\n", test);
		if(no) printf("Impossible\n");
		else
		{
            For(i, 0, m-1)
            {
                   For(j, 0, n-1)printf("%c",a[i][j]);
                   printf("\n");
            }
        }
	}

	exit(0);
}
