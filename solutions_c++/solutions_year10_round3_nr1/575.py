#include<ctime>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<cstring>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;

bool inside(double a,double b,double x)
{
    if(a>b) swap(a,b);
    if(a<x+TOLL && x<b+TOLL) return true;
    return false;
}

bool ok(double fx1,double fy1, double fx2,double fy2, double sx1,double sy1, double sx2,double sy2)
{
    //A = y2-y1
    //B = x1-x2
    //C = A*x1+B*y1
    double fA= fy2-fy1;
    double fB= fx1-fx2;
    double fC= fA*fx1+fB*fy1;

    double sA= sy2-sy1;
    double sB= sx1-sx2;
    double sC= sA*sx1+sB*sy1;

    double det = fA*sB - sA*fB;
    if(fabs(det) < TOLL)
    {
        return false;
    }
    else
    {
        double x = (sB*fC - fB*sC)/det;
        double y = (fA*sC - sA*fC)/det;
        if(inside(fx1,fx2,x) && inside(sx1,sx2,x) && inside(fy1,fy2,y) && inside(sy1,sy2,y)) return true;
        return false;
    }
    return false;


}
int A[1010], B[1010];

int main()
{
    int t; cin>>t; int cn=0;
    while(t--)
    {
        cn++;
        int n; cin>>n;
        for(int i=0;i<n;i++) cin>>A[i]>>B[i];
        int rv=0;
        for(int i=0;i<n;i++)
        for(int j=i+1;j<n;j++)
        {
            if(ok(0,A[i],1000,B[i],0,A[j],1000,B[j])) rv++;
        }
        printf("Case #%d: %d\n",cn,rv);
    }
    return 0;
}
