#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <complex>
using namespace std;
typedef complex<double> point;
#define eps 1e-8
#define cross(a,b) ((conj(a)*(b)).imag())
#define dot(a,b) ((conj(a)*(b)).X)
#define normalize(v) ((v)/length(v))
#define X real()
#define Y imag()
#define vect(a,b) (b)-(a)
#define length(V) (hypot((V).X,(V).Y))
#define PI 3.1415926535897932384626433832795
int comp(double a,double b)
{
    if(fabs(a-b)<eps)
        return 0;
    return a>b?1:-1;
}
int main()
{
    freopen("B-small-attempt4.in","rt",stdin);
    freopen("b.txt","wt",stdout);
    int C;
    cin>>C;
    for(int nn=0;nn<C;nn++)
    {
        int A,N,M;
        cin>>N>>M>>A;
        int i,j,k,l;
        bool f=0;
        for(i=1;i<=N;i++)
        {
            for(j=0;j<=M;j++)
            {
                for(k=1;k<=M;k++)
                {
                    for(l=0;l<=N;l++)
                    {
                        point p1(0,0),p2(i,j),p3(l,k);
                        if((comp(p2.X,p3.X)==0 && comp(p2.Y,p3.Y)==0) || (comp(p2.X,p1.X)==0 && comp(p2.Y,p1.Y)==0) || (comp(p1.X,p3.X)==0 && comp(p1.Y,p3.Y)==0))
                            continue;
                        double dd=fabs((cross(p1,p2)+cross(p2,p3)+cross(p3,p1))/2);
                        if(comp(dd,A/2.0)==0)
                        {
                            f=1;
                            break;
                        }
                    }
                    if(f)
                        break;
                }
                if(f)
                    break;
            }
            if(f)
                break;
        }
        cout<<"Case #"<<nn+1<<": ";
        if(i==N+1 && j==M+1 && k==M+1 && l==N+1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<"0 0 "<<i<<" "<<j<<" "<<l<<" "<<k<<endl;
    }
    return 0;
}
