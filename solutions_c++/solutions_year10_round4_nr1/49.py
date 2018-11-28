#include <vector>
#include <cstring>
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
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define F(i,n) for (int i=0;i<n;i++)
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)
#define F(i,n) for (int i=0;i<n;i++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

int T;


int K;
int a[300][300];
int b[300][300];

const int mid = 150;

int main()
{
    scanf("%d",&T);
    F(xx,T)
     {
        scanf("%d", &K);
        int sz = 0;
        memset(a, -1, sizeof(a));
        int row = - K + 1;
        F(i, 2*K - 1)
        {
            if (i < K) sz++;
            else sz--;
            F(j, sz)
            {
                int digit;
                scanf("%d", &digit);
                a[mid - K + 1 + i][mid - sz + 1 + j * 2] = digit;
            }
        }
        
        /*
        for (int i = mid - K + 1; i <= mid + K - 1; i++)
        {
            for (int j = mid - K + 1; j <= mid + K - 1; j++)
            {
                cout<<a[i][j];
                int cx = i;
                int cy = j;
                
            }
            cout<<"\n";
        }
        cout<<"\n";*/
       // memcpy(b, a, sizeof(a));

        int answer = 1000000000;
        for (int ci = mid - K + 1 - 5; ci <= mid + K - 1 + 5; ci++)
        {
            for (int cj = mid - K + 1 - 5; cj <= mid + K - 1 + 5; cj++)
            {
                bool can = true;
                int nK = K + abs(mid - ci) + abs(mid - cj);
                //memcpy(a, b, sizeof(a));
              //  cout<<" try "<<ci-mid<<" "<<cj-mid<<" : "<<nK<<"\n";
                for (int i = mid - K + 1; i <= mid + K - 1; i++)
                {
                    for (int j = mid - K + 1; j <= mid + K - 1; j++)
                     if (a[i][j] > -1)
                     {
                        int ni = ci + (ci - i);
                        int nj = cj + (cj - j);
                  //      cout<<"     "<<i-mid<<" "<<j-mid<<" to "<<ni-mid<<" "<<nj-mid<<"\n";
                        if (a[ni][nj] > -1 && a[ni][nj] != a[i][j])
                         {
                                    can = false;
                                    break;
                         }
                        if (a[i][nj] > -1 && a[i][nj] != a[i][j])
                         {
                                    can = false;
                                    break;
                         }
                        if (a[ni][j] > -1 && a[ni][j] != a[i][j])
                         {
                                    can = false;
                                    break;
                         }
                       // a[ni][nj] = a[ni][j] = a[i][nj] = a[i][j];
                     }
                    if (!can) break;
                }
                if (can)
                {
                    answer = min(answer, nK * nK - K * K);
                }
            }
        }
        
        cout<<"Case #"<<xx+1<<": "<<answer<<"\n";
     }
    return 0;
}
