#include<cstdio>
#include<cmath>
#include<cstring>
#define siz 110
int ABS(int a ){return a < 0 ? -a : a;}
int task[siz][2];
char str[2];
int A[siz];
int B[siz];
int disA[siz];
int disB[siz];
int inA;
int inB;
int posA,posB;
int N ;
void ini(){
	int i;
	for( i =0 ;i< N; i++){
		A[i] = B[i] = 0;
		disA[i] = disB[i] = 0;
	}
}
int newDist(int val, int b){
	if(val > b) return val - b;
	return 0;
}
int main(){
	//freopen("A.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int kase, ct = 1;
	int i,a;
	scanf("%d", &kase);
	while(kase--) {
		scanf("%d", &N);
		ini();
		inA = 0;
		inB = 0;
		for( i =0; i < N; i++){
			scanf("%s %d",str, &a);
			if(str[0]=='O') {
				task[i][0]=0;
				task[i][1]=a;
				A[inA++] = a;
			}
			else {
				task[i][0] = 1;
				task[i][1] = a;
				B[inB++] = a;
			}
		}
		disA[0] = A[0] - 1;
		disB[0] = B[0] - 1;
		for( i = 1; i <inA; i++){
			disA[i] = ABS(A[i] - A[i-1]);
		
		}
		for( i = 1; i <inB; i++){
		
			disB[i] = ABS(B[i] - B[i - 1]);
		}

		posA = 0;
		posB = 0;
		int res  =0;
		for( i = 0; i<N; i++){
			if(task[i][0]==0) {
				res += (disA[posA] + 1);
				disB[posB]=newDist(disB[posB],disA[posA] + 1);
				posA++;
			}
			else {
				res+= (disB[posB] + 1);
				disA[posA] = newDist(disA[posA], disB[posB] + 1);
				posB++;
			}
		}
		printf("Case #%d: %d\n",ct++, res );
	}
	return 0;
}