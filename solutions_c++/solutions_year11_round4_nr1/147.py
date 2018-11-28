#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

const int MaxN=1005;
const double dd=1e-10;
double X,S,R;
int N;
int T;
double t;
int B[MaxN],E[MaxN],W[MaxN],P[MaxN];
bool cmp(int x,int y) {return W[x]<W[y];}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>T;
    for (int cnt=1;cnt<=T;++cnt) {
        cin>>X>>S>>R>>t>>N;
        double sum=X;
        for (int i=1;i<=N;++i) {scanf("%d%d%d",&B[i],&E[i],&W[i]);sum-=E[i]-B[i];}
        if (sum/R<t+dd) t-=sum/R,sum=sum/R;
        else sum=(sum-t*R)/S+t,t=0;
        for (int i=1;i<=N;++i) P[i]=i;
        sort(P+1,P+N+1,cmp);
        for (int i=1;i<=N;++i) {
            int x=P[i];
            if ((E[x]-B[x])*1.0/(W[x]+R)<t+dd) sum+=(E[x]-B[x])*1.0/(W[x]+R),t-=(E[x]-B[x])*1.0/(W[x]+R);
            else sum+=t+(E[x]-B[x]-(W[x]+R)*t)*1.0/(W[x]+S),t=0;
        }
        printf("Case #%d: %.8lf\n",cnt,sum);
    }
    return 0;
}
