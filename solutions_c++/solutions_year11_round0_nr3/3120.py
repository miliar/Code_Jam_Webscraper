
//@author Anurag Sharma
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <climits>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <algorithm>

using namespace std;

#define For(I,A,B)	for(int I = (A); I < (B); ++I)
#define Rep(I,N)	For(I,0,N)
#define ALL(A)		(A).begin(), (A).end()
#define zero(a)		memset((a),0,sizeof(a))
#define pb push_back
#define MP make_pair
#define sz size()

typedef vector<string> VS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef long long LL;
typedef long long longlong;

VS split(string text, char delim = ' ') {
  istringstream iss(text);
  VS res;
  string token;
  while (getline(iss, token, delim))
    res.pb(token);
  return res;
}

int main(){
  //freopen("input.txt","r",stdin);
  freopen("C-small-attempt0.in","r",stdin);
  freopen("C-small-attempt0.out","w",stdout);
  int T;
  scanf("%d", &T);
  For(tc, 1, T+1) {
    int N;
    scanf("%d", &N);
    VI nums;
    int num;
    Rep(i, N) {
      scanf("%d", &num);
      nums.pb(num);
    }
    int limit = (1<<nums.sz);
    int bestsuma = -1;
    Rep(n, limit) {
      int suma = 0, sumb = 0;
      int xsuma = 0, xsumb = 0;
      for(int i=1, j=0; j<nums.sz ; i<<=1, ++j)	
	if( (i & n) ) {
	  suma += nums[j];
	  xsuma ^= nums[j];
	} else {
	  sumb += nums[j];
	  xsumb ^= nums[j];
	}

      if(suma && sumb && xsuma == xsumb) {
	int t = max(suma, sumb);
	bestsuma = max(bestsuma, t);
      }
    }
    if(bestsuma == -1)
      printf("Case #%d: NO\n", tc);
    else
      printf("Case #%d: %d\n", tc, bestsuma);
  }
  	
  return 0;
}

