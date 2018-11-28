#include<iostream>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int maxn=13;
int x[maxn][1<<maxn],f[maxn][1<<maxn][maxn],m[1<<maxn],n,p,i,j,k,ca,ti;
int main(){
	freopen("b1.in","r",stdin);
	freopen("b1.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>p;
		n=1<<p;
		fr(i,1,n)
			cin>>m[i];
		fr(i,1,p)
			fr(j,1,1<<(p-i))
				cin>>x[i][j];
		memset(f,60,sizeof(f));
		fr(i,1,n)
			fr(j,0,m[i])
				f[0][i][j]=0;
		fr(i,1,p)
			fr(j,1,1<<(p-i)){
				fr(k,0,p){
					f[i][j][k]<?=f[i-1][j*2-1][k]+f[i-1][j+j][k]+x[i][j];
					if(k)
						f[i][j][k-1]<?=f[i-1][j*2-1][k]+f[i-1][j+j][k];
				}
				for(k=p;k>=1;k--)
					f[i][j][k-1]<?=f[i][j][k];
			}
		cout<<"Case #"<<ti<<": "<<f[p][1][0]<<endl;	
	}
}