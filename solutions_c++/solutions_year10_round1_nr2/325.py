#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
using namespace std;

int T, TT;
int f[150][300], a[150];
int D, I, m, n;
int i, temp,ans;
int now, nowd;
const int MAXX=1<<15;

int main(){
	freopen("b.in","r",stdin);
	freopen("b.txt","w",stdout);
	cin>>T;
	for(int TT=1; TT<=T; ++TT){
		for(int j=0; j<150; ++j)
			for(int k=0; k<300; ++k){
				f[j][k]=MAXX;	
			}
		cin>>D>>I>>m>>n;
		for(i=1; i<=n; ++i) cin>>a[i];
		i=1;
		f[i][a[i]]=0;
		

		for(int j=0; j<256; ++j){
			for(int k=0; k<256; ++k){
				if (k==j) continue;
				if (m!=0)
					{temp=f[i][j]+((labs(j-k)-1) / m +1)*I;	
					if (temp<f[i][k]) f[i][k]=temp;	}//I
				temp=f[i][j]+labs(j-k);
				if (temp<f[i][k]) f[i][k]=temp;		//3		
			}	
		}
		for(i=2; i<=n; ++i){
			f[i][a[i]]=D*(i-1);
			for(int k=0; k<256; ++k){
				nowd=labs(k-a[i]);	
			for(int j=k-m; j<=k+m; ++j){
				if (j>255) break;
				if (j<0) continue;
				temp=f[i-1][j]+nowd;
				if (temp<f[i][k]) f[i][k]=temp;	
			}	
		}
			for(int j=0; j<256; ++j){
				temp=f[i-1][j]+D;
				if (temp<f[i][j]) f[i][j]=temp;	//D
			}


		for(int j=0; j<256; ++j){
			for(int k=0; k<256; ++k){
				if (k==j) continue;
				if (m!=0)
					{temp=f[i][j]+((labs(j-k)-1) / m +1)*I;	
					if (temp<f[i][k]) f[i][k]=temp;	}//I
				temp=f[i][j]+labs(j-k);
				if (temp<f[i][k]) f[i][k]=temp;		//3		
			}	
		}
		//cout<<i<<" "<<f[i][40]<<endl;
			//
		}
		ans=MAXX;
		for(int j=0; j<256; ++j)
			if (ans>f[n][j]) ans=f[n][j];
		
		cout<<"Case #"<<TT<<": "<<ans<<endl;	
	}
//	cin>>T>>i>>D;
}
