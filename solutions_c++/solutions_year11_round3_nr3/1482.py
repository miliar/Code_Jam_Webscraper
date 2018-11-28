#include<iostream>
#include<cstdio>
#include<vector>
#include<list>
#include<map>
#include<cmath>
#include<cstdlib>
using namespace std;
#define EPS 0.000001
#define FOR(i,N) for(int i=0;i<N;i++)
#define FORE(i,N) for(int i=1;i<=N;i++)
#define isInt(a) (fabs((a - (int)a))<EPS)
#define lenght(x,y,z) sqrt(x*x+y*y+z*z)
#define max(a,b)  a>b?a:b
#define min(a,b)  a<b:b:a



int main(void){
	long long T, N, L , H;
	cin >> T;
	int o[1000];
	FORE(ct,T){
		printf("Case #%d: ",ct);
		cin >> N >> L >> H;
		FOR(i,N) cin >> o[i];
		long long fqr = 10000000000000001;
		int possible = false;
		for(int i=L;i<=H && !possible;i++){
			int could = true;
			long long fqrm = 10000000000000001;
			for(int j=0;j<N && could;j++){
				if( (i%o[j])==0 || (o[j]%i)==0 ){				
					if(o[j]<fqr) fqrm = i;
				}else could = false;
			}
			if(could){
               if(fqrm<fqr) fqr = fqrm;	
			   possible = true;
			}	
		}
		if(possible) cout << fqr << endl;
		else cout << "NO\n";
	}
	return 0;
}
