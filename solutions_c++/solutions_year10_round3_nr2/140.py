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
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	long long tests,L,P,C;
	fin>>tests;
	for(int t=1;t<=tests;t++){
		fin>>L>>P>>C;
		vector<int> v(5);
		for(int i=0;i<5;i++) v[i]=-1;
		v[0]=C;
		for(int i=1;i<5;i++){
			if(v[i-1]>=31623) break;
			v[i]=v[i-1]*v[i-1];
		}
		int res=5;
		for(int i=0;i<5 && res==5;i++){
			if(v[i]==-1 || v[i]*L>=P) res=i;
		}
		fout<<"Case #"<<t<<": "<<res<<endl;
	}
	system("pause");
}
