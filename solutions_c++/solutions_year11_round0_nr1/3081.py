
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
  //freopen("A-small-attempt0.in","r",stdin);
  freopen("A-large.in","r",stdin);
  //freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int T;
  scanf("%d",&T);
  For(t, 1, T+1){
    int N;
    scanf("%d", &N);
    int op = 1, ot = 0, bp = 1, bt = 0;
    char robot; int pos;
    int time = 0;
    int moves=0;
    Rep(i, N) {
      cin>>robot>>pos;
      if( robot == 'O' ) {
	int steps = abs(op - pos);
	int since = time - ot;
	if( since >= steps) {
	  moves++;
	  time++;
	  ot = time;
	} else {
	  int tmp = abs(steps - since) + 1;
	  moves += tmp;
	  time += tmp;
	  ot = time;
	}
	op = pos;
      } else {
	int steps = abs(bp - pos);
	int since = time - bt;
	if( since >= steps) {
	  moves++;
	  time++;
	  bt = time;
	} else {
	  int tmp = abs(steps - since) + 1;
	  moves += tmp;
	  time += tmp;
	  bt = time;
	}
	bp = pos;
      }
    }
    printf("Case #%d: %d\n", t, moves);
  }
  	
  return 0;
}

