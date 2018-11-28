//Done by Grey Matter
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

ifstream fin("Csmall2.in");
ofstream fout("Csmall2.out");


int main() {
	int tests;
	fin>>tests;
	for(int test=1;test<=tests;test++){
		debug(test);
		int r;
		fin>>r;
		VS v(100);
		for(int i=0;i<100;i++) for(int j=0;j<100;j++) v[i]+="0000000000";
		int bacteria=0;
		for(int k=0;k<r;k++){
			int xi,yi,xf,yf;
			fin>>xi>>yi>>xf>>yf;
			bacteria+=(xf-xi)*(yf-yi);
			for(int i=yi-1;i<yf;i++) for(int j=xi-1;j<xf;j++) v[i][j]='1';
		}
		int cont=0;
		for(int i=0;i<100;i++){
			for(int j=0;j<100;j++) if(v[i][j]=='1') cont++;
		}
		cerr<<bacteria<<' '<<cont<<endl;
		bacteria=cont;
		int torn=0;
//		debug(bacteria);
		while(bacteria){
//			debug(torn);
//			debug(bacteria);
			if(torn==200){
/*				for(int i=0;i<100;i++){
					cerr<<v[i]<<endl;
				}*/
//				for(int i=0;i<100;i++) for(int j=0;j<100;j++) if(v[i][j]=='1') cerr<<i<<' '<<j<<",   ";
//				system("pause");
			}
//			system("pause");
			for(int i=99;i>=1;i--){
				for(int j=99;j>=1;j--){
					if(v[i][j]=='1'){
						if(v[i-1][j]=='0' && v[i][j-1]=='0'){
							bacteria--;
							v[i][j]='0';
						}
					}
					else {
						if(v[i-1][j]=='1' && v[i][j-1]=='1') {
							bacteria++;
							v[i][j]='1';
						}
					}
				}
			}
			for(int i=99;i>0;i--) {
				if(v[i][0]=='1' && v[i-1][0]=='0') {
					v[i][0]='0';
					bacteria--;
				}
				if(v[0][i]=='1' && v[0][i-1]=='0') {
					v[0][i]='0';
					bacteria--;
				}
			}
			if(v[0][0]=='1'){
				bacteria--;
				v[0][0]='0';
			}
			torn++;
		}
		fout<<"Case #"<<test<<": "<<torn<<endl;
	}
	system("pause");
}
