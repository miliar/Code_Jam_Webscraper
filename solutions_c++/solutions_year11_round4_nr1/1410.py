#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int Tc;
double L;
double walk;
double run;
double Limit;
double ans;
int n;
struct Node{double Len,v;}a[100005];

bool cmp(Node A,Node B){
    return A.v<B.v;
}

void add(double Len,double base_v){
    if (Limit*(base_v+run)>=Len){
        Limit-=Len/(base_v+run);
        ans+=Len/(base_v+run);
    }
    else{
        ans+=Limit;
        ans+=(Len-Limit*(base_v+run))/(base_v+walk);
        Limit=0;
    }
}

int main(){
    freopen("A.in","r",stdin);
    freopen("solve.out","w",stdout);
    cin >> Tc;
    for (int k=1;k<=Tc;k++){
        cin >> L >> walk >> run >> Limit >> n;
        double Sum=0,rest=0;
        for (int i=0;i<n;i++){
            double s,e;
            cin >> s >> e >> a[i].v;
            a[i].Len=e-s;
            Sum+=a[i].Len;
        }
        rest=L-Sum;
        a[n].v=0;
        a[n].Len=rest;
        n++;
        sort(a,a+n,cmp);
        ans=0;
        for (int i=0;i<n;i++)
          add(a[i].Len,a[i].v);
        printf("Case #%d: %.9lf\n",k,ans);
    }
}
