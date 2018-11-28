#include<stdio.h>
#include<memory.h>
#include <cmath>
const double PI = acos(-1.0);
const int MAXINT = 0x7FFFFFFF;
typedef long long int64;
const int64 MAXINT64 = 0x7FFFFFFFFFFFFFFFLL;

#define PS(x) (cout<<#x<<": "<<endl)
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define MST(t,v) memset(t,v,sizeof(t))
#define SHOW1(a,n) (PS(a),_show1(a,n))
#define SHOW2(a,r,c) (PS(a),_show2(a,r,c))

template<class T>void _show1(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void _show2(T a, int r, int l){for(int i=0; i<r; ++i)_show1(a[i],l);cout<<endl;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;} 
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}

int W, H, R, F[128][128], a, b;
bool G[128][128];
bool Calc(int &ta, int &tb, int h, int w)
{
    ta = (2 * w - h - 1);
    tb = (2 * h - w - 1);
    if(ta % 3 || tb % 3) return 0;
    ta /= 3;
    tb /= 3;
    return 1;
}
int Solve()
{
    int A, B, i, j;
    if(!Calc(A, B, H, W)) return 0;
   
    if(G[0][0]) return 0;
    for(i = 0; i <= B; ++i)
        for(j = 0; j <= A; ++j)
            if(i || j)
            {
                if(G[i][j] == 0)
                {
                    if(i) F[i][j] += F[i - 1][j];
                    if(j) F[i][j] += F[i][j - 1];
                    F[i][j] %= 10007;
                }
                else F[i][j] = 0;
            }
    return F[B][A];
            
}
int main()
{
    int T;
	int t1, t2, r, c;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
   for (int ctr = 1; ctr <= T; ctr++)
    {
        scanf("%d%d%d", &H, &W, &R);
        memset(F, 0, sizeof(F));
		 memset(G, 0, sizeof(G));
        
		 F[0][0] = 1;
       
        while(R--)
        {
            scanf("%d%d", &r, &c);
            if(Calc(t1, t2, r, c))
                G[t2][t1] = 1;
        }
        printf("Case #%d: %d\n", ctr, Solve());
    }
}
