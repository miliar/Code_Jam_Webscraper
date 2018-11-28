#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define fr(x,y,z) for(int x = (y); x < (z); x++)

#define console cout
#define dbg(x) console << #x << " == " << x << endl
#define print(x) console << x << endl

char seq[100];
map<char,int> mapa;

void read() {
	scanf("%s",seq);
}

int casos = 1;

void process() {

	mapa.clear();
	mapa[seq[0]] = 1;
	int pos = 1;
	for(pos = 1; seq[pos]; pos++) {
		if(seq[pos] != seq[0]) {
			mapa[seq[pos]] = 0;
			break;
		}
	}
	
	for(; seq[pos]; pos++) {
		if(!mapa.count(seq[pos])) {
			int tam = mapa.size();
			mapa[seq[pos]] = tam;
		}		
	}
	
	int base = mapa.size();
	base = max(base,2);
		
	ll res = 0;
	for(int i = 0; seq[i]; i++) {
		res *= base;
		res += mapa[seq[i]];
	}
	
	cout << res << endl;
}

int main() {

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++) {
		read();
		printf("Case #%d: ",i);
		process();
	}		
	return 0;
	
}
