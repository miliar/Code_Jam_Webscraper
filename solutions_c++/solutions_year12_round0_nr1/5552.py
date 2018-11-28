#include <iostream>
#include <sstream>
#include <bitset>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <numeric>
#define FOR(i,A) for(typeof (A).begin() i = (A).begin() ; i != (A).end() ; i++)
#define mp make_pair
#define clr(v,x) memset( v, x , sizeof v ) 
#define all(x) (x).begin() , (x).end()
#define rall(x) (x).rbegin() , (x).rend()
#define TAM 110

using namespace std;

typedef pair<int,int> ii ;
typedef long long ll ;
typedef pair<int,ii> pii ;

int main(){

	int test ;
	cin >> test ;
	cin.ignore() ;
	string path = "yhesocvxduiglbkrztnwjpfmaq" ;
	for(int k = 1 ; k <= test ; k++){
		string s ;
		getline( cin , s ) ;
		for(int i = 0 ; i < s.size() ; i++){
			if( s[ i ] == ' ' ) continue ;
			s[ i ] = path[ s[ i ] - 'a' ] ;
		}
		printf("Case #%d: %s\n" , k , s.c_str() ) ;
	}
	return 0 ;
}
