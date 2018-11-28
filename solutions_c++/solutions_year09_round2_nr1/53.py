#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <cassert>

using namespace std;

typedef double real;

#define Eo(x) { cerr << #x << " = " << x << endl; }

char buf[1024*1024];

stringstream ss;
set<string> f;

real dfs(const string& all){
	real res = 1;
	int k = 0;
	while (k < all.length() && all[k] != '(') k++;
	k++;
	while (k < all.length() && all[k] == ' ')k++;
	if (k < all.length()){
		int st = k;
		while (k < all.length() && all[k] != ')' && all[k] != ' ')k++;
		string sss(all.substr(st,k-st));
		real t = -1;
		sscanf(sss.c_str(),"%lf",&t);
		res *= t;
		while (k < all.length() && all[k] == ' ')k++;
		if (k < all.length() && isalpha(all[k])){
			int st = k;
			while (k < all.length() && isalpha(all[k]))k++;
			string ff(all.substr(st,k-st));
			if (f.find(ff) != f.end()){
				res *= dfs(all.substr(k));
				return res;
			} else {
				int cnt = 0;
				while (k < all.length() && all[k] != '(')k++;
				cnt++;k++;
				while (cnt && k < all.length()){
					if (all[k] == '(') cnt++;
					else if (all[k] == ')') cnt--;
					k++;
				}
				res *= dfs(all.substr(k));
				return res;
			}
		} else {
			return res;
		}
	}
	assert(0);
	return -1;
}

int main(){
	int T; cin >> T;
	for (int _ = 0; _ < T; _++){
		int l; cin >> l;
		string all;
			gets(buf);
		for (int i = 0; i < l; i++){
			gets(buf);
			all += string(buf);
		}
		Eo(all);
		printf("Case #%d:\n",_+1);
		int n; scanf("%d",&n);
			gets(buf);
		for (int i = 0; i < n; i++){
			f.clear();
			string name; cin >> name;
			int q; cin >> q;
			for (int j= 0 ; j < q; j++){
				string qq; cin >> qq;
				f.insert(qq);
			}
			real p = dfs(all);
			printf("%.10lf\n",double(p));
		}
		
	}
	return 0;
}
