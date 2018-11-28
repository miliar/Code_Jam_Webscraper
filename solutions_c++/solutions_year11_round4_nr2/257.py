#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int i,j,k,l,m,n,t,tt,ttt,ii,jj,y,d;
int ww[105];
int w,x,s,r,a,b,sum,ss,c;
char mass[12][12];

int main(){
	//freopen("c:/input.txt","r",stdin);
	freopen("c:/output.txt","w",stdout);
	
	cin>>ttt;
	while(ttt--){
		tt++;
		cout<<"Case #"<<tt<<": ";
		cin>>r>>c>>d;
		for (i=0;i<r;i++)
			for (j=0;j<c;j++)
				cin>>mass[i][j];
		int ans=0;
		for (k=min(r,c);k>=3;k--)
			for (i=0;i<=r-k;i++)
				for (j=0;j<=c-k;j++){
					x=2*i+k;
					y=2*j+k;
					int massx=0, massy=0;
					for (ii=i;ii<i+k;ii++)
						for (jj=j;jj<j+k;jj++)
							if (!((ii==i && jj==j)|| (ii==i && jj==j+k-1) || (ii==i+k-1 && jj==j) || (ii==i+k-1 && jj==j+k-1))){
								massx+=(x-2*ii-1)*(d+mass[ii][jj]-'0');
								massy+=(y-2*jj-1)*(d+mass[ii][jj]-'0');
							}
					if (massx==0 && massy==0 && ans==0) ans=k;
				}
		if (ans) cout<<ans<<endl; else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}