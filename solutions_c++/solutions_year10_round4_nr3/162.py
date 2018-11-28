#include<iostream>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int maxn=502;
bool x[maxn][maxn];
int ca,ti,i,j,k,ans,n,x1,y1,x2,y2;
bool exist(){
	int i,j;
	fr(i,1,maxn-1)
		fr(j,1,maxn-1)
			if(x[i][j])
				return true;
	return false;
}
int main(){
	freopen("c0.in","r",stdin);
	freopen("c0.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		ans=0;
		memset(x,0,sizeof(x));
		cin>>n;
		fr(i,1,n){
			cin>>x1>>y1>>x2>>y2;
			fr(j,x1,x2)
				fr(k,y1,y2)
					x[j][k]=true;
		}
		while(exist()){
			ans++;
			for(i=maxn-1;i>=1;--i)
				for(j=maxn-1;j>=1;--j)
					if(x[i][j])
						x[i][j]=x[i-1][j]||x[i][j-1];
					else
						x[i][j]=x[i-1][j]&&x[i][j-1];
		}
		cout<<"Case #"<<ti<<": "<<ans<<endl;
	}
}