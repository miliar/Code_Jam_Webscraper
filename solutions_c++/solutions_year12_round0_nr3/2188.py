#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <set>

using namespace std;

int base[10] = {1,
				10,
				100,
				1000,
				10000,
				100000,
				1000000,
				10000000,
				100000000,
				1000000000
				};

int invert(int a, int n, int digits){
	int res=0, front, back;
	front = floor(a/base[n]);
	if(front==0) return -1;
	back = a%base[n];
	//printf("%d + %d*%d =",front, back,base[digits-n]);
	res = back*base[digits-n] + front;
	//printf("%d\n", res);
	return res;
}

int digits(int n){
	int d=0;
	while(n/10){
		d++;
		n/=10;
	}
	return d+1;
}

int main(){
	int i,j,k;
	int T, A, B;
	int n,d;
	char input[1024];
	set<int> numbers;
	
	scanf("%d\n",&T);
	
	//for(i=1;i<4;i++){
	//	printf("%d %d\n",1115,invert(1115, i, digits(1115)));
	//}
	//return 0;
	for(int cases=0; cases<T; cases++){
		scanf("%d %d\n",&A, &B);
		d = digits(A);
		k=0;
		for(i=A; i<B; i++){
			numbers.clear();
			for(j=1;j<d; j++){
				n = invert(i, j, d);
				if(n<0) break;
				if(n>i && n<=B) {
					if(!numbers.count(n)){
						numbers.insert(n);
						k++;
					}
				}
			}
		}
		printf("Case #%d: ",cases+1);
		//print solution
		printf("%d\n",k);
	}
	

}
