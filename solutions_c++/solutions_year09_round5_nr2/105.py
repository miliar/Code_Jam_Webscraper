#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORD(i,n) for (int i=n-1; i>=0; --i)
#define FORALL(s,x) for (typeof(s.begin()) x=s.begin(); x!=s.end(); ++x) 
#define PRINT(s) {FORALL(s,v) cout << *v << " "; cout << endl;}
#define pii pair<int, int>
#define mp make_pair
#define pb push_back
#define int64 long long

#define MOD 10009

struct Word{
	int c[26];
	Word(string w) {
		memset(c,0,sizeof(c));
		FORALL(w,ch)
			++c[*ch-'a'];
	}	
	Word() {memset(c,0,sizeof(c));}
	void print() {
		FOR(i,26)
			cout << c[i] << " ";
		cout << endl;
	}
	
	int eval(string poly) {
		int p=1, s=0;
		FORALL(poly, ch) {
			if (*ch=='+') {
				s=(s+p)%MOD;
				p=1;
			} else {
				p=(p*c[*ch-'a'])%MOD;
			}
		}
		s+=p;
		return s;
	}
	
	void reset() {
		memset(c,0,sizeof(c));
	}
	
	void plus(Word a) {
		FOR(i,26) c[i]+=a.c[i];
	}
	
	void minus(Word a) {
		FOR(i,26) c[i]-=a.c[i];
	}
};

#define MAX 125

Word word[MAX];
string poly;
int k, n;

void input() {
	//cout << Word("abracadabra edgar").eval("aber+aab+c") << endl;
	cin >> poly >> k;
	cin >> n;
	FOR(i,n) {
		string w;
		cin >> w;
		word[i]=Word(w);		
		//word[i].print();
	}
}

#define MAXK 15

int fact[] = {1,1,2,6,24,120};

int subset[MAXK], subset_sz, result[MAXK];
Word sum;

int cnt[MAX];

int nRepeat() {
	memset(cnt,0,sizeof(cnt));
	for (int i=1; i<=subset_sz; ++i) {
		++cnt[subset[i]];
	}
	int nr=fact[subset_sz];
	for (int i=1; i<=subset_sz; ++i) {
		nr/=fact[cnt[subset[i]]];
		cnt[subset[i]]=0;
	}			
	return nr;
}

void try_subset(int i) {	
	if (i==0) {
/*		for (int i=1; i<=subset_sz; ++i)
			cout << subset[i] << " ";
		cout << endl;
//		sum.print();*/
		result[subset_sz]=(result[subset_sz]+sum.eval(poly)*nRepeat())%MOD;
		return;
	}
	FOR(v,subset[i+1]+1) {
		sum.plus(word[v]);
		subset[i]=v;
		try_subset(i-1);
		sum.minus(word[v]);
	}
}

void solve() {
	memset(result,0,sizeof(result));
	for (int i=1; i<=k; ++i) {
		subset[i+1]=n-1;
		subset_sz=i;
		sum.reset();
		try_subset(subset_sz);
	}
}

void output(int test) {
	printf("Case #%d:", test);
	for (int i=1; i<=k; ++i) 
		printf(" %d", result[i]);
	printf("\n");
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nTest;
	scanf("%d", &nTest);
	for (int test=1; test<=nTest; ++test) {
		input();
		solve();
		output(test);
	}
	return 0;
}
