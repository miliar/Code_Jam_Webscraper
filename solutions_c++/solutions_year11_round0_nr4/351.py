#include<iostream>
using namespace std;
const int N=1001;
double f[N],g[N][N][2];
int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
/*	f[1]=0;
	for (int i=2;i<=1000;i++){
		g[i][i-1][0]=0;
		g[i][i-1][1]=1;
		for (int j=i-2;j>=0;j--){
			//g[i][j]=g[i][j+1]*(i-j-1)/(i-j);
			g[i][j][0]=g[i][j+1][0]*(i-j-1)/(i-j);
			g[i][j][1]=g[i][j+1][1]*(i-j-1)/(i-j);
			//g[i][j]+=(f[j+1]+f[i-(j+1)]-1)/(i-j);
			if (i-(j+1)==1)
				g[i][j][0]+=(f[j+1])/(i-j);
			else
				g[i][j][0]+=(f[j+1]+f[i-(j+1)]-1)/(i-j);
		}
		//f[i]=1+g[i][0];
		if (g[i][0][1]==1){
			cout<<i<<endl;
			return 0;
		}
		f[i]=(1+g[i][0][0])/(1-g[i][0][1]);
		cout<<i<<' '<<f[i]<<endl;
	}*/
	int Test;
	cin>>Test;
	for (int test=1;test<=Test;test++){
		int n;
		cin>>n;
		int ans=0;
		for (int i=0;i<n;i++){
			int j;
			cin>>j;
			if (i+1!=j)
				ans++;
		}
		cout<<"Case #"<<test<<": "<<ans<<".000000"<<endl;
	}
	return 0;
}
