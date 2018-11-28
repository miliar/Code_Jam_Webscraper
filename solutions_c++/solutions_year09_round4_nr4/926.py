#include<stdio.h>

int n,t,tc;
int i,j;
char c[50];
bool ar[50][50];
long long col[50];
int cco[50];
int res;

bool runtuh(int r,int c){
	if(ar[r][c]==0) return true;
	if(r==n-1){
		return false;
	}
	else{
		if((r<n-1)&&(runtuh(r+1,c))){
			int tp=ar[r+1][c];
			ar[r+1][c]=ar[r][c];
			ar[r][c]=tp;
			res++;
			if(r+1<c) runtuh(r+1,c);
			return true;
		}
		else if((c>0)&&(runtuh(r,c-1))){
			int tp=ar[r][c-1];
			ar[r][c-1]=ar[r][c];
			ar[r][c]=tp;
			res++;
			if(r<c-1) runtuh(r,c-1);
			return true;
		}
		return false;
	}
}

int main(){
	scanf("%d",&t);
	for(tc=1;tc<=t;tc++){
		res=0;
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",c);
			for(j=0;j<n;j++){
				if(c[j]=='1') ar[i][j]=true;
				else ar[i][j] = false;
			}
		}

		for(j=0;j<n;j++){
			runtuh(0,j);
		}
		
		printf("\n");
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				printf("%d",ar[i][j]);
			}
			printf("\n");
		}
		printf("%d\n",res);
	}


	return 0;
}
