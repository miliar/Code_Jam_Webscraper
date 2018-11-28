#pragma comment(linker, "/STACK:36777216")

#include <algorithm>
#include <iostream>
#include<stdio.h>
#include <string>
#include<sstream>   
#include<string.h>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<pii,int> p3i;
typedef long double ld;
typedef vector<ld> vd;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define SORT(a) sort((a).begin(),(a).end())

const ld pi = acosl(-1.);
const ld eps = 1e-9;
typedef long double ld;
typedef pair<ld,int> pdi;

ld S[1111];
ld p[1111];
int n,k,l;
int x[5111],y[5111];
int mx[5111],my[5111];
bool u[1111];
double r[5555];

double getA(double a,double r){
    return a/2 * r * r - r*r*sin(a)/2;
}

int main(){
#ifdef LocalHost
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int TC;
    cin>>TC;
    REP(tc,TC){
        int m;
        cin>>n>>m;
        REP(i,n) scanf("%d %d",x+i,y+i);
        REP(i,m) scanf("%d %d",mx+i,my+i),mx[i]-=x[0],my[i]-=y[0];
        printf("Case #%d:",tc+1);

        x[1]-=x[0],y[1]-=y[0];
        x[0]=0,y[0]=0;
        
        REP(well,m){        
            double res = 0;
            REP(i,n) r[i]=hypot(x[i]-mx[well],y[i]-my[well]);

            double d = hypot(x[0]-x[1],y[0]-y[1]);

            double a1 = 2*acos((r[0]*r[0]+d*d - r[1]*r[1])/2/r[0]/d);
            double a2 = 2*acos((r[1]*r[1]+d*d - r[0]*r[0])/2/r[1]/d);
             double pi = acos(-1.);

       //      a1=min(2*pi-a1,a1);
         //   a2=min(2*pi-a2,a2);

            double s1 = getA(a1,r[0]);
            double s2 = getA(a2,r[1]);

           
            res = s1+s2;;
            /*if(d > r[1]) res+=s1;
            else res += pi*r[0]*r[0]-s1;
            
            if(d > r[0]) res+=s2;
            else res += pi*r[1]*r[1]-s2;
            
     */     
            printf(" %.7lf",res);
        }

        puts("");
    }
    return 0;
}
