// Maciej Andrejczuk

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <assert.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,p,k) for(int i=(p);i<=(k);i++)
#define FORD(i,p,k) for(int i=(p);i>=(k);i--)
#define ZERO(m) memset(m,0,sizeof(m))
#define PB push_back
#define FI first
#define SE second

typedef long long LL;
typedef pair<LL,int> PI;

#define MAXL 15
int l,d,n;
vector<string> v;
bool t[MAXL+3][27];

void wczytaj();
int solve();
int main()
{
	wczytaj();
	FOR(i,1,n) {
		printf("Case #%d: ",i);
		int w = solve();
		printf("%d\n",w);
	}
}

void wczytaj() {
	scanf("%d %d %d",&l,&d,&n);
	REP(i,d) {
		string s;
		cin>>s;
		v.PB(s);
		assert(s.size() == l);
	}
}

int solve() {
	string s;
	cin>>s;
	int k=0;
	REP(i,l) {
		REP(j,27) t[i][j]=0;
		if (s[k]=='(') {
			k++;
			while (s[k]!=')') {
				int pom=s[k]-'a';
				assert(pom>=0 && pom<=26);
				t[i][pom]=1;
				k++;
			}
		}
		else {
			int pom=s[k]-'a';
			assert(pom>=0 && pom<=26);
			t[i][pom]=1;
		}
		k++;
	}
	assert(k==s.size());
	
	int ret=0;
	REP(i,d) {
		bool czy=true;
		REP(j,l) {
			if (!t[j][v[i][j]-'a']) {
				czy=false;
				break;
			}
		}
		ret+=czy;
	}
	return ret;
}
