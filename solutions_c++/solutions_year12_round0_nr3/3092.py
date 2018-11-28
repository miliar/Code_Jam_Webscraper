#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <cassert>
#include <map>
#include <stack>

#define FOR(I,A,B) for(int I=(A);I<(B);I++)
#define REP(I,N) FOR(I,0,N)
#define ALL(A) (A).begin(),(A).end()

#define SQR(x) ((x)*(x))
#define PB(x) push_back(x)

#define PI (acos(-1.0))

using namespace std;
int cnt = 0;
typedef vector<int> VI;
typedef vector< vector<int> > VVI;
set<pair<int,int> > ans;
int nextNumber(int x){
	vector<int> s;
	do{
		s.push_back( x % 10 );
		x /= 10;
	}while( x > 0);
	int temp = s[0];
	for(int i = 0;i < s.size()-1;i++){
		s[i] = s[i+1];
	}
	s[s.size()-1] = temp;
	int next = 0;
	for(int i = s.size()-1 ; i >= 0;i--){
		next = next*10 + s[i];
	}
	return next;
}
int main(){
	int t,k = 1;
	cin>>t;
	while(t--){
		if( !ans.empty() ) ans.clear();
		int cnt = 0;
		int lh,rh;
		cin>>lh>>rh;
		for(int i = lh;i <= rh;i++){
			int t = i;
			int j = i;
			while( t > 0 ){
				j = nextNumber(j);
				t /= 10;
				if( i == j ) continue;
				if( lh <= j && j <= rh)
					ans.insert( make_pair(min(i,j),max(i,j)));
			}
		}
		printf("Case #%d: %d\n",k++,ans.size());
	}
	return 0;
}

