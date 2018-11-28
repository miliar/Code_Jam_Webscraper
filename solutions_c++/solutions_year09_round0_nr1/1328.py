// Tim  defines
#include <vector> 
#include <queue> 
#include <set>
#include <map> 

#include <numeric>
#include <algorithm> 
#include <string.h> 

#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 

using namespace std;
//#pragma comment(linker, "/STACK:20000000")

// useful defines
#define sz(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define Rep(i,n) for (int i=0;i<(n);++i)
#define RepV(i,v) for (int i=0;i<sz(v);++i)
#define Fill(a,b) memset(&a,b,sizeof(a))   
#define All(c) (c).begin(),(c).end() 
typedef long long LL;
typedef pair <int,int> PI;
typedef pair<double, double> PD;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <PI> VP;
const int oo = (1<<30);
const double eps = 1e-10;
const double INF = 1e10;

class TTree{
public:
	TTree * child[30];
	TTree(const string & s, int ind) {
		Rep(i,30)
			child[i] = NULL;
		if (ind >= sz(s)){
			return;
		}else{
			int tmp = s[ind]-'a';
			child[tmp] = new TTree(s, ind + 1);
		}
	}
	~TTree() {
		Rep(i,30)
			delete child[i];
	}

	void push(const string & s, int ind){
		if (ind > sz(s))
			return;
		int tmp = s[ind]-'a';
		if (child[tmp] == NULL ){
			child[tmp] = new TTree(s, ind + 1);
		}else{
			child[tmp]->push(s,ind+1);
		}
	}
};

int l, n, d, k;
TTree * root;
//char ss[20];
string s="";
string ss;
vector<TTree *> v, w;

void update(){
	w.clear();
	RepV(j,s){
		int tmp = s[j]-'a';
		RepV(i,v){
			if (v[i]->child[tmp] != NULL){
				w.push_back(v[i]->child[tmp]);
			}
		}
	}
	v.clear();
	v = w;
}


int main() { 
	freopen("AA.in","rt",stdin);
	freopen("AA.out","wt",stdout);
	scanf("%d%d%d\n",&l,&d,&n);
	root = new TTree(s,1);
	Rep(i,d){
		//scanf("%s\n", ss);
		//s = ss;
		cin>>s;
		root->push(s,0);
	}
	Rep(j,n){
		//scanf("%s\n", ss);
		cin >> ss;
		//int L = strlen(ss);		
		int L = ss.size();
		bool ok = 1;
		v.clear();
		v.push_back(root);
		s.clear();
		Rep(i,L){
			if (ss[i] == '('){
				ok = 0;
				continue;
			}
			if (ss[i] == ')'){
				ok = 1;
			} else s.push_back(ss[i]);
			if (ok){
				update();
				s.clear();
				if (!sz(v)) break;
			}
			
		}
		printf("Case #%d: %d\n",j+1,sz(v));
	}
//	Rep(i,26)
//		printf("%c",char(i+'a'));

	delete root;
	return 0;
}


