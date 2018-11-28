#include <iostream> 
#include <queue>
#include <algorithm>
#include <vector>
#include <cassert>
#include <map>
#include <cmath>
#include <set>
#include <string>
#include <cstring>
#include <cstdio>
#include <sstream>
#ifdef D 
#define D 1
#else 
#define D 0
#endif

using namespace std; // insert push_back find size begin first second

typedef unsigned long long ULL;
typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef map<int,int> MII;
typedef vector<PII> VPII;
typedef set<int> SI;
typedef set<string> SS;
typedef vector<string> VS;
typedef vector<char> VC;
typedef vector<VC> VVC;


char foo[32][32];


struct bar{
	struct bar *next[26];
};


void rek(int pos, string t, const VVC &v, VS &vs){
    if(pos==(int)v.size()){
		vs.push_back(t);
		return;
	}

	for(int i=0;i<(int)v[pos].size();i++){
		char c = v[pos][i];
		if(!foo[pos][c-'a'])continue;
		char tmp[2];
		tmp[0]=tmp[1] = '\0';
		tmp[0] = c;
		string ap = string(tmp);
		rek(pos+1,t+ap,v,vs);
	}
}
VVC dec(string s){

	string t="";
	for(int i=0;i<(int)s.size();i++){
		if(s[i]==')') t = t+ " ";
		else 
		if(s[i]=='(') t = t+ " (";
		else t = t+""+s[i];
	}


	
	stringstream ss(t);

	VVC ret;
	int pos = 0;
	VS v;
	string u;
	while(ss >> u) v.push_back(u);
	for(int i=0;i<v.size();i++){
		string w = v[i];
		if(w[0]=='('){
			VC vc;
			for(int j=1;j<(int)w.size();j++){
				vc.push_back(w[j]);
			}
			ret.push_back(vc);
		}else{
			for(int j =0;j<(int)w.size();j++){
				VC vc ;
				vc.push_back(w[j]);
				ret.push_back(vc);
			}
		}
	}
/*
	for(int i=0;i<ret.size();i++){
		printf("(");
		for(int j=0;j<ret[i].size();j++) printf("%c",ret[i][j]);
		printf(")");
	}
	puts("");
*/
	return ret;
}

struct bar tree;


void ins(string s){
	struct bar *pos;
	pos = &tree;
	for(int i=0;i<(int)s.size();i++){
		char c = s[i] - 'a';
		assert(0<=c && c <26);
		if(pos->next[c]==NULL) 
			pos->next[c] = (struct bar*) calloc(1,sizeof(struct bar));
		pos = pos->next[c];
	}
}
int cnt;
void search(const VVC & vvc, int pos, struct bar *root){
	if(pos==(int)vvc.size()){
		cnt++;	
		return ;
	}
	assert(root!=NULL);

	for(int i=0;i<(int)vvc[pos].size();i++){
//		printf("c: %c (%d,%i)\n",vvc[pos][i],pos,i);
		char c = vvc[pos][i]-'a';
		assert(0<=c && c <26);
		if(NULL!=root->next[c]){
			search(vvc,pos+1,root->next[c]);
		}
	}
}

int main(){

	SS wordset;
	memset(&tree,0,sizeof(struct bar));
	int l,d,n;
	scanf("%d %d %d ",&l,&d,&n);
	for(int i=0;i<d;i++){
		string in;
		cin >> in;
		wordset.insert(in);
		ins(in);
		assert(in.size()==l);
		for(int j=0;j<l;j++){
			foo[j][in[j]-'a']=1;
		}
	}

	for(int kase=1;kase<=n;kase++){
		string in;
		cin >> in;
		VVC decomposed = dec(in);
		cnt = 0;
		search(decomposed,0,&tree);
/*		VS vs;
		string tmp = "";
		rek(0,tmp,decomposed, vs);
		cnt = 0;
		for(int i=0;i<(int)vs.size();i++){
			cout << "i: " << i << " " << vs[i] << endl;
			if(wordset.find(vs[i])!=wordset.end()) cnt++;
		}*/
		printf("Case #%d: %d\n",kase,cnt);
	}
	



	return 0;
}
