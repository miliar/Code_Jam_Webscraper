#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
#include <vector>
#include <list>
#include <ctype.h>
#include <stack>
#include <string>
#include <algorithm>
#include <sstream>
#include <queue>
using namespace std;
#define PB		push_back
#define ALL(v)		(v).begin() , (v).end()
#define SZ(v)		( (int) v.size() )
#define Set(v,x)	memset(  v , x , sizeof(v))
#define two(n)		( 1 << (n) )
#define contain(Set,i)  ( (Set) & two(i) )

struct word {
	char pal[20];
	int code[20];
} w[5100];

int c[20], nl;
bool ok(int i) {
	for (int j = 0 ; j < nl ; j++)
		if ( (c[j] & w[i].code[j])== 0 )
			return false;
	return true;
}

int main() {
	int i , j , t , nt , d;
	char pat[2000];

	cin >> nl >> d >> nt;
	for (i = 0 ; i < d ; i++) {
		scanf("%s\n", w[i].pal);
		for (j = 0 ; j < nl ; j++)
			w[i].code[j] |= two(w[i].pal[j]-'a');
	}
	for (t = 1 ; t <= nt ; t++) {
		scanf("%s\n", pat);
		Set(c,0);
		j = 0;
		for (i = 0 ; i < nl ; i++) {
			if (pat[j] != '(')
				c[i] = two(pat[j]-'a');
			else {
				while (pat[++j] !=')')
					c[i] |= two(pat[j]-'a');
			}
			j++;
		}
		j = 0;
		for (i = 0 ; i < d ; i++) {
			if (ok(i))
				j++;
		}
		printf("Case #%d: %d\n", t, j);
	}
	return 0;
}

