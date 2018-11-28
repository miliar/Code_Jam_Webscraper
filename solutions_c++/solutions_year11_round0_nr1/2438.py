//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, to) for(int i = 0; i<to; ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)

int t,a,N,X[3],px,x,C,S,P;
char ch;
inline int mabs(int a){
	return (a<0)?-a:a;
}

int main(){
	scanf("%d", &t);
	For(T,t){
		X[0] = X[1] = 1;
		C = S = P = px = 0;
		scanf("%d ", &N);
		For(i, N){
			scanf("%c %d ",&ch, &a);
			if (ch=='B') x = 0;
			else x = 1;
			if (px==x){
				S += mabs(X[x]-a)+1;
				C += mabs(X[x]-a)+1;
			}else{
				P = max(0, mabs(X[x]-a)-S)+1;
				C += P;
				S = P;
			}
			X[x] = a;
			px = x;
		}
		printf("Case #%d: %d\n",T+1, C);
	}
}