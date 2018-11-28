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
	int tests;
	fin>>tests;
	for(int t=1;t<=tests;t++){
		int n;
		fin>>n;
		vector<PII> v(n);
		for(int i=0;i<n;i++) fin>>v[i].first>>v[i].second;
		sort(v.begin(),v.end());
		int cont=0;
		for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if(v[j].second<v[i].second) cont++;
		fout<<"Case #"<<t<<": "<<cont<<endl;
	}
	system("pause");
}
