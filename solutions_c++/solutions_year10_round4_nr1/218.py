#include<stdio.h>
char c[300][300],s[100];
int n;
int Q(int x){
int i,j;
for(i=0;i<n*2-1;i++){
for(j=1;x-j>=0;j++){
	if(c[i][j+x]==0||c[i][x-j]==0||j+x>300)break;
	if(c[i][j+x]==' '||c[i][x-j]==' ')continue;
	if(c[i][j+x]!=c[i][x-j])return 0;
	}
}
return 1;
}
int Q2(int x){
int i,j;
for(i=0;i<n*2-1;i++){
for(j=1;x-j>=0;j++){
	if(c[j+x][i]==0||c[x-j][i]==0||j+x>300)break;
	if(c[j+x][i]==' '||c[x-j][i]==' ')continue;
	if(c[j+x][i]!=c[x-j][i])return 0;
	}
}
return 1;
}
int main(){
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
int T,t,i,k,ans,r,k2,j;
scanf("%d",&T);gets(s);
for(t=1;t<=T;t++){
for(i=0;i<300;i++)for(j=0;j<300;j++)c[i][j]=0;
scanf("%d",&n);gets(s);
k=n;ans=0;
for(i=0;i<n*2-1;i++)gets(c[i]);
for(i=n-1;i<n*2-1;i++){
	if(Q(i))break;
	ans+=k*2+1;
	k++;
	}
for(i=n-1,r=0,k2=n;i>=0;i--){
if(Q(i))break;
r+=k2*2+1;
k2++;
}
if(r<ans){ans=r;k=k2;}
r=ans;k2=k;
for(i=n-1;i<n*2-1;i++){
	if(Q2(i))break;
	ans+=k*2+1;
	k++;
	}
for(i=n-1;i>=0;i--){
if(Q2(i))break;
r+=k2*2+1;
k2++;
}
if(r<ans)ans=r;
printf("Case #%d: %d\n",t,ans);
}
}
