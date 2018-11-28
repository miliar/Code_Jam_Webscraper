#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
#include<map>
using namespace std;
typedef pair<int,int> PI;
typedef long long LL;
typedef double D;
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define R(I,N) for(int I=0;I<N;I++)
#define F(I,A,B) for(int I=A;I<B;I++)
#define FD(I,N) for(int I=N-1;I>=0;I--)
#define make(A) scanf("%d",&A)
char t[4][4];
bool spr(char z){
	R(i,4){
		bool x=1;
		R(j,4){
			if(t[i][j]!=z&&t[i][j]!='T')
			x=0;
		}
		if(x){
			printf("%c won\n",z);
			return 1;
		}
	}
	R(j,4){
		bool x=1;
		R(i,4){
			if(t[i][j]!=z&&t[i][j]!='T')
			x=0;
		}
		if(x){
			printf("%c won\n",z);
			return 1;
		}
	}
	bool x=1;
	R(i,4)if(t[i][i]!=z&&t[i][i]!='T')x=0;
	if(x){
		printf("%c won\n",z);
		return 1;
	}
	x=1;
	R(i,4)if(t[i][3-i]!=z&&t[i][3-i]!='T')x=0;
	if(x){
		printf("%c won\n",z);
		return 1;
	}
	return 0;
}
void test(){
	R(i,4)scanf(" %s",t[i]);
	if(spr('X'))return;
	if(spr('O'))return;
	R(i,4)R(j,4)if(t[i][j]=='.'){
		printf("Game has not completed\n");
		return ;
	}
	printf("Draw\n");
}
main(){
	int _;make(_);
	R(i,_){
		printf("Case #%d: ",i+1);
		test();
	}
}
