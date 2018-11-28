#include <cstdio>
#include <iostream>
#include <string>
#include <set>
using namespace std;

int ans;
set<string> dict;
string t;

void go(int dep, string s){
	if (dict.find(s)==dict.end()) return;
	if (dep==t.length()){
		++ans;
	} else {
		if (t[dep]!='(') go(dep+1,s+t[dep]);
		else{
			int k=dep;
			while (t[k]!=')') ++k;
			for (int i=dep+1;i<k;++i)
				go(k+1,s+t[i]);
		}
	}
}

int main(){
	int l, d, n;
	cin >> l >> d >> n;
	while (d--){
		cin >> t;
		dict.insert(t);
		for (int i=t.length()-1;i>=0;--i)
			dict.insert(t.erase(i));
	}
	for (int z=1;z<=n;++z){
		cin >> t;
		ans = 0;
		go(0,"");
		printf("Case #%d: %d\n",z,ans);
	}
	return 0;
}
