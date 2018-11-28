#include<iostream>
#include<vector>
#include<set>
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

char map[501][501];

int main(){
	int tn;cin>>tn;
	for(int ttn=1;ttn<=tn;ttn++){
		cout<<"Case #"<<ttn<<": ";
		int c,r,d;cin>>c>>r>>d;
		for(int i=0;i<c;i++)cin>>map[i];
		int ans=-1;
		for(int i=min(r,c);i>=3;i--){
			for(int j=0;j<c-i+1;j++){ 
				for(int k=0;k<r-i+1;k++){
					//cout<<i<<j<<k<<endl;
					int f=0;
					double xmas=0;
					double ymas=0;
					double posix,posiy;
					if(i%2)posix=(i/2)+0.5;
					else posix=(i/2);
					if(i%2)posiy=(i/2)+0.5;
					else posiy=(i/2);
					for(int l=0;l<i;l++){
						for(int m=0;m<i;m++){
							if((l==0) && (m==0))continue;
							if((l==i-1) && (m==0))continue;
							if((l==0) && (m==i-1))continue;
							if((l==i-1) && (m==i-1))continue;
							xmas+=(((double)l+0.5)-posix)*(double)(map[j+l][k+m]-'0'+d);
							ymas+=(((double)m+0.5)-posiy)*(double)(map[j+l][k+m]-'0'+d);
						}
					}
					//cout<<xmas<<' '<<ymas<<endl;
					if(xmas==0.0 && ymas==0.0){
						f=1;
						ans=i;
					}
					if(f)goto gogo;
				}
			}
		}
		gogo:;
		if(ans==-1)cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}
