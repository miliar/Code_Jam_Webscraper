#include<iostream>
using namespace std;

int T,t,P,i,j,k,fare[15][2000],dp[15][2000][15],miss[15][2000];

int beli(int y, int x, int mis) {
	if(y<0) return 0;
	if(dp[y][x][mis]<2000000000) return dp[y][x][mis];
	dp[y][x][mis]=fare[y][x]+beli(y-1,2*x,mis)+beli(y-1,2*x+1,mis);
	if(miss[y][x]>mis) {
		dp[y][x][mis]=min(dp[y][x][mis],beli(y-1,2*x,mis+1)+beli(y-1,2*x+1,mis+1));
	}
	//cout<<y<<" "<<x<<" "<<mis<<": "<<dp[y][x][mis]<<endl;
	return dp[y][x][mis];
}

int main() {
	cin>>T;
	for(t=1;t<=T;t++) {
		cin>>P;
		for(i=0;i<(1<<P);i++) cin>>miss[0][i];
		for(i=0;i<(1<<P-1);i++) miss[0][i]=min(miss[0][2*i],miss[0][2*i+1]);
		for(i=0;i<P;i++) {
			for(j=0;j<(1<<(P-1-i));j++) {
				cin>>fare[i][j];
				for(k=0;k<=P;k++) {
					dp[i][j][k]=2000000000;
				}
			}
			if(i==0) continue;
			for(j=0;j<(1<<(P-1-i));j++) miss[i][j]=min(miss[i-1][j*2],miss[i-1][j*2+1]);
		}
		cout<<"Case #"<<t<<": "<<beli(P-1,0,0)<<endl;
		/*
		cout<<"miss: "<<endl;
		for(i=0;i<P;i++) {
			for(j=0;j<(1<<(P-1-i));j++) {
				cout<<miss[i][j]<<" ";
			}
			cout<<endl;
		}
		cout<<"fare: "<<endl;
		for(i=0;i<P;i++) {
			for(j=0;j<(1<<(P-1-i));j++) {
				cout<<fare[i][j]<<" ";
			}
			cout<<endl;
		}
		*/
	}
}
