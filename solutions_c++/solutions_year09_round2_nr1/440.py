#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <sstream>
#include <cstring>
#include <iostream>
#include <cassert>
#include <cctype>

using namespace std;

int T, L, N;
char line[1<<20];
string S;

struct Node {
	Node() { w = 0 ; }
	string name;
	double w;
	vector<int> kids;
};
vector<Node> nodes;

set<string> F;


int next(int i)
{
	//int i0=i; 
	for (;i<S.size() && S[i]==' '; ++i) ;
	//if (i==S.size()) printf("-- %d %d %d\n", i0, i, S.size());
	assert(i<S.size());
	return i;
}


int parse(int par, int i)
{
	nodes.push_back(Node());
	int ix = nodes.size()-1;
	Node& nd = nodes[ix];

	if (par!=-1) {
		nodes[par].kids.push_back(ix);
	}

	i = next(i);
	assert(isdigit(S[i]));

	int j;
	for (j=i; isdigit(S[j])||S[j]=='.'; ++j) ;
	nd.w = atof(S.substr(i, j-i).c_str());
	//cout << "w = " << nd.w << endl;

	i = next(j);

	if (S[i]==')') {
		return i+1;
	} else {	// letters
		for (; 'a'<=S[i] && S[i]<='z'; ++i) {
			nd.name.push_back(S[i]);
		}
		//cout << "name = " << nd.name << endl;

		//int i0=i;
		i = next(i);
		//printf("-- %d %d\n", i0, i);
		//printf("-- %d %d\n", next(4), S[4]==' '?1:0);
		assert(S[i]=='(');
		i = parse(ix, i+1);

		i = next(i);
		assert(S[i]=='(');
		i = parse(ix, i+1);

		i = next(i);
		assert(S[i]==')');
		return i+1;
	}
}

double trav(int i, double p)
{
	p *= nodes[i].w;
	if (nodes[i].name.empty()) {
		return p;
	} else if (F.find(nodes[i].name)!=F.end()) {
		return trav(nodes[i].kids[0], p);
	} else {
		return trav(nodes[i].kids[1], p);
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	gets(line);
	T = atoi(line);

	for (int test=0; test<T; ++test) {
		nodes.clear();

		gets(line);
		L = atoi(line);

		S = "";
		for (int l=0; l<L; ++l) {
			gets(line);
			S += line;
			S += " ";
		}
		//cout<<S<<endl;

		int i = next(0);
		assert(S[i]=='(');
		parse(-1, i+1);

		printf("Case #%d:\n", test+1);

		gets(line);
		N = atoi(line);

		for (i=0; i<N; ++i) {
			gets(line);

			string anim, feat;
			int n;

			F.clear();

			istringstream iss(line);
			iss >> anim >> n;
			for (int f=0; f<n; ++f) {
				iss >> feat;
				F.insert(feat);
			}

			double ans = trav(0, 1.0);
			printf("%.7lf\n", ans);
		}
	}

	return 0;
}