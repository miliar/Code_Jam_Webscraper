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

ifstream fin("arxiu.in");
ofstream fout("arxiu.out");

int main() {
	int l,d,n;
	fin>>l>>d>>n;
	VS p(d);
	for(int i=0;i<d;i++) fin>>p[i];
	for(int cas=1;cas<=n;cas++){
		string s;
		fin>>s;
		VVB v(l,26);
		bool bb=false;
		int cont=0;
		for(int i=0;i<s.size();i++){
			if(s[i]=='(') bb=true;
			if(s[i]==')') bb=false;
			if(s[i]>='a' && s[i]<='z') v[cont][s[i]-'a']=true;
			if(!bb) cont++;
		}
		int comptador=0;
		for(int i=0;i<d;i++){
			bool b=true;
			for(int j=0;j<l;j++){
				if(!v[j][p[i][j]-'a']) 	{b=false; break;}
			}
			if(b) comptador++;
		}
		fout<<"Case #"<<cas<<": "<<comptador<<endl;
	}
}
