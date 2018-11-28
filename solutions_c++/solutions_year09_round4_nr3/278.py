#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int n,k;
		cin>>n>>k;
		int s[n][k];
		for(int j=0;j<n;j++)
			for(int l=0;l<k;l++){
				cin>>s[j][l];
			}
		int w[101][101];
		memset(w,0,sizeof w);
		for(int j=0;j<n;j++)
			for(int l=0;l<n;l++){
				bool f=true;
				for(int m=0;m<k;m++)
					if(s[j][m]<=s[l][m]){
						f=false;
						break;
					}
				if(f)
					w[j][l]=1;
			}
		//for(int j=0;j<n;j++) for(int l=0;l<n;l++)cerr<<w[i][j];
		//cerr<<endl;
		int lx[101],ly[101],cx[101],cy[101];
		int qx[101],qy[101];
		int ans=0;
		memset(cx,255,sizeof cx);
		memset(cy,255,sizeof cy);
		while(1){
			memset(lx,255,sizeof lx);
			memset(ly,255,sizeof ly);
			int qxl=0,qyl=0;
			int a=-1;
			for(int i=0;i<n;i++)
				if(cx[i]==-1)
					qx[qxl++]=i;
			bool f;
			do{
				f=false;
				for(int i=0;i<qxl;i++){
					for(int j=0;j<n;j++)
						if(w[qx[i]][j]==1 && ly[j]==-1){
							ly[j]=qx[i];
							qy[qyl++]=j;
							//cerr<<"y: "<<j<<endl;
							f=true;
						}
				}
				if(!f)
					break;
				f=false;
				for(int i=0;i<qyl;i++){
					if(cy[qy[i]]==-1){
						a=qy[i];
						break;
					}
					else if(lx[cy[qy[i]]]==-1){
						lx[cy[qy[i]]]=qy[i];
						qx[qxl++]=cy[qy[i]];
						//cerr<<"x: "<<cy[qy[i]]<<endl;
						f=true;
					}
				}
			}while(f);
			if(a==-1)
				break;
			else{
				while(a!=-1){
					int b=ly[a];
					cy[a]=b;
					cx[b]=a;
					w[b][a]=0;
					a=lx[b];
					if(a!=-1)
						w[b][a]=1;
				}
				ans++;
			}
		}
		cout<<"Case #"<<i<<": "<<n-ans<<endl;
	}
}