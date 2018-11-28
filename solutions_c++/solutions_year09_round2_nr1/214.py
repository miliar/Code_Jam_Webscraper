#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>
#include <ctype.h>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

char s[1000000];

struct Node {
	double w;
	string n;
	int f,s;
};

Node nodes[100000];
int nidx = 0;

char la;

int skip(){
	while (la!='(' && la!=')' && !isdigit(la) && !isalpha(la) && la!='.'){
		la = getchar();
	}
}

int next(){
	la = getchar();
	skip();
}

double weight(){
	string s(1,la);
	while (true){
		la = getchar();
		if (isdigit(la) || la=='.'){
			s += la;
		} else break;
	}
	skip();
//	printf("weight = %s\n",s.c_str());
	return atof(s.c_str());
}

string name(){
	string s(1,la);
	while (true){
		la = getchar();
		if (isalpha(la)) s += la;
		else break;
	}
//	printf("name = %s\n",s.c_str());
	skip();
	return s;
}

int tree(int first){
	assert(la=='(');
	next();
	
	int node = nidx++;
	Node &X = nodes[node];
	X.w = weight();
	X.n = "-";
	X.f = X.s = -1;

	if (isalpha(la)){
		X.n = name();
		X.f = tree(false);
		X.s = tree(false);
	}
	assert(la==')');
	if (!first) next();
	return node;
}

int main(){
	int nTC,A,n;
	scanf("%d",&nTC);
	for (int TC=1; TC<=nTC; TC++){
		printf("Case #%d:\n",TC);
		scanf("%d",&A);

		next();
		int root = tree(true);

		scanf("%d",&A);
		//printf("A = %d\n",A);
		for (int i=0; i<A; i++){
			scanf("%s %d",s,&n);

			set<string> fs;
			for (int j=0; j<n; j++){
				scanf("%s",s);
				fs.insert(s);
			}

			double prob = 1.0;
			for (int j=root; ; ){
				Node &X = nodes[j];
				//printf("%lf %s %d %d\n",X.w,X.n.c_str(),X.f,X.s);
				prob *= X.w;
				if (X.n == "-"){
					break;
				} else if (fs.count(X.n)){
					j = X.f;
				} else {
					j = X.s;
				}
			}
			printf("%.7lf\n",prob);
		}
	}
}
