#include <iostream>
#include <math.h>
#include <stdio.h>

#define  rep(i,a,b) for ( int i = a; i<=b; i++ )

using namespace std ;

int main(){
	int T; int N; 
	int A[1010],H[1010];
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout); 

	cin >> T; 

	rep(t,1,T) {
		 
		cin >> N; 
		double kq = N; 

		rep(i,1,N) {
			cin >> A[i];
			if (A[i]==i) kq-=1;  
		}

		printf("Case #%d: %.6lf\n", t, kq); 
	}
	return 0; 
}	