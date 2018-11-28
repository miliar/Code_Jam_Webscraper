//Done by sug
//Fet per Ferran Alet

#include<iostream>
#include<cmath>
#include<iomanip>
#include<vector>
#include<map>
#include<queue>
#include<fstream>
#include<algorithm>
#include<string>
#include<stack>
#include<numeric>
#include<set>
#include<sstream>

#define INF 2147483647
#define LINF 1000000000000000000LL
#define EPS 1e-9
#define debug(x) cerr << #x << " = " << x << endl
#define FORN(x,y) for(int x=0;x<y;x++)
#define FORU(x,y) for(int x=1;x<=y;x++)
using namespace std;


typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef MII::iterator iMII;
typedef long long ll;

int jefazo(int n,VI &jef){
	if(jef[n]==-1) return n;
	return jef[n]=jefazo(jef[n],jef);
}

ifstream fin("B.in");
ofstream fout("B.out");

int main() {
	int casos;
	fin>>casos;
	for(int cas=1;cas<=casos;cas++){
		int a,b;
		fin>>a>>b;
		VVI v(a,b);
		for(int i=0;i<a;i++) for(int j=0;j<b;j++) fin>>v[i][j];
		VI jef(a*b);
		for(int i=0;i<jef.size();i++) jef[i]=-1;
		for(int i=0;i<a;i++) {
			for(int j=0;j<b;j++){
				int minim=v[i][j];
					int direction=-1;
					int iii;
					int jjj;
					int xs[]={-1,0,0,1};
					int ys[]={0,-1,1,0};
					for(int k=0;k<4;k++){
						int ii=i+xs[k];
						int jj=j+ys[k];
						if(ii>=0 && ii<a && jj>=0 && jj<b && v[ii][jj]<minim){
							minim=v[ii][jj];
							iii=ii;
							jjj=jj;
							direction=k;
						}
					}
					if(direction!=-1){
						if(jefazo((iii*b)+jjj,jef)<jefazo((i*b)+j,jef)) jef[jefazo((i*b)+j,jef)]=jefazo((iii*b)+jjj,jef);
						else jef[jefazo((iii*b)+jjj,jef)]=jefazo((i*b)+j,jef);
					}
			}
		}
		int cont=-1;
		map<int,int> M;
		fout<<"Case #"<<cas<<':'<<endl;
		for(int i=0;i<a;i++) {
			for(int j=0;j<b;j++){
				if(j) fout<<' ';
				if(jefazo((i*b)+j,jef)==(i*b)+j) {
					cont++;
					M[(i*b)+j]=cont;
				}
				fout<<char(M[jefazo((i*b)+j,jef)]+'a');
			}
			fout<<endl;
		}
	}
}
