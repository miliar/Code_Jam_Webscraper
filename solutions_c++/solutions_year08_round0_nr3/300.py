
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
int T; 
const double pi=2*acos(0); 
double f,R,t,r,g; 
double S,fr,a,b,inR;
bool verb=0; 

double dist(double x,double y) { return sqrt(x*x+y*y); } 

double area(double x,double y){ // we know, that 0<=x,y<=inR 
    if(dist(x,y)>=inR) return 0; 
    
    double Ax=sqrt(inR*inR-y*y),Ay=y;
    double Bx=x,By=sqrt(inR*inR-x*x);
    double d=dist(Ax-Bx,Ay-By); 

	double tr= (Ax-x)*(By-y)/2; 
	double pl= asin(d/(2*inR))*inR*inR;
	double mn= sqrt(inR*inR- d*d/4.0) *d/2.0; 

   if(verb)	printf("x: %lf   y:  %lf pl: %lf  mn: %lf  res: %lf \n",x,y,pl,mn,tr+pl-mn); 
	return tr+pl-mn; 
} 

int main()
{
    scanf("%d",&T); 

	REP(nt,T){ 
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g); 

		if( g<=2*f) printf("Case #%d: %lf\n",nt+1,(double)1); 
		else { 
             S=pi*R*R; inR=R-t-f; 
			double y1,y2; 
			a=r+f; 
			b=r+g-f; 
			fr=0; 

			while(a<inR){ 
                   y1=r+f; y2=min(r+g-f,inR); 				
				   
				while(y1<inR){                    
				   fr=fr+area(a,y1)-area(a,y2)-area(b,y1)+area(b,y2); 	
					y1+=(g+2*r); 
					y2=min(y2+g+2*r,inR); 
				} 	
            
				a+=(g+2*r); b+=(g+2*r); 
			} 
          printf("Case #%d: %lf\n",nt+1,1-4*fr/S); 
//		  if(nt>0)verb=0; 
		} 


	} 



	return 0;
}

