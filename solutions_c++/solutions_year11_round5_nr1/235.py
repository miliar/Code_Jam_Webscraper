#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <complex>
#include <vector>
#define PB push_back

using namespace std;

int T,W,L,U,G;
typedef complex<double> CD;
typedef vector<CD> VC;
CD LB[1005],UB[1005];
VC V;
CD Cross(CD A,CD B,double x) {
   return (B-A)/(B.real()-A.real())*(x-A.real())+A;
}
double CP(CD A,CD B) {return A.real()*B.imag()-A.imag()*B.real();}
double Area(VC &V) {
       double sum=0;
       for (int i=0;i<V.size();++i)
           if (i+1==V.size()) sum+=CP(V[i],V[0]);
           else sum+=CP(V[i],V[i+1]);
       return abs(sum/2);
}
const double dd=1e-10;
double Solve(double last,double x) {
       V.clear();
       //for (int i=1;i<=L;++i) cout<<LB[i]<<" ";
       //cout<<"\n";
       //for (int i=1;i<=U;++i) cout<<UB[i]<<" ";
       //cout<<"\n";
       for (int i=1;i<=L;++i) {
           if (LB[i].real()-last<-dd) 
              if (LB[i+1].real()-last>dd)
                 V.PB(Cross(LB[i],LB[i+1],last));
           if (LB[i].real()>last-dd && LB[i].real()<x+dd) V.PB(LB[i]);
           if (LB[i].real()-x>dd) break;
           else if (LB[i+1].real()-x>dd)
                V.PB(Cross(LB[i],LB[i+1],x));
       }
       for (int i=U;i>=1;--i) {
           if (UB[i].real()-x>dd)
              if (UB[i-1].real()-x<-dd)
                 V.PB(Cross(UB[i-1],UB[i],x));
           if (UB[i].real()>last-dd && UB[i].real()<x+dd) V.PB(UB[i]);
           if (UB[i].real()-last<-dd) break;
           else if (UB[i-1].real()-last<-dd)
                V.PB(Cross(UB[i-1],UB[i],last));
       }
       //cout<<last<<" "<<x<<"\n";
       //for (int i=0;i<V.size();++i) cout<<V[i]<<" ";
       //cout<<"\n";
       return Area(V);
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>T;
    for (int t=1;t<=T;++t) {
        cout<<"Case #"<<t<<":\n";
        cin>>W>>L>>U>>G;
        for (int i=1;i<=L;++i) {
            int x,y;
            scanf("%d%d",&x,&y);
            LB[i]=CD(x,y);
        }
        for (int i=1;i<=U;++i) {
            int x,y;
            scanf("%d%d",&x,&y);
            UB[i]=CD(x,y);
        }
        V.clear();
        for (int i=1;i<=L;++i) V.PB(LB[i]);
        for (int i=U;i>=1;--i) V.PB(UB[i]);
        double area=Area(V)/G;
        double last=0;
        //cout<<area<<"\n";
        for (int i=1;i<G;++i) {
            double l=last,r=W;
            while (l<r-1e-8) {
                  double mid=(l+r)/2;
                  if (Solve(last,mid)<area) l=mid;
                  else r=mid;
            }
            last=l;
            printf("%.8lf\n",l);
        }
    }
    return 0;
}
