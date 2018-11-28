#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <cmath>
#include <numeric>
#include <cassert>
#include <bitset>

using namespace std;

struct token{
	double p;
	string feature;
	token *has;
	token *hasnt;	
	token(){
		has = hasnt = NULL;
	}
	~token(){
		delete has;
		delete hasnt;
	}
	double traverse(double prob, const set<string> &animal){
		prob*=p;
		if(has == NULL){
			assert(hasnt == NULL && feature == "");
			return prob;
		}
		if(animal.find(feature) != animal.end()){
			//printf("...is %s\n", feature.c_str());
			return has->traverse(prob, animal);
		}
		else {
			//printf("...is NOT %s\n", feature.c_str());
			return hasnt->traverse(prob, animal);
		}
	}
};

char buf[100];

token* readtoken(){
	token *n = new token();
	while(getchar() != '(');
	scanf("%lf", &n->p);
	buf[1] = '\0';
	while((buf[0] = getchar())==' ' || buf[0] == '\n');
	if(buf[0]==')'){
		return n;
	} else {
		char c;
		for(int i = 1; (c = getchar())>='a' && c <='z'; ++i){
			buf[i]=c;
			buf[i+1]='\0';
		}
		bool ended = (c == ')');
		n->feature = buf;
//		printf("Read feature: '%s'\n", buf);
		n->has = readtoken();
		n->hasnt = readtoken();
		if(!ended)
			while(getchar() != ')');
		return n;
	}
}

inline bool solve(int tc){
	scanf("%*d");
	token *t = readtoken();
	int a;
	printf("Case #%d:\n", tc);
	scanf("%d", &a);
	for(int i = 0; i<a; ++i){
		int n;
		scanf("%s%d",buf,&n);
		//printf("%s:\n",buf);
		set<string> animal;
		for(int j = 0; j<n; ++j){
			scanf("%s", buf);
			animal.insert(string(buf));
		}
		printf("%.7lf\n", t->traverse(1.0, animal));
	}
	delete t;
	return true;
}

int main (int argc, char const *argv[]) {
	int n; scanf("%d",&n);
	for(int k=1;solve(k)&&k<n;k++);
	return 0;
}