#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>
 
using namespace std;

#define eps 1e-9
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()
#define mp make_pair
#define pb push_back

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))

typedef pair < int, int > pii;
typedef long long LL;
string s,stree;

struct Node{
	string name;
	double val;
	Node* dir, * esq;
};


map<string, map<string,int> >mymap;

double go(Node* tree, string ani,double prob){
	if(tree==NULL) return prob;
	prob*=tree->val;
	if(mymap[ani].find(tree->name)!=mymap[ani].end()){
		return go(tree->esq,ani,prob);
	}
	return go(tree->dir,ani,prob);	
}


int ind = 0;

Node* parse(){
	if(ind>=SZ(stree)) return NULL;
	
	//espacios despues del (
	
	while(stree[ind]==' '||stree[ind]=='(' || stree[ind]==')'){		
		ind++;		
	}
	
	//lee valor
	double val = 0;
	while(stree[ind]!='.'){
		val=val*10+stree[ind]-'0';
		ind++;				
	}
	ind++;
	
	double fact = 0.1;
	while(isalnum(stree[ind])){
		val+=(stree[ind]-'0')*fact;
		fact*=0.1;
		ind++;		
	}
	while(stree[ind]==' '){
		ind++;	
	}
	Node * node = new Node();
	node->val = val;
	if(stree[ind]==')'){
		ind++;
		node->name = "";
		node->esq=NULL;
		node->dir=NULL;
		return node;
	}
	while(isalpha(stree[ind])){
		node->name+=stree[ind++];
	}
	ind++;
	node->esq = parse();
	ind++;
	node->dir = parse();
	ind++;
	return node;
}
void run1(int caso){
	mymap.clear();
	Node * tree;
	int L;
	cin >>L;
	getline(cin,s);
	stree="";
	
	
	REP(i,L){
		getline(cin,s);	
		stree+=s;
	}
	ind=1;
	tree= parse();
	int A;
	cin >> A;
	getline(cin,s);

	cout << "Case #"<<caso<<":"<<endl;
	REP(i,A){
		string ani,fea;
		cin >>ani;

		int nfea;
		cin >>nfea;
		
		REP(j,nfea){
			cin>>fea;
			mymap[ani][fea]=1;
		}
		getline(cin,s);
		cout << go(tree,ani,1)<<endl;
	}

	int sol=0;
	
}
int main()
{
	int T; scanf("%d",&T);
	getline(cin,s);	
	FORE(i,1,T) run1(i);
	return 0;
}
