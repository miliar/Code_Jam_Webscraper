#include<stdio.h>
#include<algorithm>
int s[201][2];
int m[201];
main(){
int T,TN;
int i,j,k;
int C,D;
scanf("%d",&T);
for(TN=1;TN<=T;TN++){
k=0;
scanf("%d%d",&C,&D);
for(i=0;i<C;i++){
scanf("%d%d",&s[i][0],&s[i][1]);
}
m[0]=0;
for(i=0;i<C;i++){
m[i+1]=m[i]+s[i][1];
}
for(i=0;i<C;i++){
for(j=i;j<C;j++){
k>?=D*m[j+1]-s[j][0]-D*m[i]+s[i][0]-D;
}
}
k*=5;
printf("Case #%d: %d.%d\n",TN,k/10,k%10);
}
}
