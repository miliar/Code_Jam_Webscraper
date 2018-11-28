
#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i = a; i <b ; i++)
#define FRR(i,a,b) for(int i = b - 1; i >=a ; i--)
#define sz size()
#define pb push_back
#define VI vector<int>
#define VVI vector<VI>
#define eps 1e-9
#define INF 1000000
#define mp make_pair()
#define SS stringstream
#define VS vector<string>


//int getDiff(string a, string b){
//	int depth = 0;
//	FOR(i,0,b.sz)depth+=b[i] == '/';
//	int common = 0;
//	FOR(i,0,min(a.sz, b.sz)){
//		if(a[i] != b[i]){
//			common--;
//			break;
//		}
//		common+=a[i] == '/';
//	}
//	return depth - common;
//}



vector<string> tokenize(string a, char delim){
	vector<string> ret;
	int i =0;
	while( i < a.sz){
		for(; i < a.sz && a[i] == delim; i++);
		int j = i;
		string tmp = "";
		for(; j < a.sz && a[j] != delim; j++)tmp+=a[j];
		i = j;
		if(tmp != ""){
			ret.pb(tmp);
		}
	}
	return ret;
}

int getDiff(string a, string b){
	VS ta = tokenize(a, '/'), tb = tokenize(b, '/');
	int ret = tb.sz;
	FOR(i,0,tb.sz){
		if(i < ta.sz && ta[i] == tb[i])ret--;
		else break;
	}
	return ret;
}

int main(){
	int cases;
	cin >> cases;
	FOR(caseNum, 0, cases){
		int n, m;
		vector<string> exist;
		exist.pb("");
		cin >> n >> m;
		int ans = 0;
		FOR(i,0,n){
			string tmp; cin >> tmp; exist.pb(tmp);
		}
		
		FOR(j,0,m){
			string dir; cin >> dir;
			int add=INF;
			FOR(i,0,exist.sz){
				add = min(add, getDiff(exist[i], dir));
			}
			exist.pb(dir);
			ans+=add;
		}
		cout << "Case #" << caseNum+1 << ": " << ans << endl;
	}
	
}