#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <map>
#include <complex>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <bitset>
#include <cassert>
using namespace std;

#define FOR(a,b,c) for(long long a=(long long)(b);a<(long long)(c);a++)
#define ITER(a,b) for(__typeof((b).begin()) a = (b).begin(); a!=(b).end(); a++)
#define SUBSET(a,b) for(long long a = b; a!=0; a = (b & (a-1)))
#define MEMSET(dest,val) memset(dest,val,sizeof(dest))
#define PAIR pair<long long,long long>
#define BEGEND(a) (a).begin(), (a).end()
#define SHIFT(v) (1LL<<(v))
#define SQ(a) ((a) * (a))
#define LSB(a,b) (b<=sizeof(a)?(b & (SHIFT(a)-1)):LLMAX)

#define eps 1E-9
#define PI acos(-1.0)
#define INF 1000000000
#define LLINF ((1LL<<62)-1)


int _T;
long long R, k, N;
vector<long long> G;
long long maxe[1000];
int next[1000];

int main(){
  cin >> _T;
  FOR(i,0,_T){
    cout << "Case #" << (i+1) << ": ";
    cin >> R >> k >> N;
    G.resize(N); FOR(j,0,N) cin >> G[j];
    FOR(j,0,N){
	long long left = k;
	maxe[j] = 0;
	FOR(j2,j,j+N){
	    int cur = j2%N;
	    if(left < G[cur]) break;
	    maxe[j]+=G[cur]; left-=G[cur];
	    next[j] = (cur+1)%N;
	}
    }
    long long cur = 0, times=R, money = 0;
    while(times-- > 0){
	money += maxe[cur];
	cur = next[cur];
    }
    cout << money;
    cout << endl;
  }
  return 0;
}

