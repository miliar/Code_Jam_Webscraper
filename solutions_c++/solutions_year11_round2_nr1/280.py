#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<fstream>
#include<sstream>

using namespace std;




int main(){
	int tn;cin>>tn;
	for(int ttn=1;ttn<=tn;ttn++){
		cout<<"Case #"<<ttn<<":"<<endl;
		int n;cin>>n;
		string ss[1000];
		for(int i=0;i<n;i++)cin>>ss[i];
		int wn[1000];memset(wn,0,sizeof(wn));
		int ln[1000];memset(ln,0,sizeof(ln));
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(ss[i][j]=='1')wn[i]++;
				if(ss[i][j]=='0')ln[i]++;
			}
		}
		double wp[1000];
		for(int i=0;i<n;i++)wp[i]=(double)wn[i]/(double)(wn[i]+ln[i]);
		//for(int i=0;i<n;i++)cout<<wp[i]<<' ';cout<<endl; 
		double owp[1100];
		for(int i=0;i<n;i++){
			double ans=0.0;
			for(int j=0;j<n;j++)if(ss[i][j]!='.'){
				int ww=0;
				int ll=0;
				for(int l=0;l<n;l++)if(l!=i){
					if(ss[j][l]=='1')ww++;
					if(ss[j][l]=='0')ll++;
				}
				ans+=(double)ww/(double)(ww+ll);
			}
			ans/=(double)(wn[i]+ln[i]);
			owp[i]=ans;
		}
		//for(int i=0;i<n;i++)cout<<owp[i]<<' ';cout<<endl; 
		double oowp[1100];
		for(int i=0;i<n;i++){
			double tmp=0.0;
			for(int j=0;j<n;j++){
				if(ss[i][j]!='.')tmp+=owp[j];
			}
			tmp/=(double)(wn[i]+ln[i]);
			oowp[i]=tmp;
		}
		//for(int i=0;i<n;i++)cout<<oowp[i]<<' ';cout<<endl; 
		for(int i=0;i<n;i++){
			printf("%.10f\n",(0.25*wp[i]+0.50*owp[i]+0.25*oowp[i]));
		}
	}
	return 0;
}
