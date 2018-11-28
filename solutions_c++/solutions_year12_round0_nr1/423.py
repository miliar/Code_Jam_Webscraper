#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <stdlib.h>
#include <stdio.h>
#include <numeric>
#include <string.h>
#include <cassert>

#ifdef _DEBUG
#define typeof(X) std::identity<decltype(X)>::type //C++0x (for vs2010)
#else
#define typeof(X) __typeof__(X) // for gcc
#endif

#define sz(a)  int((a).size())
#define FOREACH(it, c) for (typeof((c).begin()) it=(c).begin(); it != (c).end(); ++it)
#define FOR(i,count) for (int i = 0; i < count; i++)
#define V_CIN(v) do{for(int i = 0; i < sz(v); i++) cin >> v[i];}while(0)
#define all(c) (c).begin(),(c).end()

using namespace std;
static const double EPS = 1e-10;
typedef long long ll;
const int MODULO = 1000000007;

//BEGIN!!!
char dest[] = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
	int n;
	cin >> n;
	char s[256];
	gets(s);
	FOR(i,n){
		gets(s);
		for(int j = 0; s[j]; j++){
			if(s[j] != ' ')	s[j] = dest[s[j] - 'a'];
		}
		printf("Case #%d: %s\n",i + 1,s);
	}
	return 0;
}