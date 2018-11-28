#include<stdio.h>
char a[100][100],A,B,n,K;
int Q(int x,int y){
int i;
for(i=1;i<K&&i+x<n&&a[i+x][y]==a[x][y];i++);
if(i==K)return 1;
for(i=1;i<K&&i+y<n&&a[x][i+y]==a[x][y];i++);
if(i==K)return 1;
for(i=1;i<K&&i+x<n&&i+y<n&&a[i+x][i+y]==a[x][y];i++);
if(i==K)return 1;
for(i=1;i<K&&i+x<n&&y-i>=0&&a[i+x][y-i]==a[x][y];i++);
if(i==K)return 1;
return 0;
}
int main(){
int T,t,i,j,k;
scanf("%d",&T);
for(t=1;t<=T;t++){
A=0;B=0;
scanf("%d%d",&n,&K);
for(i=0;i<n;i++){
scanf("%s",a[i]);
for(k=n-1,j=n-1;j>=0;j--){if(a[i][j]!='.')a[i][k--]=a[i][j];}
for(;k>=0;k--)a[i][k]='.';
}
for(i=0;i<n;i++){
	for(j=0;j<n;j++){
		if(a[i][j]!='.'){if(Q(i,j)){if(a[i][j]=='R')A=1;else B=1;}}
		}
	}
printf("Case #%d: ",t);
if(A==1&&B==1)puts("Both");
else if(A==1)puts("Red");
else if(B==1)puts("Blue");
else puts("Neither");
}
} 
