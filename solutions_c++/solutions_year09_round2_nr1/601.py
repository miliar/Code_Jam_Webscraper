#include <iostream>
#include <cstdio>
#include <string>
#include <set>
using namespace std;

const int maxn = 200;
const int mul = 1000000000;
const int root = 1;

struct Node{
	long long pb;
	string ft;
};

Node nodes[maxn];

void build_tree(int pos){
	int loc = pos << 1;
	char c;
	double d;
	c = getchar();
	while(c != '(') c = getchar();
	scanf("%lf", &d);
	nodes[pos].pb = (long long)(mul * d);
	nodes[pos].ft = "";
	c = getchar();
	while(c == ' ') c = getchar();
	if(c == ')'){
		return;
	}
	nodes[pos].ft.push_back(c);
	while(true){
		c = getchar();
		if(c == '\n'){
			build_tree(loc);
			build_tree(loc + 1);
			break;
		}
		else nodes[pos].ft.push_back(c);
	}
	c = getchar();
	while(c != ')') c = getchar();
}

char buff[1000];

double query(){
	long long ans = mul;
	int num, pos = root;
	set<string> ss;
	string s;
	scanf("%s", buff);
	scanf("%d", &num);
	while(num--){
		scanf("%s", buff);
		s = buff;
		ss.insert(s);
	}
	while(true){
		ans = ans * nodes[pos].pb / mul;
		if(nodes[pos].ft == "") break;
		if(ss.count(nodes[pos].ft)) pos = (pos << 1);
		else pos = (pos << 1) + 1;
	}
	return double(ans) / mul;
}

int main(){
	int t, a, i, m;
	double ans;
	scanf("%d", &t);
	for(i = 1; i <= t; i++){
		scanf("%d\n", &a);
		build_tree(root);
		scanf("%d\n", &m);
		printf("Case #%d:\n", i);
		while(m--){
			ans = query();
			printf("%.7lf\n", ans);
		}
	}
}
	
	

