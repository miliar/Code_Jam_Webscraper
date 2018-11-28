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

char magic[28][28];
int hate[28][28], fudeu[101];
char str[101];

int read(){
	memset(magic,0,sizeof magic);
	memset(hate,0,sizeof hate);
	int c,d;
	char ss[5];
	scanf("%d", &c);
	for(int i = 0; i < c; i++){
		scanf("%s", ss);
		magic[ss[0]-'A'][ss[1]-'A'] = ss[2];
		magic[ss[1]-'A'][ss[0]-'A'] = ss[2];
	}
	scanf("%d", &d);
	for(int i = 0; i < d; i++){
		scanf("%s", ss);
		hate[ss[0]-'A'][ss[1]-'A']=1;
		hate[ss[1]-'A'][ss[0]-'A']=1;
	}
	return 1;
}
void process(){
	int N;
	scanf("%d %s", &N, str);
	string ss, s2;
	for(int i = 0; i < N; i++){
		int val = str[i]-'A';
		if(!ss.empty() && magic[ss[ss.size()-1]-'A'][val]){
			ss[ss.size()-1] = magic[ss[ss.size()-1]-'A'][val];
		}else ss = ss + str[i];
		//dbg(ss);
		int ok = 1;
		for(int j = 0; j < ss.size()-1; j++){
			if(hate[ss[ss.size()-1]-'A'][ss[j]-'A']){
				ok = 0;
			}
		}
		if(!ok)ss.clear();
		/*
			ss = ss+str[i];
			int ok = 1;
			for(int j = i+1; j < N; j++){
				int v2 = str[j]-'A';
				if(!magic[str[j-1]-'A'][v2] && hate[val][v2]){
					ok = 0;
					i = j;
					break;
				}
			}
			if(ok){
				ss = ss + str[i];
				//printf("%c", str[i]);
			}
		}*/
	}
	printf("[");
	for(int i = 0; i < ss.size(); i++){
		if(i)printf(", ");
		printf("%c", ss[i]);
	}
	printf("]\n");
}
// BEGIN CUT HERE
int main() {
//freopen("out.txt","w",stdout);
//freopen("out.txt","w",stderr);
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos && read(); i++){
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}
// END CUT HERE 
