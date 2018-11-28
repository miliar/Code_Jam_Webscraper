// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <sstream>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef long long ll;

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORTO(i,a,b)  for(int i=(a);i<=(b);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<x<<endl
#define SIZE(X) int(X.size())

#define CLEAR(x) memset(x,0,sizeof(x))

int C, M, A, N;

char buffer[100000];
vector<string> in;

#define MAX 1000000

char feat[MAX][12];
double prob[MAX];
int L[MAX], R[MAX];

int p, top;

int build(int id) {
	p++; // (
	sscanf(in[p++].c_str(), "%lf", &prob[id]);
	if (in[p] != ")") {
		sscanf(in[p++].c_str(), "%s", feat[id]);
		L[id] = build(top++);
		R[id] = build(top++);
	}
	p++; // )
	return id;
}

int main() {
	scanf("%d\n", &C);
	FORTO(c,1,C) {
		CLEAR(L);
		CLEAR(R);
		CLEAR(feat);
		CLEAR(prob);
		in.clear();
		top = 0, p = 0;
		
		scanf("%d\n", &M);
		FOR(i,M) {
			stringstream ss(gets(buffer));
			string s;
			while (ss >> s) {
				string tmp;
				FOR(j,SIZE(s)) {
					if (s[j] == '(' || s[j] == ')') {
						if (tmp != "") in.push_back(tmp);
						tmp = "";
						in.push_back(string(1,s[j]));
					} else {
						tmp += s[j];
					}
				}
				if (tmp != "") in.push_back(tmp);
			}
		}
	//	FOR(i,SIZE(in)) {
		//	DEBUG(in[i]);
	//	}
		
		build(top++);
		
		printf("Case #%d:\n", c);
		
		scanf("%d\n", &A);
		FOR(i,A) {
			set<string> S;
			scanf("%s %d", buffer, &N);
			FOR(j,N) {
				scanf("%s", buffer);
				S.insert(buffer);
			}
			int Q = 0;
			double p = 1.0;
			do {
				p *= prob[Q];
				Q = S.count(feat[Q]) ? L[Q] : R[Q];
			} while (Q);
			printf("%.9lf\n", p);
		}
	}
	return 0;
}
