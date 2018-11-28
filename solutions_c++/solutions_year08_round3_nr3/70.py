# include <iostream>
# include <cstdio>
# include <cstdlib>
# include <algorithm>
# include <vector>
# include <string>
# include <cmath>

using namespace std;

long long LL[10000], A[4000000];


bool is(long long a){

	if(a==0) return true;
	int x[] = {2,3,5,7};

	for(int i = 0; i < 4; i++){
		while(a%x[i]==0) return true;
	}

	return false;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int TT;
	
	cin >> TT;
	
	long long M[2000], A[2000], B[2000], ans= 0;

	for(int tt = 1; tt <= TT; tt++){
		ans = 0;

		int n,m;
		long long X,Y,Z;
		cin >> n >> m >> X >> Y >> Z;

		for(int i = 0; i < m; i++) cin >> M[i];

		for(int i = 0; i < n; i++){
			A[i] = M[i%m];
			M[i%m] = (X * M[i%m] + Y*(i+1)) % Z;
			/*  print A[i mod m]
			  A[i mod m] = (X * A[i mod m] + Y * (i + 1)) mod Z
			  */
		}

		for(int i = 0; i < n; i++){
			B[i] = 1;

			for(int j = 0; j < i; j++) {
				if(A[i] > A[j]) B[i] = (B[i] +  B[j]) % 1000000007;
			}
			
			ans  = (ans + B[i]) % 1000000007;

		}



				cout << "Case #" << tt << ": " << ans << endl;	
	
		
	}

	


	return 0;
}