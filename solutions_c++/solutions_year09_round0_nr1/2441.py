#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std; 

#define all(x) (x).begin(),(x).end()
#define fore(it,x) for(typeof((x).begin()) it=(x).begin();it!=(x).end();it++)
#define sqr(x) ((x)*(x))
#define i64 long long
#define u64 unsigned long long
typedef vector<int> vi;typedef vector<vi> vvi;
typedef vector<string> vs;typedef vector<vs> vvs;
typedef vector<double> vd;typedef vector<vd> vvd;
typedef pair<int,int> pii;typedef vector<pii> vpii;
typedef set<int> si;typedef set<string> ss;
typedef set<char> sc;typedef set<pii> spii;

int cand[2000];
vs dic;
string aux;

int res;
/*
void create(int k , int n , string str){
	if ( k == n ){
		for ( int i = 0; i < dic.size() ; i++ ){
			if ( !str.compare(dic[i]) ){
				res++;
				return;
			}
		}
	} else {
		for ( int i = 0 ; i < aux.size() ; i++ ){
			if ( cand[i] == k ){
				create(k+1,n,str+aux[i]);
			}
		}
	}
}*/

void create(){
	int j;
	for ( int i = 0 ; i < dic.size() ; i++ ){

		for ( j = 0 ; j < dic[i].size() ; j++ ){
			int k = 0;
			while ( k < aux.size() ){
				if ( cand[k] == (j+1) && aux[k] == dic[i][j] ){
					break;
				}
				k++;
			}
			if ( k == aux.size() ){
				break;
			}
		}
		if ( j == dic[i].size() ){
			res++;
		}
	}
}

int main(int argc, char* argv[]){
	#ifndef ONLINE_JUDGE
	  if (freopen("input.txt", "r", stdin) == NULL)
		fprintf(stderr, "%s: cannot open input file: %s.\n", argv[0], "input.txt");
	  if (freopen("output.txt", "w", stdout) == NULL)
		fprintf(stderr, "%s: cannot open output file: %s.\n", argv[0], "output.txt");
	#endif
	
	int L, D , N ,n;
	int i , j;

	scanf("%d %d %d", &L, &D, &N);

	for ( i = 0 ; i < D ; i++ ){
		cin >> aux;
		dic.push_back(aux);
	}
	
	sort( all(dic) );

	for ( n = 1 ; n <= N ; n++ ){
		for ( i = 0 ; i < 500 ; ++i )
			cand[i] = 0;

		i = 0 ;
		j = 1 ;
		cin >> aux;
		while (  i < aux.size() ){
			if ( aux[i] == '(' ){
				i++;
				while ( i < aux.size() && aux[i] != ')' ){
					cand[i] = j;
					i++;
				}
				j++;
			} else {
				cand[i] = j++;
			}
			++i;
		}

		if ( j < n )
			printf("Case #%d: 0\n", n);
		else {
			res = 0;
			create();
			printf("Case #%d: %d\n", n , res);
		}
	}

	return 0;
}
