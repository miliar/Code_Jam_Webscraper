#include <stdio.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
#define PB		push_back
#define ALL(v)		(v).begin() , (v).end()
#define SZ(v)		( (int) v.size() )
#define Set(v,x)	memset(  v , x , sizeof(v))
#define two(n)		( 1 << (n) )
#define contain(Set,i)	( ( (Set) & two(i) ) !=0 )
typedef long long LL;
const int MAXT = 24*60;

int A , B , NA , NB , T , chegaA[MAXT+100] , chegaB[MAXT+100];
vector< int > partidaA[MAXT+100] , partidaB[MAXT+100];

void solve() {
	int t , numA = 0 , numB = 0;
	A = B = 0;
	for ( t = 0 ; t < MAXT ; t++) {
		numA += chegaA[t];
		numB += chegaB[t];

		for ( size_t i = 0 ; i < partidaA[t].size() ; i++) {
			if ( numA == 0 )	A++;
			else			numA--;
			chegaB[ partidaA[t][i] + T ]++;
		}
		for ( size_t i = 0 ; i < partidaB[t].size() ; i++) {
			if ( numB == 0 )	B++;
			else			numB--;
			chegaA[ partidaB[t][i] + T ]++;
		}
	}
}
int main()
{
	int nc , C , i , j , k , p ;
	string x , y;
	cin >> C;
	for (nc = 1 ; nc <= C ; nc++) {
		Set( chegaA , 0 ) ;
		Set( chegaB , 0 ) ;
		for (i = 0 ; i < MAXT ; i++) {
			partidaA[i].clear();
			partidaB[i].clear();
		}
		cin >> T >> NA >> NB;
		for (i = 0 ; i < NA ; i++) {
			cin >> x >> y;
			x[2] = ' ';
			y[2] = ' ';
			stringstream sx(x);
			sx >> j >> k;
			j = j * 60 + k;

			stringstream sy(y);
			sy >> k >> p;
			partidaA[j].PB( k * 60 + p );
		}
		for (i = 0 ; i < NB ; i++) {
			cin >> x >> y;
			x[2] = ' ';
			y[2] = ' ';
			stringstream sx(x);
			sx >> j >> k;
			j = j * 60 + k;

			stringstream sy(y);
			sy >> k >> p;
			partidaB[j].PB( k * 60 + p );
		}
		solve();
		printf("Case #%d: %d %d\n", nc , A , B );
	}
	return 0;
}
