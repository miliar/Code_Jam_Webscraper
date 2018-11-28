#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
double dotp(double *a, double *b) {
                double ans=0;
                REP(i,3) ans+=a[i]*b[i];
                return ans;
}
double val(double *s) {return sqrt(dotp(s,s));}
double crossp(double *a, double *b) {
                double c[3];
                REP(i,3) c[i]=a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3];
                return val(c);
}
void go(double *s, double *v) {
                double dis=crossp(s,v)/val(v);
                double tm=sqrt(val(s)*val(s)-dis*dis)/val(v);
                printf("%.7lf %.7lf\n", dis, tm);
}
int main()
{
                freopen("B-large (2).in","r",stdin);
                freopen("B.out","w", stdout);
                int tc, n;
                double s[3], v[3], t;
                scanf("%d", &tc);
                for (int cs=1; cs<=tc; ++cs) {
                                REP(i,3) s[i]=v[i]=0;
                                scanf("%d", &n);
                                REP(j,n) {
                                                REP(i,3) scanf("%lf", &t), s[i]+=t;
                                                REP(i,3) scanf("%lf", &t), v[i]+=t;
                                }
                                REP(i,3) s[i]/=n, v[i]/=n;
                                printf("Case #%d: ", cs);
                                if (dotp(s,v)>=0) printf("%.7lf 0.0000000\n", val(s));
                                else go(s,v);
                }
}
