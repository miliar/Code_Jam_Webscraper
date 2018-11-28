// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
const int MAXN = 2000;
typedef vector<int> VI; 


double toDouble(string x) {
	stringstream ss;
	double www;
	ss<<x;
	ss>>www;
	return www;
}

bool isDouble(string x) {
	REP(i,x.size()) 
		if (x[i]!='.') {
			if (x[i]<'0' || x[i]>'9') return false;
		}
	return true;
}



int main() {
	int ile;
	scanf("%d",&ile);
	FOR(iile,1,ile) {
		string wynik="";
		int len;
		char s[200];
		scanf("%d",&len); gets(s);
		REP(i,len) {
			gets(s);
			string st=s;
			REP(j,st.size()) {
				if (st[j]!='(' && st[j]!=')') wynik+=st[j]; else wynik+=" ";
			}
		}
		vector<string> tree;
		stringstream ss;
		ss<<wynik;
		string t;
		while (ss>>t) {
			tree.push_back(t);
		}

		double prob[MAXN];
		string nazwa[MAXN];
		pair<int,int> synowie[MAXN];


		REP(i,MAXN) {
			prob[i]=0;
			nazwa[i]="";
			synowie[i]=make_pair(-1,-1);
		}
		int start=1;
		int nextFree=1;
		int poz=-1;
		stack<int> stos;
		stos.push(start);


		while (!stos.empty()) {
			int curr=stos.top(); stos.pop(); poz++;
			prob[curr]=toDouble(tree[poz]);
			if (poz+1<tree.size() && !isDouble(tree[poz+1])) {
				poz++;
				nazwa[curr]=tree[poz];
				synowie[curr]=make_pair(nextFree+1,nextFree+2);
				stos.push(nextFree+2);
				stos.push(nextFree+1);
				nextFree+=2;
				}
		}

/*
		FOR(i,1,nextFree) {
			cout << "Pozycja " << i << endl;
			cout << nazwa[i] << endl;
			cout << prob[i] << endl;
			cout << "(" << synowie[i].first << " " << synowie[i].second << ")" << endl;
			cout << "---" << endl;
		}
*/
		printf("Case #%d: \n",iile);
		int quest,abil;
		scanf("%d",&quest);
		char name[200],tmp[200];
		REP(i,quest) {
			scanf("%s",name);
			scanf("%d",&abil);
			set<string> v;
			REP(j,abil) {
				scanf("%s",tmp);
				string st=tmp;
				v.insert(st);
			}

			int start=1;
			double wynik=1;
			while (start!=-1) {
				wynik*=prob[start];
				if (v.find(nazwa[start])!=v.end()) {
					start=synowie[start].first;
				} else start=synowie[start].second;
			}
			printf("%.7f\n",wynik);	
		}

	}
	return 0;
}

