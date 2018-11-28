/* Author - Rishi */
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
#define NT()               int nt;for(scanf("%d",&nt);nt;nt--)
#define SI                 ({int t;scanf("%d",&t);t;})

typedef map<int,int>    MI;
typedef pair<int,int>   PI;
typedef long long int   LL;
typedef V( int )        VI;
typedef V( VI )         VVI;
typedef V( PI  )        VPI;
typedef V( string )     VS;
typedef V( VS )         VVS;

int main(){
	int C=1;
	NT(){
		int n=SI,k=SI,b=SI,t=SI;
		V(PI ) a(n);
		REP(i,n)a[i].F=SI;
		REP(i,n)a[i].S=SI;
		int count=0;
		REP(i,n){
			int d=b-a[i].F;
			if(d<=t*a[i].S)
				count++;
		}
		if(count < k){
			cout<<"Case #"<<C++<<": "<<"IMPOSSIBLE\n";
			continue;
		}
		SORT(a);
		VI pos(n);
		REP(i,n){
			pos[i]=a[i].F+t*a[i].S;
		}
		count=0;
		for(int i=n-1;i>=0;i--){
			if(k==0)break;
			if(pos[i]>=b){
				k--;
				int s=a[i].F;
				FOR(j,i+1,n){
					if(pos[j]<b)
						count++;
				}
			}
		}
		cout<<"Case #"<<C++<<": "<<count<<endl;
	}
}
