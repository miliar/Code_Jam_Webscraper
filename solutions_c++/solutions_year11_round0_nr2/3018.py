#pragma warning(disable:4018)  // signed/unsigned mistatch
#pragma warning(disable:4244)  // w64 to int cast
#pragma warning(disable:4267)  // big to small -- possible loss of data
#pragma warning(disable:4786)  // long identifiers
#pragma warning(disable:4800)  // forcing int to bool
#pragma warning(disable:4996)  // deprecations
#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
#define all(v) (v).begin(), (v).end()
typedef long long i64;
template <class T> void make_unique(T& v) {sort(all(v)); v.resize(unique(all(v)) - v.begin());}
using namespace std;

bool oposite[30][30]; //who repeals who
char comb[30][30]; //who combines with who
int mark[30]; //what i have in the string

string f(string &s){
	string res = "";
	for(int i=0, n=s.size(); i<n; ++i){
		int last = res.size()-1;
		if(last < 0){
			res += s[i];
			mark[s[i]-'A']++;
		}else if(comb[res[last]-'A'][s[i]-'A'] != 0){
			mark[res[last]-'A'] = max(0, mark[res[last]-'A']-1);
			res[last] = comb[res[last]-'A'][s[i]-'A'];
			mark[res[last]-'A']++;
			
			for(int j='A'; j<='Z'; ++j){ //check for new oposites
				if(mark[j-'A']>0 && oposite[j-'A'][res[last]-'A']){
					memset(mark,0,sizeof(mark));
					res.clear();
					break;
				}
			}
		}else{
			bool flag = true;
			for(int j='A'; j<='Z'; ++j){ //check for new oposites
				if(mark[j-'A']>0 && oposite[j-'A'][s[i]-'A']){
					memset(mark,0,sizeof(mark));
					res.clear();
					flag = false;
					break;
				}
			}
			if(flag){
				res+=s[i];
				mark[s[i]-'A']++;
			}
		}
	}
	return res;
}

int main(){
	freopen("B-large-0.in","r",stdin);
	freopen("B-large-0.out", "w",stdout);
	int T; scanf("%d", &T);
	char buffer[500];
	for(int t=1; t<=T; ++t){
		memset(oposite, false, sizeof(oposite));
		memset(comb, 0, sizeof(comb));
		memset(mark, false, sizeof(mark));

		int C; scanf("%d", &C);
		for(int k=0; k<C; ++k){
			scanf("%s", buffer);
			comb[buffer[0]-'A'][buffer[1]-'A'] = buffer[2];
			comb[buffer[1]-'A'][buffer[0]-'A'] = buffer[2];
		}
		int D; scanf("%d", &D);
		for(int k=0; k<D; ++k){
			scanf("%s", buffer);
			oposite[buffer[0]-'A'][buffer[1]-'A'] = true;
			oposite[buffer[1]-'A'][buffer[0]-'A'] = true;
		}
		int n; scanf("%d %s", &n, buffer);
		string s(buffer);
		string res = f(s);
		printf("Case #%d: [", t);
		if(res.size() > 0)printf("%c", res[0]);
		for(int i=1, n = res.size(); i<n; ++i){
			printf(", %c",res[i]);
		}
		printf("]\n");
	}
	return 0;
}