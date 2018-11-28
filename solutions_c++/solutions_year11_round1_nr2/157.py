#include <iostream>
#include <vector>
#include <set>
#include <assert.h>
#include <map>
#include <string>
#include <cstdio>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;

#define For(i,a,b) for(int i=a;i<b;i++)
#define rep(i,x) For(i,0,x)
#define foreach(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); ++i)
#define F first
#define S second
#define sz(x) ((int)(x).size())
#define SQ(x) ((x)*(x))
#define mp make_pair
#define pb push_back
#define TWO(x) (1<<(x))

typedef pair<vector<string>,int> Part;
typedef vector<Part> Ps;

void process(Part part, char c, Ps& res){
//	cout<<"DO: "<<c<<endl;
	bool use = false;

	map<int, Part> M;
	foreach(it, part.F){
		string s = *it;
		int n = sz(s);
		int key = 0;
		rep(i,n) if(s[i]==c){
			key += TWO(i);
			use = true;
		}
		M[key].S = part.S;
		M[key].F.pb(s);
	}
	if(use && M.find(0) != M.end()){
		M[0].S++;
	}
	foreach(it, M) res.pb(it->S);
}

void show(Ps in){
	return;
	cout<<"=======SET======="<<endl;
	foreach(it, in){
		cout<<"CLASS: "<<it->S<<endl;
		foreach(it2, it->F){
			cout<<(*it2)<<" ";
		}
		cout<<endl;
	}
	cout<<"=================="<<endl;
}

int main(){
int np;cin>>np;
rep(tp,np){
	map<int, vector<string> > D;
	map<string,int> M;
	int n,m;cin>>n>>m;
	string first;
	rep(i,n){
		string t; cin>>t;
		if(i==0) first = t;
		M[t] = i;
		D[sz(t)].pb(t);
	}
	vector<string> ans;
	rep(i,m){
		string L; cin>>L;
		int best_score = 0;
		string best_string = first;
		Ps cur;
		foreach(it, D){
			cur.pb(mp(it->S, 0));
		}
		rep(k, sz(L)){
			show(cur);
			Ps next;
			foreach(it, cur) process(*it, L[k], next);
			foreach(it, next) foreach(it2, it->F){
				int score = it->S;
				string s= *it2;
				if(score > best_score || (score == best_score && M[s] < M[best_string])){
					best_string = s;
					best_score = score;
				}
			}
			cur = next;
		}
		ans.pb(best_string);
	}
	printf("Case #%d:", tp+1);
	foreach(it, ans) cout<<" "<<(*it);
	cout<<endl;
}
}
