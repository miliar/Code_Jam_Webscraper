#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<climits>
#include<algorithm>
#include<set>
#include<math.h>
#include<map>
#include<time.h>
#include<fstream>
#include<sstream>

#define FOR(i ,  n) \
	for(i = 0; i < n; i++)
#define FORI(i ,startForIndex , endForIndex) \
	for(i = startForIndex ;i < endForIndex; i++)
#define FORD(i ,startForIndex , endForIndex) \
	for(i = startForIndex - 1;i >= endForIndex; i--)
#define tr( container , it) \
	for( typeof(container.begin()) it = container.begin() ; it != container.end() ; it++ ) 
#define print1(ar) \
	for( typeof(ar.begin()) it = ar.begin() ; it != ar.end(); it++){\
		cout << * it << " " ;\
	}printf("\n") ;
#define print2(ar)\
	for( typeof(ar.begin()) it = ar.begin() ; it != ar.end(); it++){\
		for(typeof(it->begin()) itt = it->begin() ; itt !=  it->end() ; itt++ ){\
			cout << * itt << " " ;\
		}printf("\n") ;\
	}printf("\n");
#define ALL(ar)\
	ar.begin() , ar.end()
#define PB push_back
#define LL long long int 
#define VI	vector < int > 
#define VVI 	vector < VI >  
#define VVVI 	vector < VVI > 
#define VS	vector < string >
#define VL	vector < LL > 
#define VVL 	vector < VL >
#define V(i) 	vector < i >
#define VV(i) 	vector < vector < node > > 
#define pi(var)	cout << #var << " = " << var << endl ;
#define si(var)	scanf("%d" , &var)
using namespace std ;

int go(string &ar) {
	int i ,fl= 0; 
	FOR(i,ar.size()-1){
		if(ar[i] != ar[i+1]) {
			fl = 1; 
			break ;
		}
	}
	return fl ;
}



int main(){
	int i , t , j , tmp, n, m , k , cnt , fl, ind, dotfl , ffl;
	cin >> t ; 
	FOR(k,t) {
		dotfl = ffl = 0  ;
		VS ar(4) ;
		string artmp ;
		FOR(i,4) {
			cin >> ar[i] ;
		}
		FOR(i,4) {
			artmp.clear() ;
			fl =0 ;
			FOR(j,4) {
				if( ar[i][j] == '.') {
					dotfl = 1 ;
					fl = 1; 
					break ;
				}
				else if(ar[i][j] != 'T') {
					artmp.PB(ar[i][j]);
				}
			}
			if( fl == 1) {
				continue ;
			}
			fl = go(artmp) ;
			if(fl == 0) {
				printf("Case #%d: %c won\n", k+ 1 , artmp.c_str()[0]) ;
				ffl = 1;
				break ;
			}
		}
		if( ffl == 1) {continue ;}
		FOR(i,4) {
			artmp.clear() ;
			fl =0 ;
			FOR(j,4) {
				if( ar[j][i] == '.') {
					dotfl = 1 ;
					fl = 1; 
					break ;
				}
				else if(ar[j][i] != 'T') {
					artmp.PB(ar[j][i]);
				}
			}
			if( fl == 1) {
				continue ;
			}
			fl = go(artmp) ;
			if(fl == 0) {
				printf("Case #%d: %c won\n", k+ 1 , artmp.c_str()[0]) ;
				ffl = 1;
				break ;
			}
		}
		if( ffl == 1) {continue ;}
		

		artmp.clear() ;
		fl = 0;
		FOR(i,4) {
			if(ar[i][i] == '.') {
				fl = 1 ;
				break ;
			}
			if(ar[i][i] != 'T') {
				artmp.PB(ar[i][i]) ;
			}
		}
		if( fl == 0 and go(artmp) == 0)  {
			printf("Case #%d: %c won\n", k+ 1 , artmp.c_str()[0]) ;
			ffl = 1;
		//	break ;
		}
		if( ffl == 1) {continue ;}
		
		artmp.clear() ;
		fl = 0 ;
		FOR(i,4) {
			if(ar[3 -i][i] == '.') {
				fl = 1 ;
				break ;
			}
			else if(ar[3 -i][i] != 'T') {
				artmp.PB(ar[3-i][i]) ;
			}
		}
		if( fl == 0 and go(artmp) == 0)  {
			printf("Case #%d: %c won\n", k+ 1 , artmp.c_str()[0]) ;
			ffl = 1;
		//	break ;
		}

		if( ffl == 0) {
			printf("Case #%d: ", k+1 ) ;
			if( dotfl == 1) {
				printf("Game has not completed\n");
			}
			else {
				printf("Draw\n")  ;
			}
		}
	}
}
