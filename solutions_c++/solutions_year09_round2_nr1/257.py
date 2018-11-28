#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <queue>
#include <algorithm>
#include <list>
#include <sstream>

using namespace std;

#define f(i,j,k) for(int i = j; i < k; i++)
#define fd(i,j,k) for(int i = j; i >= k; i--)
#define pb push_back
#define sz size
#define all(a) (a).begin(), (a).end()
#define vs vector<string>
#define vi vector<int>
#define deb(x...) //printf(x)

template <typename T>
void printv(vector<T>& v){
	int n = v.sz();
	printf("[");
	for(int i = 0; i < n; i++){
		cout << v[i] << ", ";
	}
	printf("]\n");
}

vs split(const string& s, const string delim){
	vs res;
	string at;
	int n = s.sz();

	for(int i = 0; i < n; i++){
		char c = s[i];
		if(delim.find(c) != string::npos){
			if(at.sz() > 0){
				res.pb(at);
			}
			at = "";
		} else {
			at.pb(c);
		}
	}
	if(at.sz() > 0){
		res.pb(at);
	}

	return res;
}

template <typename S, typename T>
T convert(const S var){
	T res;
	stringstream ss;

	deb("C1\n");
	ss << var;
	deb("C2\n");
	ss >> res;
	deb("C3");

	return res;

}

vs arv;



int end_tree(int idx){
	int qt_abre = 1;
	for(++idx;idx < arv.sz() ;idx++){
		if(arv[idx] == ")"){
			if(qt_abre == 1){ return idx; }
			qt_abre--;
		} else if(arv[idx] == "(") {
			qt_abre++;

		}

	}
	return -1;
}

class tree{
public:
	string feat;
	tree* t1, *t2;
	double w;

	tree(int idx1, int idx2){
		deb("idx1 = %d, idx2 = %d, (%d)\n", idx1, idx2, idx1==idx2);
		if(idx1 == idx2){
			deb("A\n");
			w = convert<string, double>(arv[idx1]);
			t1=t2=NULL;
			feat = "";
		} else {
			deb("B\n");
			deb("arv[idx+1] = %s\n", arv[idx1+1].c_str());
			w = convert<string, double>(arv[idx1]);
			deb("B1\n");
			feat = arv[idx1+1];
			deb("B2\n");
			int end = end_tree(idx1+2);
			deb("B3\n");
			t1 = new tree(idx1+3, end-1);
			deb("B4\n");
			int ns = end+1;
			deb("B5\n");
			end = end_tree(ns);
			deb("B6\n");
			t2 = new tree(ns+1, end-1);
			deb("B7\n");
		}
	}

	~tree(){
		if(t1 != NULL) delete t1;
		if(t2 != NULL) delete t2;
	}

	void getprob(double &p, set<string>& s){
		p *= w;
		if(t1 == NULL) return;

		if(s.find(feat) != s.end()){
			t1->getprob(p, s);
		} else {
			t2->getprob(p, s);
		}
	}
};

int main(void){
	int T;
	scanf("%d\n",&T);
	for(int p = 0; p < T; p++){
		int lins;
		printf("Case #%d:\n",p+1);
		scanf("%d\n",&lins);
		string raw, s;
		for(int i = 0; i < lins; i++){
			getline(cin, s);
			raw += " " + s;
		}
		deb("0\n");
		string nraw;
		for(int i =0; i < raw.sz(); i++){
			if(raw[i] == '(' || raw[i] == ')'	){
				nraw.pb(' ');
				nraw.pb(raw[i]);
				nraw.pb(' ');
			} else {
				nraw.pb(raw[i]);
			}
		}
		deb("1\n");

		arv = split(nraw, " ");
		//printv(arv);
		deb("2 (%d)\n", arv.sz());
		int ending = arv.sz()-2;
		tree t(1,ending);

		deb("3\n");
		int n;
		cin >> n;
		for(int i = 0; i < n; i++){
			string an;
			int feats;
			string s;
			cin >> an >> feats;
			set<string> ss;
			for(int j = 0; j < feats; j++){
				cin >> s;
				ss.insert(s);
			}
			double p = 1;
			t.getprob(p,ss);
			printf("%.7lf\n", p);
		}
	}

	return 0;

}
