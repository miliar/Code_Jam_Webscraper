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
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define console cout
#define dbg(x) console << #x << " == " << x << endl
#define print(x) console << x << endl

char c[101][101];
char answ[101][101];
int h,w;

int read(){
	scanf("%d %d", &h, &w);
	for(int i = 0; i < h; i++)scanf("%s", c[i]);
	return 1;
}
void process(){
	for(int i = 0; i < h; i++){
		strcpy(answ[i], c[i]);
	}
	for(int i = h-1; i > 0; i--){
		for(int j = w-1; j > 0; j--)if(answ[i][j] == '#'){
			if(answ[i][j-1] == '#' && answ[i-1][j] == '#' && answ[i-1][j-1] == '#'){
				answ[i][j]='/', answ[i][j-1]='\\', answ[i-1][j] = answ[i][j-1], answ[i-1][j-1]=answ[i][j];
			}
		}
	}
	int ok = 1;
	for(int i = 0; i < h; i++){
		for(int j = 0; j < w; j++)if(answ[i][j] == '#'){
			ok = 0;
		}
	}
	if(ok == 0){
		printf("Impossible\n");
	}else{
		for(int i = 0; i < h; i++)printf("%s\n",answ[i]);
	}
}


// BEGIN CUT HERE
int main() {
//freopen("out.txt","w",stdout);
//freopen("out.txt","w",stderr);
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos && read(); i++){
		fprintf(stderr, "i(%d)\n", i);
		printf("Case #%d:\n", i);
		process();
	}
	return 0;
}
// END CUT HERE 
