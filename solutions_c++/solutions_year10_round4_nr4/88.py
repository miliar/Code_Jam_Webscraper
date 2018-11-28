
// Headers {{{
#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define CLR(A,v) memset((A),v,sizeof((A)))
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SIZE(x) (int)(x.size())
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long LL;
typedef long double LD; 
typedef vector<string> VS;
// }}}

const double pi = acos(0) * 2; 

class point { 
    public: 
        double x,y; 
        void get() { 
            scanf("%lf%lf",&x,&y); 
        }        
                 
} ; 

double sqr(double x) { return x*x; } 

double dist(const point &A, const point &B) { 
    return sqrt(sqr(A.x-B.x) + sqr(A.y-B.y)); 
} 

double pole(double a, double b, double c) { 
    double p = (a + b + c) / 2; 
    return sqrt(max(0.0,p*(p-a)*(p-b)*(p-c))); 
}

double lezka(double h, double r) { 
//    printf("lezka %lf  %lf\n",h,r); 
    double alpha = asin(min(1.0,h/r)); 
//    printf("%lf\n",alpha);  
    return r*r*alpha - r*r*sin(alpha*2)/2.0; 
} 

 
int main()
{
    int T,N,M; 
    scanf("%d",&T);      
    FOR(tc,1,T) { 
        scanf("%d%d",&N,&M); 
        point A,B; 
        A.get(); 
        B.get(); 
        double d = dist(A, B); 
        printf("Case #%d:",tc); 

        REP(i,M) { 
            point X; 
            X.get(); 
            double r1 = dist(A, X), r2 = dist(B, X); 
            double cr; 
            if (r1 > r2) swap(r1, r2); 
            double h = 2*pole(r1,r2,d) / d; 
//            printf("r1=%lf  r2=%lf h=%lf  d=%lf\n",r1,r2,h,d); 

            if (sqr(r1) + sqr(d) > sqr(r2)) { 
  //              printf("dupa\n");  
                cr = lezka(h,r1) + lezka(h,r2);                 
            } 
            else { 
                cr = r1*r1*pi - lezka(h,r1) + lezka(h,r2); 
            } 
            printf(" %.10lf",cr);  
    //        puts("");  
        }  
        puts("");         
    } 


	return 0;
}

