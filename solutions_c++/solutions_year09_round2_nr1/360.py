#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>
#include <ctype.h>

using namespace std;

const int nmax = 1000000;

struct node{
	string name;
	int l,r;
	double p;
};

node tree[nmax];


string tt[nmax];
string animal[nmax];

int n,na;

double num(string s){
	stringstream ss;
	ss << s;
	double n;
	ss >> n;
	return n;
}
int pos;

void rec(int nn){
	int cur = n;
	double p;
	p = num(tt[pos]);
	++pos;
	tree[cur].p = p;
	if (pos == nn || !isalpha(tt[pos][0])){
		tree[cur].name = "!";
	}
	else{
		tree[cur].name = tt[pos];
		++pos;
		++n;
		tree[cur].l = n;
		rec(nn);

		++n;
		tree[cur].r = n;
		rec(nn);
	}
}

double dfs(int cur){
	if (tree[cur].name == "!") return tree[cur].p;
	
	bool ok = false;
	for (int i = 0;i < na; ++i)
		if (tree[cur].name == animal[i]){
			ok = true;
			break;
		}
	double q;
	if (ok) q = dfs(tree[cur].l);
	else q = dfs(tree[cur].r);
	return q * tree[cur].p;
}


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int ntest;
	scanf("%i",&ntest);

	for (int test = 1;test <= ntest; ++test){
		int l;
		scanf("%i",&l);
		stringstream ss;
		

		string s,s1;
		getline(cin,s1);
		for (int i = 1;i <= l; ++i){
			getline(cin,s1);
			s+=s1;
		}
		for (int i = 0;i < s.size(); ++i)
			if (s[i] == ')' || s[i] == '(') s[i] = ' ';

		ss << s;

		int nt = 0;

		while (ss >> s1){
			tt[nt] = s1;
			//cout << s1 << " ";
			++nt;
		}
		//cout << endl;

		n = 0;
		pos = 0;
		rec(nt);
		int a;
		scanf("%i",&a);
		printf("Case #%i:\n",test);

		for (int i = 0;i < a; ++i){
			cin >> s1;
			cin >> na;
			for (int j = 0;j < na; ++j) cin >> animal[j];
			printf("%.7lf\n",dfs(0));
		}
		
	}


	
	return 0;
}