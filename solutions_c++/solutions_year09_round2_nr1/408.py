#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <sstream>
#include <set>
#include <numeric>
#include <map>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <memory>

template<typename _T,typename _S> _T cast(_S _a) {std::stringstream _s;_s << _a;_T _r; _s >> _r;return _r;}
template<typename end_type> std::vector<end_type> split(const std::string& s,const std::string &delim = " "){std::vector<end_type>res;std::string t;for(int i=0;i!=s.size();++i){if(delim.find(s[i])!=std::string::npos){if(!t.empty()){res.push_back(cast<end_type>(t));t="";}}else {t+=s[i];}} if(!t.empty()){res.push_back(cast<end_type>(t));}return res;}
int s2i(std::string _x) {return cast<int>(_x);}

#define INF 0x7fffffff
#define EPS 1e-12
#define IN(x,a,b) ((x)>(a)&&(x)<(b))
#define round(x) floor(x+0.5)
#define round2(x,p) round(x*(1e-p))/(1e-p)
#define ALL(x) (x).begin(),(x).end()
#define sqr(a) ((a)*(a))
#define WR printf
#define RE scanf
#define FOR(i,Be,En) for(i=(Be);i<=(En);i++)
#define DFOR(i,Be,En) for(i=(Be);i>=(En);i--)
#define PB push_back
#define SZ(a) (int)((a).size())
#define FIT(i,v) for(i=(v).begin();i!=(v).end();i++)
#define RFIT(i,v) for(i=(v).rbegin();i!=(v).rend();i++)
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define SE second
#define FI first
#define CLR(a) memset(a,0,sizeof(a))
#define ULL  unsigned long long
#define LL long long

using namespace std;

struct tree{
	tree *left, *right;
	tree* parent;
	double val;
	string name;
	tree(){
		left = right = parent = NULL;
		name = "";
		val = 1;
	}
	tree(tree *le, tree *ri, tree* pa, string na, double v):left(le),right(ri),parent(pa),name(na),val(v){}
};

tree* root;

int pos = 0;
string s;
set<string>vv;

tree* make(tree* par){
	tree * cur;	
	bool qq = false;
	bool beg = false;
	for(;pos<s.size();++pos){
		if(s[pos] == '('){	
			beg = true;
			int j;
			for(j = pos + 1; j < s.size(); ++j){
				if(s[j] == '(')
					break;					
				if (s[j] == ')'){
					qq = true;
					break;
				}
			}
			int sz = s.size();
			string tmp = s.substr(pos+1,j - pos - 1);
			stringstream ss(tmp);
			double n;
			string name = "";
			ss >> n;
			if(ss)
				ss >> name;
			cur = new tree(NULL,NULL,par,name,n);
			pos = j;
			if(qq)
				return cur;
			cur->left = make(cur);
			cur->right = make(cur);
		}
		if(s[pos] == ')' && beg)
			return cur;
	}
	return cur;
}

double dfs(double p,tree * rr){
	p *= rr->val;
	if(rr->left == NULL && rr->right == NULL)
		return p;
	if(vv.count(rr->name) != 0){
		return dfs(p,rr->left);
	}
	else
		return dfs(p,rr->right);
}

void solve(){
	s = "";
	pos = 0;
	root = NULL;	
	root = new tree(NULL,NULL,NULL,"&&&",1);
	int L;
	scanf("%d\n",&L);
	for(int i=0;i<L;++i){
		char buf[100];
		gets(buf);
		string ss = buf;
		s += ss;		
	}
	root->right = make(root);
	int A;
	scanf("%d\n",&A);
	for(int i=0;i<A;++i){
		vv.clear();
		char buf[1000];
		gets(buf);
		string S = buf;

		stringstream ss(S);
		string name;

		int n;
		ss >> name;
		ss >> n;
		string tmp;		
		for(int j = 0; j < n; ++j){
			ss >> tmp;
			vv.insert(tmp);			
		}
		double p = 1;
		tree* cucu = root;
		printf("%.7lf\n",dfs(p,cucu));
	}
}

int main(){
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  int T;
  scanf("%d\n",&T);
  for(int t = 1; t <= T; ++t){
	  printf("Case #%d:\n",t);
	  solve();
	  //printf("\n");
  }

  return 0;
}