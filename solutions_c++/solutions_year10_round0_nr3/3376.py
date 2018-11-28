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


int main() {
	ifstream fin("C-small3.in");
	ofstream fout("C-small3.out");
	int tests,R,k,n,RR;
	long long cont=0;
	fin>>tests;
	for(int test=1;test<=tests;test++){
		cont=0;
		fin>>n>>R>>k;
		int nn=n;
		VI v(k);
		for(int i=0;i<k;i++) fin>>v[i];
		int times=0;
		int g=0;
		while((g!=0 || cont==0) && times<n){
			RR=0;
			int gi=g;
			while(RR+v[g]<=R) {
				RR+=v[g];
				g++;
				if(g==v.size()) g=0;
				if(gi==g) break;
			}
			cont+=RR;
			times++;
		}
		debug(cont);
		debug(n);
		debug(times);
		cont=cont*(int(n/times));
		debug(cont);
		n%=times;
		times=0;
		while(times<n){
			RR=0;
			int gi=g;
			while(RR+v[g]<=R) {
				RR+=v[g];
				g++;
				if(g==v.size()) g=0;
				if(gi==g) break;
			}
			cont+=RR;
			times++;
		}
		fout<<"Case #"<<test<<": "<<cont<<endl;
	}
	system("pause");
}
