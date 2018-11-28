#include <fstream>
using namespace std;
int in[101][101];
char out[101][101];
int a,b;

bool amimin(int oldm, int oldn, int m, int n){
	int min=in[m][n];
	int minm = m, minn = n;
	if(m-1>=0 && in[m-1][n] < min){
		min=in[m-1][n];
		minm = m-1;
		minn = n;
	}
	if(n-1>=0 && in[m][n-1] < min){
		min=in[m][n-1];
		minm = m;
		minn = n-1;
	}
	if(n+1<b && in[m][n+1] < min){
		min=in[m][n+1];
		minm = m;
		minn = n+1;
	}
	if(m+1<a && in[m+1][n] < min){
		min=in[m+1][n];
		minm = m+1;
		minn = n;
	}
	return (minm==oldm && minn==oldn);
}

void findnext(int &m, int &n){
	for(int i=0;i<a;i++){
		for(int j=0;j<b;j++){
			if(out[i][j]==0){
				m=i;
				n=j;
				return;
			}
		}
	}
}

void solve(int m, int n, char alpha){
	out[m][n] = alpha;
	//만약 주위에 더 낮은 곳이 있으면 최소높이를 찾는다
	int min=in[m][n];
	int minm = m, minn = n;
	if(m-1>=0 && in[m-1][n] < min){
		min=in[m-1][n];
		minm = m-1;
		minn = n;
	}
	if(n-1>=0 && in[m][n-1] < min){
		min=in[m][n-1];
		minm = m;
		minn = n-1;
	}
	if(n+1<b && in[m][n+1] < min){
		min=in[m][n+1];
		minm = m;
		minn = n+1;
	}
	if(m+1<a && in[m+1][n] < min){
		min=in[m+1][n];
		minm = m+1;
		minn = n;
	}
	// 내려갈곳이 아직 체크되어있지 않으면 내려가라
	if(!(minm == m && minn == n) && out[minm][minn]==0){
		solve(minm, minn, alpha);
	}
	// 올라갈곳 있는지 찾아보자
		bool finish=true;
		if(m-1>=0 && amimin(m,n,m-1, n) && out[m-1][n]==0){
			finish=false;
			solve(m-1, n, alpha);
		}
		if(n-1>=0 && amimin(m,n,m, n-1) && out[m][n-1]==0){
			finish=false;
			solve(m, n-1, alpha);
		}
		if(n+1<b && amimin(m,n,m, n+1) && out[m][n+1]==0){
			finish=false;
			solve(m, n+1, alpha);
		}
		if(m+1<a && amimin(m,n,m+1, n) && out[m+1][n]==0){
			finish=false;
			solve(m+1, n, alpha);
		}
}

int main(){
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("B-large.out");
	int t;
	fin>>t;
	for(int ci=1;ci<=t;ci++){
		//초기화
		for(int i=0;i<101;i++){
			for(int j=0;j<101;j++){
				in[i][j] = 0;
				out[i][j] = 0;
			}
		}
		//입력
		fin>>a>>b;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				fin>>in[i][j];
			}
		}
		char alpha='a';
		while(1){
			int newm=-1, newn=-1;
			findnext(newm, newn);
			if(newm == -1 && newn == -1) break;
			else{
				solve(newm, newn, alpha);
				alpha++;
			}
		}
		//print
		fout<<"Case #"<<ci<<":"<<endl;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				fout<<out[i][j];
				if(j!=b-1) fout<<" ";
			}
			fout<<endl;
		}
	}
}