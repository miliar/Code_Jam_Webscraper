#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<memory.h>
#include<iomanip>
#include<cmath>
#include<fstream>
#include<map>
#include<ctime>
#include<queue>
#include<set>
#include<vector>
using namespace std;

char mp[105][105];
double rpi[105],wp[105],owp[105],oowp[105];

int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int t,n,i,j,c;
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		cin>>n;
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				cin>>mp[i][j];
			}
		}
		for(i=1;i<=n;i++){
			int k=0,p=0;
			for(j=1;j<=n;j++){
				if(mp[i][j]=='.') continue;
				if(mp[i][j]=='1') p++;
				k++;
			}
			wp[i]=p*1.0/k;
		}
		for(c=1;c<=n;c++){
			double ans=0;
			int kk=0;
			for(i=1;i<=n;i++){
				if(mp[i][c]!='.'){
					int k=0,p=0;
					for(j=1;j<=n;j++){
						if(j==c || mp[i][j]=='.') continue;
						if(mp[i][j]=='1') p++;
						k++;
					}
					ans+=p*1.0/k;
					kk++;
				}
			}
			owp[c]=ans/kk;
		}
		for(c=1;c<=n;c++){
			double ans=0;
			int kk=0;
			for(i=1;i<=n;i++){
				if(mp[i][c]!='.'){
					ans+=owp[i];
					kk++;
				}
			}
			oowp[c]=ans/kk;
		}
		cout<<"Case #"<<cas<<':'<<endl;
		for(i=1;i<=n;i++){
			rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
			cout<<rpi[i]<<endl;
		}
	}
	return 0;
}
		

			




