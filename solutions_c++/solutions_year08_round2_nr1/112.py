#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <set>
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

long long px[1000100] , py[1000100];
int main() {
	int CC , nc , N ;
	long long res  , A , C , D , B , M , X , Y , x0 , y0;
		
	scanf("%d\n", &CC);
	for ( nc = 1 ; nc <= CC ; nc++) {
		cin >> N >> A >> B >> C >> D >> x0 >> y0 >> M;
		res = 0;
		px[0] = x0;
		py[0] = y0;
		X = x0 ; Y = y0;
		for (int i = 1 ; i < N ; i++) {
			X = ( A * X + B) % M;
			Y = ( C * Y + D) % M;
			px[i] = X;
			py[i] = Y;
		}
		int i , j , k;
		for (i = 0 ; i < N ; i++)
			for (j = i+1 ; j < N ; j++)
				for ( k = j+1 ; k < N ; k++) {
					X = px[i] + px[j] + px[k];
					Y = py[i] + py[j] + py[k];
					if ( X % 3 == 0 && Y % 3 == 0 )
						res++;
				}

		printf("Case #%d: %lld\n", nc , res );
	}	
	return 0;
}
