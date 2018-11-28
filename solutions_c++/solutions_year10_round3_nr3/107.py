#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int m,n;
int mp[512][512];

bool jd(int i,int j,int k){
	int jou[2];
	if(mp[i][j]==0) {
		jou[(i+j)%2]=0;
		jou[(i+j+1)%2]=1;
	}
	else if(mp[i][j]==1) {
		jou[(i+j)%2]=1;
		jou[(i+j+1)%2]=0;
	}
	else return false;
	for(int ii=i;ii<i+k;ii++){
		for(int jj=j;jj<j+k;jj++){
			int t=(ii+jj)%2;
			if(jou[t]!=mp[ii][jj]) break;
		}
		if(jj<j+k) break;
	}
	if(ii<i+k) return false;
	return true;
}

int main()
{
   int cs,fat=0;
   freopen("C:\\a.in","r",stdin);
   freopen("C:\\a.out","w",stdout);
   scanf("%d",&cs);
   for(fat=1;fat<=cs;fat++)
   {
	   scanf("%d%d",&m,&n);
	   int i,j,k;
	   for(i=0;i<m;i++){
		   char ch[210];
		   scanf("%s",ch);
		   for(j=0;j<n/4;j++){
			   int t;
			   if(ch[j]>='0'&&ch[j]<='9') {
				   t=ch[j]-'0';
			   }
			   else {
				   t=ch[j]-'A'+10;
			   }
			   mp[i][j*4+3]=t&1;
			   t/=2;
			   mp[i][j*4+2]=t&1;
			   t/=2;
			   mp[i][j*4+1]=t&1;
			   t/=2;
			   mp[i][j*4+0]=t&1;
		   }
	   }
/*	   for(i=0;i<m;i++) {
		   for(j=0;j<n;j++){
			   printf("%d",mp[i][j]);
		   }
		   printf("\n");
	   }
*/	   i=m;
	   if(i>n) i=n;
	   int ans=0;
	   int cxx[512];
	   for(j=0;j<=m;j++) cxx[j]=0;
	   while(i>1){
		   for(j=0;j+i<=m;j++){
			   for(k=0;k+i<=n;k++){
				   if(jd(j,k,i))
					   break;
			   }
			   if(k+i<=n) break;
		   }
		   if(j+i<=m) {
			   cxx[i]++;
			   ans+=i*i;
			   for(int jj=j;jj<j+i;jj++){
				   for(int kk=k;kk<k+i;kk++){
					   mp[jj][kk]=-1;
				   }
			   }
		   }
		   else {
			   i--;
		   }
	   }
	   int tx=0;
	   cxx[1]=m*n-ans;
	   for(i=m;i>=1;i--) if(cxx[i]) tx++;
	   printf("Case #%d: %d\n",fat,tx);
	   for(i=m;i>=1;i--) {
		   if(cxx[i]){
			   printf("%d %d\n",i,cxx[i]);
		   }
	   }
   }
   return 0;
}
