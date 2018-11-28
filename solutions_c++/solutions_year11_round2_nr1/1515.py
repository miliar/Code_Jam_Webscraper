#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>

using namespace std;

int main(){
	
	int T;
	cin>>T;
	for(int testcase=1;testcase<=T;testcase++){
		int N;
		cin>>N;
		vector<string> data(N);
		for(int i=0;i<N;i++)
			cin>>data[i];
		int R=data[0].size();
		
		vector<double> WP(N),WPK(N),WPC(N),OWP(N),OOWP(N),ans(N);
		
		for(int i=0;i<N;i++){
			double k,c;
			k=0,c=0;
			for(int j=0;j<R;j++){
				if(data[i][j]=='1')
					k++;
				if(data[i][j]!='.')
					c++;
			}
			WP[i]=k/c;
			WPK[i]=k;
			WPC[i]=c;
		}
		for(int i=0;i<N;i++){
			double k,c;
			k=0,c=0;
			for(int j=0;j<N;j++){
				if(i!=j&&data[i][j]!='.'){
					if(data[j][i]=='1'){
						k+=(WPK[j]-1.0)/(WPC[j]-1.0);
						c++;
					}else if(data[j][i]=='0'){
						k+=(WPK[j])/(WPC[j]-1.0);
						c++;
					}else{
						k+=(WPK[j])/(WPC[j]);
						c++;
					}
				}
			}
			OWP[i]=k/c;
		}
		for(int i=0;i<N;i++){
			double k,c;
			k=0,c=0;
			for(int j=0;j<N;j++){
				if(i!=j&&data[i][j]!='.'){
					k+=OWP[j];
					c++;
				}
			}
			OOWP[i]=k/c;
		}
		
		for(int i=0;i<N;i++)
			ans[i]=0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
		printf("Case #%d:\n",testcase);
		for(int i=0;i<N;i++)
			printf("%.8lf\n",ans[i]);
	}
	return 0;
}
