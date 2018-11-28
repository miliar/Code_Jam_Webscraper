#include <cstdio>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>

#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair <int,int> pii;
typedef map <string,int> msi;

int main(){
	int i,j,k,t,tt;
	scanf("%d",&tt);
	for(t=1;t<=tt;t++){
		int n;
		cin>>n;
		double opp[n],wp[n],owp[n],oowp[n],rpi[n];
		int owpn[n],oown[n],wins;
		char ch[n][n];
		for(i=0;i<n;i++){
			opp[i]=0;
			wins=0;
			for(j=0;j<n;j++){
				cin>>ch[i][j];
				if(ch[i][j]!='.') opp[i]++;
				if(ch[i][j]=='1') wins++;
			}
			wp[i]=wins/opp[i];
//cout<<"wp:"<<wp[i]<<endl;

		}
		double oowpt;
		for(i=0;i<n;i++){
			double owpt=0;
			owpn[i]=0;
			for(j=0;j<n;j++){
				double owptt=0;
				double owpnn=0;
				if(i==j||ch[i][j]=='.') continue;
//				for(int ii=0;ii<n;ii++)
				for(k=0;k<n;k++){
					if(k!=i){	
						//owp[j]=wp[i]*opp[i]/(opp[i]-1);		
						if(ch[j][k]!='.') owpnn++;
						if(ch[j][k]=='1')
							owptt++;
					}
					
				}
				owpt+=(owptt/owpnn);
			//	if(i==1) cout<<"owp[b]="<<owpt<<endl;
				owpn[i]++;
			}
			//cout<<"before:"<<owpt<<"/"<<owpn[i]<<endl;
			owp[i]=owpt/owpn[i];
			//cout<<"owp"<<owp[i]<<endl;
		}
		for(i=0;i<n;i++){
			oowpt=0;
			oown[i]=0;
			for(j=0;j<n;j++)
				if(ch[i][j]!='.'){
					oowpt+=owp[j];
					oown[i]++;
				}
			oowp[i]=oowpt/oown[i];
			//cout<<"oowp"<<oowp[i]<<endl;
		}
		printf("Case #%d:\n",t);
		for(i=0;i<n;i++){
			rpi[i]=(0.25)*(wp[i]+oowp[i])+(0.5)*owp[i];
			printf("%.12lf\n",rpi[i]);
		}

	}
	return 0;
}
