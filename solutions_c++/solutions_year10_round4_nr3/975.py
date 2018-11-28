#include <vector>
#include <cassert>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include<string.h>
#include<math.h>
#include <climits>
#include <fstream>
#include <sstream>

using namespace std;

#define FOR(i,a,b)         for(int i= (int )a ; i < (int )b ; i++)
#define FORD(i,a,b)        for(int i= (int )a ; i >= (int )b ; i--)
#define REP(i,n)           FOR(i,0,n)
#define REPD(i,n)          FORD(i,n-1,0)
#define F                  first
#define S                  second
#define MP                 make_pair
#define PB                 push_back
#define PP                 pop()
#define EM                 empty()
#define INF                2000000000
#define PF                 push_front
#define ALL(x)             x.begin(),x.end()
#define SORT(x)            sort(ALL(x))
#define V(x)               vector< x >
#define PRINT(x)           cout << #x << " " << x << endl
#define SZ(x)              x.size();
#define PRV(v)             REP(Ind,v.size())cout<<v[Ind]<<" ";cout<<endl;
#define NT()               int nt;for(scanf("%d ",&nt);nt;nt--)
#define SI                 ({int t;scanf("%d",&t);t;})

typedef map<int,int>    MI;
typedef pair<int,int>   PI;
typedef long long int   LL;
typedef V( int )        VI;
typedef V( VI )         VVI;
typedef V( PI  )        VPI;
typedef V( string )     VS;
typedef V( VS )         VVS;

int a[101][101] , len=101 , b[101][101];

bool isE(){
	REP(i,len)REP(j,len)if(a[i][j]==1) return 0;
	return 1;
}


int main(){
        int C=1;
        NT(){
                int n=SI ;
                REP(i,len)REP(j,len)a[i][j]=0;
                REP(ii,n){
                        int x1=SI , y1=SI , x2=SI , y2=SI ;
                        FOR(i,min(x1,x2),max(x1,x2)+1)
                                FOR(j,min(y1,y2),max(y1,y2)+1)a[i][j]=1;
                }

		int ans=0, ii=0;
		while(!isE()){
			REP(i,len)REP(j,len){
				b[i][j]=a[i][j];
				if((i-1<0 or a[i-1][j]==0) && (j-1<0 or a[i][j-1]==0))
					b[i][j]=0;
				if(i-1>0 and a[i-1][j]==1 and j-1>0 and a[i][j-1]==1)
					b[i][j]=1;
			}
			REP(i,len)REP(j,len)a[i][j]=b[i][j];
			ans++;
					
		}		
		cout<<"Case #"<<C++<<": "<<ans<<endl;
        }
}
