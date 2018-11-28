#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<algorithm>

using namespace std;

int i,j,k,n,m,a,b,c,d,caso=1, t;
int N,S,p;

int main(){

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	cin >> t;
	while(t--){
		scanf("%d%d%d", &N, &S, &p);
		int resp = 0;
		for(i=0;i<N;i++){
			scanf("%d", &a);
			// printf("%d\n", p - ((a-p)/2));
			if( a >= p && p - ((a-p)/2) < 2){
				resp++;
			}
			else if( a >= p && p - ((a-p)/2) == 2 && S > 0) { 
				resp++; 
				S--;
			}
		}
		printf("Case #%d: %d\n", caso++, resp);
	}

	return 0;
}
