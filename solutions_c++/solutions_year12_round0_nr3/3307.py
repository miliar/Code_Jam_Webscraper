#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
using namespace std;

int numDig( int n ){int i=0;while(n){n/=10;++i;} return i;}
int numPow( int n, int i ){int t = n;while(--i){n*=t;}return n;}
int rotNum( int n, int tam ){
	int mov = numPow(10, tam);
	int back = n % mov;
	int front = n / mov;
	int mov2 = numPow(10, numDig(front));
	return back * mov2 + front;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int N, a, b;
	scanf("%d", &N);
	for(int n=0;n<N;++n){
		scanf("%d %d", &a, &b);
		int cont = 0;
		for(int i=a;i<=b;++i){
			int dig = numDig(i);
			for(int j=1;j<dig;++j){
				int r = rotNum(i, j);
				if(r>i && r<=b)
					cont++;
			}
		}
		printf("Case #%d: %d\n", n+1, cont);
	}
}