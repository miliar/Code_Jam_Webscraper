#include<iostream>
using namespace std;
int C[20000], G[20000];

const int INF=1000000000;
void corINF(int &c){
	if(c>=INF)
		c=INF;
}
int Rc[2][20000];

int R(int i){
	return i<<1;
}
int L(int i){
	return (i<<1)+1;
}
int main(){
	int N;
	cin>>N;
	for(int test=1; test<=N; test++){
		int M, V;
		cin>>M>>V;
		for(int i=1; i<=(M-1)/2; i++)
			cin>>G[i]>>C[i];
		for(int i=1; i<=(M+1)/2; i++){
			int j=i+(M-1)/2;
			int a; cin>>a;
			Rc[1][j]=Rc[0][j]=INF;
			if(a==1)
				Rc[1][j]=0;
			else
				Rc[0][j]=0;
		}

#define cRR(va,a,b,of) Rc[va][i]=min(Rc[va][i], Rc[a][L(i)]+Rc[b][R(i)]+of)
		for(int i=(M-1)/2; i>=1; i--)
			if(G[i]==1){
				Rc[0][i]=INF;
				cRR(0,0,1,0);
				cRR(0,0,0,0);
				cRR(0,1,0,0);
				corINF(Rc[0][i]);

				Rc[1][i]=INF;
				cRR(1,1,1,0);
				if(C[i]==1){
					cRR(1,1,0,1);
					cRR(1,0,1,1);
				}
				corINF(Rc[1][i]);
			}
			else{
				Rc[0][i]=INF;
				cRR(0,0,0,0);
				if(C[i]==1){
					cRR(0,1,0,1);
					cRR(0,0,1,1);
				}
				corINF(Rc[0][i]);

				Rc[1][i]=INF;
				cRR(1,1,1,0);
				cRR(1,0,1,0);
				cRR(1,1,0,0);
				corINF(Rc[1][i]);
			}
		if(Rc[V][1]==INF)
			printf("Case #%d: IMPOSSIBLE\n", test, Rc[V][1]);
		else
			printf("Case #%d: %d\n", test, Rc[V][1]);
	}
	return 0;
}
