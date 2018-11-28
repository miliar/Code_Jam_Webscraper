#define _CRT_SECURE_NO_WARNINGS
#include <map> 
#include <set> 
#include <queue> 
#include <bitset> 
#include <valarray> 
#include <complex> 
#include <iostream> 
#include <sstream> 
#include <cmath> 
#include <algorithm> 
#include <string> 
#include <cassert>
#include <ctime>
#include <float.h>
#include <string>
#include <cstring>

#ifdef _MSC_VER
#pragma comment(linker,"/STACK:20000000")
#endif

using namespace std;

// prewritten code

#define Size(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define RepV(i,v) for (int i=0;i<Size(v);++i)
#define All(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define Abs(a) ((a)<0?-(a):(a))
#define VVI vector<vector<int> >
#define VI vector<int>
#define VVS vector<vector<string> >
#define VS vector<string>
#define ForEach(it,a) for (typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)
#define DBG(x) cout << #x <<" = "<< x << endl;
#define DBGA(x) {cout << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cout<<x[i]<<' '; cout<<endl;}
#define DBGV(x) {cout << #x <<": "; for (int i=0; i<(int)Size(x); ++i) cout<<x[i]<<' '; cout<<endl;}

const string problem_name = "1";

string tree;

int k, m;
double wh[1000000];
int mate[1000000][3];
string f[1000000];

bool is_whitespace(char c){
	return c==' ' || c=='\n';
}

void build_tree(int parent){
	while (is_whitespace(tree[k])) ++k;
	assert(tree[k]=='(');
	++k;
	while (is_whitespace(tree[k])) ++k;
	string w="";
	while ((tree[k]>='0' && tree[k]<='9') || tree[k]=='.'){
		w += tree[k];
		++k;
	}
	while (is_whitespace(tree[k])) ++k;
	stringstream ss; ss << w;
	++m;
	ss >> wh[m];
	f[m] = "";
	mate[parent][++mate[parent][0]] = m;
	if (tree[k]!=')'){
		while (tree[k]>='a' && tree[k]<='z') {
			f[m] += tree[k];
			++k;
		}
		int cur=m;
		build_tree(cur);
		build_tree(cur);
		while (is_whitespace(tree[k])) ++k;
		++k;
	} else ++k;
}

double go(int u, vector<string> &v){
	if (f[u] == "") return wh[u];
	bool ok=false;
	RepV(i,v) if (v[i]==f[u]) {ok=true; break;}
	if (ok) return wh[u]*go(mate[u][1], v);
	else return wh[u]*go(mate[u][2], v);
}

void solve_case(){
	Fill(mate,0);
	int l;
	scanf("%d\n",&l);
	tree="";
	For(i,1,l){
		string s;
		getline(cin,s);
		tree += s;
	}
	k=0; m=0; wh[0]=1;
	build_tree(0);
	int a;
	scanf("%d\n",&a);
	For(i,1,a) {
		string s, name;
		int cnt;
		getline(cin,s);
		stringstream ss;
		ss << s;
		vector<string> v;
		ss >> name >> cnt;
		For(j,1,cnt) {
			string tmp;
			ss >> tmp;
			v.push_back(tmp);
		}
		printf("%.8lf\n",go(1,v));
	}
}

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int _t;
	scanf("%d\n",&_t);
	
	For(_z,1,_t){
		printf("Case #%d:\n",_z);
		
		solve_case();
		
		fflush(stdout);
	}
	
	return 0;
}
