//

#include<vector>
#include<utility>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std;

const int N=200;
double win[N],all[N],wp[N],owp[N],oowp[N],res[N],dtmp;
char data[200][200];

int main() {
     freopen("test.in","r",stdin);
	 freopen("test.out","w",stdout);

	 int ca,i,n,j,k,cnt;
	 cin>>ca;
	 for(i=1;i<=ca;++i) {
		 cin>>n;
		 for(j=0;j<n;++j) {
			 for(k=0;k<n;++k) {
				 cin>>data[j][k];
			 }
		 }

		 for(j=0;j<n;++j) {
			 win[j]=all[j]=0;
			 for(k=0;k<n;++k) {
				 if( data[j][k]=='1' ) ++win[j],++all[j];
				 if( data[j][k]=='0' ) ++all[j];
			 }
			 res[j]=0.25*(win[j]/all[j]);
		 }

		 for(j=0;j<n;++j) {
			 cnt=owp[j]=0;
			 for(k=0;k<n;++k) {
				 if( data[j][k]!='.' ) {
					 ++cnt;
					 if( data[j][k]=='1' ) owp[j]+=win[k]/(all[k]-1);
					 else                  owp[j]+=(win[k]-1)/(all[k]-1);
				 }
			 }
			 owp[j]/=cnt;
			 res[j]+=0.5*owp[j];
		 }

		 for(j=0;j<n;++j) {
			 cnt=dtmp=0;
			 for(k=0;k<n;++k) {
				 if( data[j][k]!='.' ) dtmp+=owp[k],++cnt;
			 }
			 res[j]+=0.25*(dtmp/cnt);
		 }

		 printf("Case #%d:\n",i);
		 for(j=0;j<n;++j) {
			 printf("%.7lf\n",res[j]);
		 }
	 }







			 



     
     return 0;
}