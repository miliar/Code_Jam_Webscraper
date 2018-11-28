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
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	vector<long long> v(31);
	v[1]=1;
	for(int i=2;i<=30;i++) {
		v[i]=(v[i-1]*2)+1;
	}
	int tests;
	fin>>tests;
	for(int test=1;test<=tests;test++){
		int a,b;
		fin>>a>>b;
		fout<<"Case #"<<test<<": ";
		if(b%(v[a]+1)==v[a]) fout<<"ON"<<endl;
		else fout<<"OFF"<<endl;
	}
	system("pause");
}
