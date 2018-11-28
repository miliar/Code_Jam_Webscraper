#include <cstdio>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <cassert>

using namespace std;

char buffer[128];

struct node{
	double p;
	string name;
	int left, right;
};

node nodes[102400];
int nodeN;
string in;
set<string> match;

int cu(int idx, char c, char u){
	int n=0, z=0;
	while(1){
		if(in[idx+n] == u)
			return z;
		if(in[idx+n++] == c)
			++z;
		if(z == 2)
			return z;
	}
}

int parse(int &idx, bool l=false){
	int n = nodeN++;
	//fprintf(stderr, "parse: %s\n\n", in.substr(idx, -1).c_str());
	while(in[idx] != '(')
		++idx;
	++idx;
	int i;
	while(isspace(in[idx]))
		++idx;
	for(i=0; !isspace(in[idx]) && in[idx] != ')';++i, ++idx)
		buffer[i] = in[idx];
	buffer[i] = '\0';
	nodes[n].p = strtod(buffer, NULL);
	if(!cu(idx, '(', ')')){
		nodes[n].name = "";
		for(; in[idx] != ')'; ++idx)
			;
		return n;
	}
	while(isspace(in[idx]))
		++idx;
	for(i=0; !isspace(in[idx]) && in[idx] != '(';++i, ++idx)
		buffer[i] = in[idx];
	buffer[i] = '\0';
	nodes[n].name = string(buffer);
	assert(nodes[n].name.size());
		
	nodes[n].left = parse(idx, true);
	++idx;
	nodes[n].right = parse(idx, true);
	++idx;
	
	for(i=0; in[idx] != ')'; ++idx)
		;
	return n;
}

void rek(int n, double &p){
	p *= nodes[n].p;
	if(!nodes[n].name.size())
		return;
	if(match.find(nodes[n].name) != match.end())
		rek(nodes[n].left, p);
	else
		rek(nodes[n].right, p);
}

int main(){
	int tc, tcN;
	int N, M;
	scanf("%d", &tcN);
	for(tc=1; tc<=tcN; ++tc){
		scanf("%d ", &M);
		in = "";
		for(int i=0; i<M; ++i){
			fgets(buffer, sizeof(buffer), stdin);
			in += " ";
			in += string(buffer);
		}
		nodeN = 0;
		int idx = 0;
		parse(idx);
		printf("Case #%d:\n", tc);
		scanf("%d ", &N);
		for(int i=0; i<N; ++i){
			string line;
			match.clear();
			getline(cin, line);
			stringstream ls(line);
			int K;
			ls >> buffer >> K;
			for(int k=0; k<K; ++k){
				ls >> buffer;
				match.insert(string(buffer));
			}
			double p = 1;
			rek(0, p);
			printf("%.7lf\n", p);
		}
	}
}
