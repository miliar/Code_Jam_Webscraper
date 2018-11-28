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

string s;
int k;
char t[100000];

int grupos(int n ) {
	int r = 0 , i = 0 , j;
	while ( i < n ) {
		r++;
		j = i;
		while ( t[i] == t[j])
			i++;
	}
	return r;
}
int main() {
	int C , nc , res;
	
	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cin >> k >> s;
		int size = s.size();
		int i , j , v[10];
		for (i = 0 ; i < k ; i++)
			v[i] = i;
		res = -1;
		do {
			i = 0 ;
			while (i < size ) {
				for (j = 0 ; j < k ; j++)
					t[i+j] = s[i+v[j]];
				i += k;
			}
			t[size] = '\0';
			j = grupos(size);
	//		printf("%s  %d\n", t , j );
			if ( res == -1 || res > j )
				res = j;
		}while (next_permutation(v,v+k));

		printf("Case #%d: %d\n", nc , res );
	}	
	return 0;
}
