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
const int INF = 0x3f3f3f3f;

string alph = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
	freopen("A-small-1.in","r",stdin);
	freopen("A-small-1.out", "w", stdout);
	//freopen("data.in","r",stdin);
	//freopen("data.out", "w", stdout);
	int T; scanf("%d\n", &T);
	char buffer[200];
	for(int t=1; t<=T; ++t){
		gets(buffer);
		string s(buffer);
		printf("Case #%d: ", t);
		for(int i=0, n=s.size(); i<n; ++i){
			if(s[i] == ' ')continue;
			s[i] = alph[s[i] - 'a'];
		}
		printf("%s\n", s.c_str());
	}
	return 0;
}