#include <iostream>
#include <vector>
using namespace std;

long long ans[505][505];
int main(){
	long long i,j,k,x,z;
	long long C[505][505];
	int T,t,y;
	
	C[0][0]=1;
	for(i=1;i<=503;i++){
		C[i][0]=1;
		for(j=1;j<=i;j++){
			C[i][j]= (C[i-1][j] + C[i-1][j-1])%100003;
		}
	}
	
	for(i=2;i<=502;i++){
		ans[i][1] = 1;
		for(j=2;j<i;j++){
			x = 0;
			for(k=1;k<j;k++){
				if((j-k) <= (i-j))
					x += ((ans[j][k]*C[(i-j)-1][(j-k)-1])%100003);
			}
			x %= 100003;
			ans[i][j] = x;
		}
	}
	
	cin>>T;
	t = 1;
	while(T--){
		cin>>y;
		
		z = 0;
		for(i=1;i<y;i++)
			z += ans[y][i];
			
		z %= 100003;
		printf("Case #%d: %lld\n",t,z);
		t++;
	}
	return 0;
}
	