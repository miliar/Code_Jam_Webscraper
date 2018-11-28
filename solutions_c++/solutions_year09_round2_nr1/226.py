#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define bits(x) __builtin_popcount(x)

vector<string> feat;
vector<int> si,no;
vector<double> prob;


int arbol(){
	int demas=0;
	char c;
	double val;
	cin>>c>>val;
	string ff;
	
	prob.push_back(val);
	string sig;
	
	cin>>ff;
	if (ff[0]==')'){
		feat.push_back("-");
		si.push_back(-1); no.push_back(-1);
		return (int)ff.size()-1;
	}else{
		feat.push_back(ff);
		si.push_back(prob.size());
		int postmp=no.size();
		no.push_back(0);
		arbol();
		no[postmp]=prob.size();
		demas=arbol();
		if (demas>0) return demas-1;
		cin>>c;
		return 0;
	}
}

set<string> tengo;

double calc(int pos){
	double rta=prob[pos];
	if (feat[pos]=="-") return rta;
	if (tengo.find(feat[pos])!=tengo.end()) return rta*calc(si[pos]);
	return rta*calc(no[pos]);
}

int main(){
	int casos,c,L,A;
	
	cin>>casos;
	for (c=0;c<casos;c++){
		printf("Case #%d:\n",c+1);
		
		cin>>L;
		feat.clear(); si.clear(); no.clear(); prob.clear();
		arbol();
		cin>>A;
		
		for (int i=0;i<A;i++){
			tengo.clear();
			string tmp;
			int cant;
			
			cin>>tmp>>cant;
			for (int j=0;j<cant;j++){
				cin>>tmp;
				tengo.insert(tmp);
			}
			printf("%.10f\n",calc(0));
			
		}
	}
	
	return 0;
}
