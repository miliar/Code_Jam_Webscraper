#include<stdio.h>
#include<algorithm>
using namespace std;
int A[1000][1000],B[1000][1000], Y=0,X=0;
void dr(){
	for(int i=0;i<X;i++){
		for(int j=0;j<Y;j++){
			if(A[i][j]==1){
				if(i==0 && j==0)B[i][j] = 0;
				else if(i==0)if(A[i][j-1]==0)B[i][j] = 0;
				else if(j==0)if(A[i-1][j]==0)B[i][j] = 0;
				if(A[i-1][j]==0 && A[i][j-1]==0)B[i][j] = 0;
			}
			if(A[i][j]==0 && i!=0 && j!=0)if(A[i][j-1]==1 && A[i-1][j]==1)B[i][j] = 1;
		}
	}
}
int ok(){
	for(int i=0;i<X;i++)
		for(int j=0;j<Y;j++)
			if(A[i][j]==1)return 0;
	return 1;	
}
int main() {
	int i, j, p, T, t, k, sum = 0, H=0;
	int x1,x2,y1,y2;
	freopen("new2.in","r",stdin);
	freopen("new.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		H = 0;X=Y=0;
		scanf("%d",&k);
		for(i=0;i<k;i++){
			scanf("%d%d%d%d",&y1,&x1,&y2,&x2);
			X = max(max(x1,x2) , X);;
			Y = max(max(y1,y2) , Y);
			x1--;y1--;x2--;y2--;
			for(j=x1;j<=x2;j++){
				for(p=y1;p<=y2;p++)
					A[j][p]=B[j][p]=1;
			}
		}	
		
		while(ok()==0){
			dr();
			H++;
			for(j=0;j<X;j++)for(p=0;p<Y;p++)A[j][p]=B[j][p];
		}	
		printf("Case #%d: %d\n",t,H);
		for(i=0;i<X;i++) for(j=0;j<Y;j++) A[i][j] = B[i][j] = 0;	
	}
	return 0;	
}
