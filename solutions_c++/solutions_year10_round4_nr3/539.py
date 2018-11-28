#include<cstdio>
#define INF 1234567890

int t,T;
int max(int a, int b) {return a>b?a:b;}

int A[101][101],B[101][101];
int Y=0,X=0;
void change(){
	for(int i=0;i<X;i++){
		for(int j=0;j<Y;j++){
			if(i==0 && j==0) B[i][j] = 0;
			else if(i==0) {if(A[i][j-1]==0) B[i][j] = 0;}
			else if(j==0) {if(A[i-1][j]==0) B[i][j] = 0;}
			else if(A[i-1][j]==0 && A[i][j-1]==0) B[i][j] = 0;
			else if(A[i][j-1]==1 && A[i-1][j]==1) B[i][j] = 1;
		}
	}
}
int check(){
	for(int i=0;i<X;i++) for(int j=0;j<Y;j++) if(A[i][j]==1) return 0;
	return 1;	
}

int main() {
	int i, j, K, k, sum = 0;
	int x1,x2,y1,y2;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		int time = 0;
		X = Y = 0;
		scanf("%d",&K);
		for(k=0;k<K;k++){
			scanf("%d %d %d %d",&y1,&x1,&y2,&x2);
			X = max(x2, X);
			Y = max(y2, Y);
			x1--;y1--;x2--;y2--;
			for(i=x1;i<=x2;i++) for(j=y1;j<=y2;j++) A[i][j]=B[i][j]=1;
		}	
		
		while(!check()){
			change();
			time++;
			for(i=0;i<X;i++)
			for(j=0;j<Y;j++)
				A[i][j]=B[i][j];
		}	
		printf("Case #%d: %d\n",t,time);	
	}
	return 0;	
}
