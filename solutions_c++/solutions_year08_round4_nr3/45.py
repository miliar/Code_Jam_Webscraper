#include	<cstdio>
#include	<cstdlib>
#include	<cstring>
#include	<string>
#include	<vector>
#include	<cmath>
#include	<algorithm>
#include	<cassert>
#include	<set>
#include	<map>
#include	<queue>
#include	<iostream>
#include <fstream>
using namespace std;
#define pb push_back
#define REP(i,n) for(int i=0;i<(n);i++ ) 

typedef long long LL;
typedef pair<int,int> piii;

int N;
int X[1010],Y[1010],Z[1010],P[1010];
const double eps=1e-7;
int gao(double k)
{
        double t[8],p[8];
        //cout<<k<<endl;
        REP(i,N)
        {       
                double K=P[i]*k;
                p[0]=+X[i]+Y[i]+Z[i]+K;
                p[1]=+X[i]+Y[i]+Z[i]-K;
                p[2]=-X[i]+Y[i]+Z[i]+K;
                p[3]=-X[i]+Y[i]+Z[i]-K;
                p[4]=-X[i]-Y[i]+Z[i]+K;
                p[5]=-X[i]-Y[i]+Z[i]-K;
                p[6]=+X[i]-Y[i]+Z[i]+K;
                p[7]=+X[i]-Y[i]+Z[i]-K;
                if (i)
                {
                        REP(j,8)
                                if (j&1)
                                        t[j]=max(t[j],p[j]);
                                else
                                        t[j]=min(t[j],p[j]);
                }
                else
                {
                        REP(j,8)
                                t[j]=p[j];
                }
                //REP(j,8)
                //        cout<<t[j]<<' ';
                //cout<<endl;
        }
        return (t[0]>=t[1]-eps && t[2]>=t[3]-eps && t[4]>=t[5]-eps && t[6]>=t[7]-eps);
}

int main()
{
        int T;
        cin>>T;
        REP(cas,T)
        {
                cin>>N;
                REP(i,N)
                        cin>>X[i]>>Y[i]>>Z[i]>>P[i];
                double l=0,r=1e10;
                while (r-l>1e-7)
                {
                        double m=(l+r)/2;
                        if (gao(m))
                                r=m;
                        else
                                l=m;
                }
                printf("Case #%d: %.6lf\n",cas+1,l);
        }
        return 0;
}
