#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int T, tc;
int spid[1000002];
int N,X,R,S;
int t;
int a,b,c;

int main() {
    freopen("res2.out","w",stdout);
    freopen("res2.txt","r",stdin);

scanf("%d",&T);
for (int ii = 1;ii<=T;ii++) {
    memset(spid,0,sizeof(spid));
    scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
    double runs = t;
    for (int i=0;i<N;i++) {
        scanf("%d%d%d",&a,&b,&c);
        for (int j = a;j< b;j++){
            spid[j] = c;
            }
        }
        
   
sort(spid, spid + X);
double res=0.0;
for (int i=0;i<X;i++) {
    double rt, men= 0.0;
    double wows = spid[i] + S;
    if (runs > 0.0) 
       {
             rt = (1/(wows - S + R));
             if (runs < rt) men = 1.0 - (runs / rt);
             else men = 0.0;
             if (runs < rt) rt = runs;
             runs-=rt;
             res+= rt;
             }
    else men = 1.0;
    
    
    res+= (men/wows);
    }
printf("Case #%d: %.8lf\n",ii,res);
}

}
