#include <stdio.h>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <vector>

#include <string.h>
#include <string>

#include <iostream>

using namespace  std;

template<typename T> T sqr(T a) { return (a) * (a); }
template<typename T> int size(T a) { return (int)((a).size()); }

void initf(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}
typedef struct Node * Pnode;
struct Node{
	string name;
	map<string, Pnode> mp;
};
Pnode Root;
int k = 0;
int n, m;

void Insert(Pnode& Root,vector<string> v, int pos){
	if (pos >= size(v))return;
	if(Root->mp[v[pos]] == NULL){
		Pnode cur = new Node;
		cur->name = v[pos];
		Root->mp[v[pos]] = cur;
		++ k;
	}
	Insert(Root->mp[v[pos]], v, pos + 1);
}
void solve(int t){
	Pnode Root = new Node;
	Root->name = "Root";
	string s;
	for(int i = 0; i < n; ++i){
		cin >> s;
		vector<string> pat;
		string cur = "";
		for(int j = 1; j < size(s); ++j){
			if(s[j] == '/'){
				pat.push_back(cur);
				cur = "";
			} else {
				cur += s[j];
			}
		}
		if( size(cur) > 0 ) pat.push_back(cur);
		Insert(Root, pat, 0);
	}
	int sum = 0;
	for(int i = 0; i < m; ++i){
		cin >> s;
		vector<string> pat;
		string cur = "";
		for(int j = 1; j < size(s); ++j){
			if(s[j] == '/'){
				pat.push_back(cur);
				cur = "";
			} else {
				cur += s[j];
			}
		}
		if( size(cur) > 0 ) pat.push_back(cur);
		k = 0;
		Insert(Root, pat, 0);
		sum += k;
	}
	printf("Case #%d: %d\n", t, sum);
}
int main(){


	initf();


	int test ;
	cin >> test;
	for(int t = 0; t < test; ++t){
		cin >> n >> m;
		solve(t + 1);
	}


	return 0;
}