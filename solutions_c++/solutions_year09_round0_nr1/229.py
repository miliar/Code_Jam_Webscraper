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

#define fr(x,y,z)	for(int x = (y); x < (z); x++)

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

int L, D, N;

struct No {
	int adj[30];
	void init() {
		memset(adj,-1,sizeof(adj));
	}
} no[100000];
int n = 1;

void add(char* seq) {
	//dbg(seq);
	int atual = 0;
	for(int i = 0; seq[i]; i++) {
		int& next = no[atual].adj[seq[i]-'a'];
		if(next == -1) {
			next = n++;
			no[next].init();
		}
		atual = next;
		//dbg(atual);
	}
}

#define TAM1 70000
#define TAM2 20

char seq[2000000];

vector<char> v[110];
int q;

void read() {
	no[0].init();
	fr(i,0,D) {
		scanf("%s",seq);
		add(seq);
	}
	
	assert(n < TAM1);
}


char memo[TAM1][TAM2];
int r[TAM1][TAM2];

int busca(int pos = 0, int ind = 0) {	
	if(!memo[pos][ind]) {
		if(ind >= q) {
			r[pos][ind] = 1;
		}
		else {
			r[pos][ind] = 0;
			fr(i,0,v[ind].size()) {
				int next = no[pos].adj[v[ind][i]-'a'];
				if(next != -1) {
					r[pos][ind] += busca(next,ind+1);
				}
			}
		}
		memo[pos][ind] = true;
	}
	return r[pos][ind];
}

int casos = 1;
void process() {
	
	scanf("%s",seq);
	
	int pos = q = 0;
	while(seq[pos]) {
		v[q].clear();
		if(seq[pos] == '(') {
			pos++;
			while(seq[pos] != ')') {
				v[q].push_back(seq[pos]);
				pos++;
			}
			pos++;
		}
		else {
			v[q].push_back(seq[pos]);
			pos++;
		}
		q++;
	}
	
	assert(q < TAM2);
	
	/*fr(i,0,q) {
		printf("v[%d] = {",i);
		fr(j,0,v[i].size()) {
			printf(" %c",v[i][j]);
		}
		printf(" }\n");
	}*/
	
	memset(memo,false,sizeof(memo));
	printf("Case #%d: %d\n",casos++,busca());
}

int main() {

	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%d %d %d",&L, &D, &N);
	
	read();
	
	fr(i,0,N) {
		process();
		fflush(stdout);
	}
	
	return 0;
	
}
