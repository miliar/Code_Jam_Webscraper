#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <memory>
#include <cctype>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define FOR( i , a , n ) for (int i = (a); i <= (n) ; i++ )
#define REP( i , n ) for (int i = 0; i < (n) ; i++ )
#define debug(x) cout << #x" = " << x << "\n"
#define FORIT( i , c ) for ( __typeof((c).begin())  i  = (c).begin() ; (i) != (c).end() ; (i)++ )





void doProblemA(){
	int N,K,T;
	cin>>T;
	for(int t =1 ; t <= T; t++){
		cin>>N>>K;
		cout<<"Case #"<<t<<": ";
		if((K & ( (1<<N) - 1 )) ==(1<<N)-1) 
			cout<<"ON\n";
		else 
			cout<<"OFF\n";
		}
	
	





	
	}



int main() {
 doProblemA();
 return 0;
}
