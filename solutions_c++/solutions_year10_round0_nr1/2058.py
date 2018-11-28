#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<deque>
#include<algorithm>
using namespace std ;

typedef long long LL ;
typedef vector<int> VI ;
typedef pair<int,int> para ;

const int INF = 1000000000 ;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(i,c) for(__typeof((c).begin())i = (c).begin();i!=(c).end(); ++i)
#define ALL(x) x.begin(),x.end()

int D, n, k;

int main()
{
  scanf("%d",&D);	
	FOR(I,1,D){
    scanf("%d %d",&n,&k);
    printf("Case #%d: ", I);
    if(((k+1)&((1<<n)-1))==0)
      printf("ON\n");
    else
      printf("OFF\n");
  }
  return 0 ;
}

