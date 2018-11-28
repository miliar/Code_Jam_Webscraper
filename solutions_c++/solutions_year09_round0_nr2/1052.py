#include<iostream>
using namespace std;

int ar[200][200];
char ans[200][200];
int crnx,crny,crnt,T,tc,i,j,N,M;
char z;

char dfs(int x, int y) {
	if(ans[x][y]!='-') return ans[x][y];
	crnx=x; crny=y; crnt=ar[x][y];
	//cek utara
	if(ar[x-1][y]<crnt) {
		crnt=ar[x-1][y]; crnx=x-1; crny=y;
	}
	//cek barat
	if(ar[x][y-1]<crnt) {
		crnt=ar[x][y-1]; crnx=x; crny=y-1;
	}
	//cek timur
	if(ar[x][y+1]<crnt) {
		crnt=ar[x][y+1]; crnx=x; crny=y+1;
	}
	//cek selatan
	if(ar[x+1][y]<crnt) {
		crnt=ar[x+1][y]; crnx=x+1; crny=y;
	}
	if(crnt==ar[x][y]) {
		ans[x][y]=z;
		z++;
	}
	else ans[x][y]=dfs(crnx,crny);
	return ans[x][y];
}

int main() {
	cin>>T;
	for(tc=1;tc<=T;tc++) {
		cin>>N>>M;
		for(i=0;i<=N+1;i++) {
			for(j=0;j<=M+1;j++) ar[i][j]=2000000000;
		}
		for(i=1;i<=N;i++) {
			for(j=1;j<=M;j++) {
				cin>>ar[i][j];
				ans[i][j]='-';
			}
		}
		cout<<"Case #"<<tc<<":"<<endl;
		z='a';
		for(i=1;i<=N;i++) {
			for(j=1;j<=M;j++) {
				if(j>1) cout<<" ";
				cout<<dfs(i,j);
			}
			cout<<endl;
		}
	}
	return 0;
}
