
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main(){
	int nn;scanf("%d",&nn);
	for(int npr=1;npr<=nn;npr++){
		int n;scanf("%d",&n);
		char buf[n][n+2];
		for(int i=0;i<n;i++)scanf("%s",buf[i]);
		for(int i=0;i<n;i++)buf[i][i]='.';
		double cnt[n];memset(cnt,0,sizeof(cnt));
		double win[n];memset(win,0,sizeof(win));
		for(int i=0;i<n;i++)for(int k=0;k<n;k++)cnt[i]+=(buf[i][k]!='.');
		for(int i=0;i<n;i++)for(int k=0;k<n;k++)win[i]+=(buf[i][k]=='1');
		double wp[n];
		for(int i=0;i<n;i++)wp[i]=win[i]/cnt[i];
		double wp2[n][n];
		for(int i=0;i<n;i++)for(int k=0;k<n;k++){
			wp2[i][k]=(win[i]-(buf[i][k]=='1'))/(cnt[i]-(buf[i][k]!='.'));
		}
		double owp[n];memset(owp,0,sizeof(owp));
		for(int i=0;i<n;i++){
			for(int k=0;k<n;k++)if(buf[i][k]!='.')owp[i]+=wp2[k][i];
			owp[i]/=cnt[i];
		}
		double oowp[n];memset(oowp,0,sizeof(oowp));
		for(int i=0;i<n;i++){
			for(int k=0;k<n;k++)if(buf[i][k]!='.')oowp[i]+=owp[k];
			oowp[i]/=cnt[i];
		}

#if 0 
		for(int i=0;i<n;i++)cout<<"wp["<<i<<"]="<<wp[i]<<endl;
		for(int i=0;i<n;i++)cout<<"owp["<<i<<"]="<<owp[i]<<endl;
		for(int i=0;i<n;i++)cout<<"oowp["<<i<<"]="<<oowp[i]<<endl;
#endif

		printf("Case #%d:\n",npr);
		for(int i=0;i<n;i++)printf("%.15lf\n",wp[i]/4+owp[i]/2+oowp[i]/4);
	}
	return 0;
}
