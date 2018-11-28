#include <fstream>

using namespace std;
ifstream fin("C-small.in");
ofstream fout("C-small.out");
const int MNAX = 100;
int ans = 0;
int a[MNAX+2][MNAX+2];

int main(){
	int t,test;
	fin>>test;
	for (t=1;t<=test;++t){
		memset(a,0,sizeof(int)*(MNAX+2)*(MNAX+2));
		ans = 0;
		int bb=0;
		int i,j;
		int c;
		int n=0,m=0;
		fin>>c;
		for (i=1;i<=c;++i){
			int x1,x2,y1,y2;
			fin>>y1>>x1>>y2>>x2;
			n = max(n,x2);
			m = max(m,y2);
			for (int ii=x1;ii<=x2;++ii){
				for (int jj=y1;jj<=y2;++jj){
					a[ii][jj] = 1;
				}
			}
		}
			for (i=1;i<=n;++i){
				for (j=1;j<=m;++j){
					bb+=a[i][j];
				}
			}
		/*
			for (i=1;i<=n;++i){
				for (j=1;j<=m;++j){
					fout<<a[i][j];
				}
				fout<<'\n';
			}
				fout<<'\n';
*/		while (bb>0){
			for (i=n;i>=1;--i){
				for (j=m;j>=1;--j){
					if (a[i][j]==0 && a[i-1][j]==1 && a[i][j-1]==1){++bb; a[i][j] = 1;}
					else if (a[i][j]==1 && (a[i-1][j]==0 && a[i][j-1]==0)){--bb; a[i][j] = 0;}
				}
			}
			++ans;
/*			for (i=1;i<=n;++i){
				for (j=1;j<=m;++j){
					fout<<a[i][j];
				}
				fout<<'\n';
			}
				fout<<'\n';
*/		}

		fout<<"Case #"<<t<<": "<<ans<<'\n';
	}
}