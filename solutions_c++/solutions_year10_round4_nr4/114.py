#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> pii; 

#define PI acos(-1.0)
#define sqr(x) ((x) * (x))
#define dis2(a, b) (sqrt(sqr(a.first - b.first) + sqr(a.second - b.second) + 0.0))

pii x[2], r;

 int main() 
 {
    int cn;
    cin>>cn;
    for (int ci = 1; ci <= cn; ci++) {
        printf("Case #%d: ", ci); 
        int N, M;
        cin>>N>>M;
        REP(i, N) 
            cin>>x[i].first>>x[i].second;
        REP(i, M) {
            double A1, A2, d, ang1, ang2;
            pii y;
            cin>>y.first>>y.second;
            double c1 = dis2(y, x[0]);
            double c2 = dis2(y, x[1]);
            double ans = 0;  
            A1 = PI * sqr(c1);  
            A2 = PI * sqr(c2);  
            d = dis2(x[0], x[1]);
               
            ang1 = acos((sqr(c1)+ sqr(d) - sqr(c2)) / 2 / c1/ d);  
            ang2 = acos((sqr(c2)+ sqr(d) - sqr(c1)) / 2 / c2/ d);  
            
            ans -= sqr(c1) * ang1 - sqr(c1) * sin(ang1) * cos(ang1);
            ans -= sqr(c2) * ang2 - sqr(c2) * sin(ang2) * cos(ang2); 
            printf("%.10lf", -ans);
            if (i == M - 1)
                puts("");
            else
                putchar(' ');
        }
    }
}