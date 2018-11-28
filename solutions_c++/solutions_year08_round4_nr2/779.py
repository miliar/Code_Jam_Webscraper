#include <vector>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <complex>
#include <cassert>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;

typedef complex<double> mycomp;

#define DET(a,b,c,d)         ((a)*(d)-(b)*(c)) 

inline double flaeche(mycomp a,mycomp b,mycomp c){
	return DET(real(b-a),real(c-a),imag(b-a),imag(c-a));
}

string doit(){
	char doit[80];
	int n,m,A;
	cin >> n >> m >> A;

	for(int x0=0;x0<=n;x0++){
		for(int y0=0;y0<=m;y0++){
			for(int x1=0;x1<=n;x1++){
				for(int y1=0;y1<=m;y1++){
					mycomp a(0,0),b(x0,y0),c(x1,y1);
					if(fabs(flaeche(a,b,c)-(double)A)<1e-9){
						sprintf(doit,"0 0 %d %d %d %d",x0,y0,x1,y1);
						goto end;
					}	
				}
			}
		}
	}
	sprintf(doit,"IMPOSSIBLE");

	goto end;
	//IMPOSSIBLE	
	if(n*m<A) sprintf(doit,"IMPOSSIBLE");
	else{
		if(n>=m){
			for(int i=n;i>0;i--){
				if(A%i==0){
					int x=i;
					int y=A/x;
					if(y>m){
						sprintf(doit,"IMPOSSIBLE");
						goto end;
					}	
					assert(A==x*y);
					assert(x<=n);
					if(y>m){
						cerr << "x: "<<x<<" y: "<<y<<" n: "<<n<<" m: "<<m<<" A: "<<A<<endl;
						assert(y<=m);
					}	
					sprintf(doit,"0 0 %d 0 %d %d",x,x,y);
					break;
				}
				
			}
		}else{
			for(int i=m;i>0;i--){
				if(A%i==0){
					int y=i;
					int x=A/y;
					assert(A==x*y);
					if(x>n){
						sprintf(doit,"IMPOSSIBLE");
						goto end;
					}
					assert(x<=n);
					assert(y<=m);
					sprintf(doit,"0 0 %d 0 %d %d",x,x,y);
					break;
				}
			}


		}
	}
end:	
	string ret(doit);
	return ret;
}	

int main(){
	int num_cases;
	cin >> num_cases;
	for(int kase=1;kase<=num_cases;kase++){
		cerr << "kase: "<<kase<<endl;
		cout << "Case #"<<kase<<": "<< doit()<<endl; 
	}	
	return 0;
}	
