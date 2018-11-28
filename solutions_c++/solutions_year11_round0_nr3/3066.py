#include <cstdio>
#include <algorithm>
using namespace std;

int a[1003],n;

int zbr (int x, int y){
    int sum=0,p=0;
    for (int i=1;1;i*=2){
        if (i>x && i>y) break;
        if ((x>>p)%2==1 && (y>>p)%2==0) sum+=i; 
        if ((x>>p)%2==0 && (y>>p)%2==1) sum+=i; 
        ++p;
        //printf ("%d %d %d %d %d\n",i,sum,p,x,y);
    }
    return sum;
}

int rek (int poz, int pravi1, int fake1, int pravi2, int fake2){
    if (poz==n){
       if (pravi1==0 || pravi2==0) return 0; 
       if (fake1==fake2) return max(pravi1,pravi2); else return 0;
    }
    return max( rek (poz+1,pravi1+a[poz],zbr(fake1,a[poz]),pravi2,fake2) ,rek (poz+1,pravi1,fake1,pravi2+a[poz],zbr(fake2,a[poz])) );
}

void solve (int test){
     scanf ("%d",&n);
     for (int i=0;i<n;++i) scanf ("%d",&a[i]);
     int rj=0;
     int pravi1=0,pravi2=0,fake1=0,fake2=0;
     rj=rek(0,0,0,0,0);
     if (rj==0){
        printf ("Case #%d: NO\n",test,rj);
        return;
     }
     printf ("Case #%d: %d\n",test,rj);
}

int main (){
    int t;
    scanf ("%d",&t);
    for (int i=0;i<t;++i){
        solve(i+1);
    }
}
