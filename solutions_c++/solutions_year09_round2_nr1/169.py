
#pragma comment(linker,"/STACK:64000000")

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <bitset>
#include <sstream>
#include <cmath>
#include <ctime>

#define WR printf
#define RE scanf
#define FOR(i,Be,En) for(i=(Be);i<=(En);++i)
#define DFOR(i,Be,En) for(i=(Be);i>=(En);--i)
#define PB push_back
#define SZ(a) (int)((a).size())
#define FIT(i,v) for(i=(v).begin();i!=(v).end();i++)
#define RFIT(i,v) for(i=(v).rbegin();i!=(v).rend();i++)
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define SE second
#define FI first
#define CLR(a) memset(a,0,sizeof(a))
#define LL long long
using namespace std;
typedef vector<int>    VI;
typedef vector<string> VS;
typedef pair<int ,int> PAR;


int T;
PAR graf[1000000];
string fe[1000000];
double pr[1000000];
int n;
void init()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	RE("%d",&T);
}
int read(stringstream & ss, int & n){
	//if (n>105000) {WR("gg"); exit(0);}
	int cn = n++;
	string s;
	ss >> s >> pr[cn];
	ss >> s;
	if (s==")") {
		fe[cn] = "???%%%";
		graf[cn] = make_pair(-1,-1);
	} else {
		fe[cn] = s;
		graf[cn].FI = read(ss, n);
		graf[cn].SE = read(ss, n);
		ss >> s;
	}
	return cn;
}
void sol(){
	int t, ls, i, a, j;
	FOR(t,1,T){
		RE("%d\n",&ls);
		string s, hs;
		FOR(i,1,ls){
			getline(cin, hs);
			s = s  + hs;
		}
		for(i=0;i<SZ(s);i++) if (s[i]=='(' || s[i]==')') s.insert(i+1," ");
		reverse(s.begin(), s.end());
		for(i=0;i<SZ(s);i++) if (s[i]==')' || s[i]=='(') s.insert(i+1," ");
		reverse(s.begin(), s.end());
		//cout << s;
		
		//cout << s << endl;
		
		
		n = 0;
		stringstream ss(s);
		read(ss, n);
		
		//WR("\n");
		//FOR(i,0,n-1) WR("%.5lf %s %d %d\n",pr[i], fe[i].c_str(), graf[i].FI, graf[i].SE);
		
		RE("%d",&a);
		if (t>1) WR("\n");
		WR("Case #%d:",t);
		FOR(i,1,a){
			string name;
			int cc;
			set<string>  m;
			cin >> name >> cc;
			FOR(j,1,cc) {
				cin >> name;
				m.insert(name);
			}
			double curp = 1.;
			int curn = 0;
			while (n>0){
				curp*=pr[curn];
				if (graf[curn].FI==-1) break;
				if (m.find(fe[curn])!=m.end()) curn = graf[curn].FI;
				else curn = graf[curn].SE;
			}
			WR("\n%.8lf",curp);
		}
	}
}
int main()
{
	init();
	sol();
	return 0;
}