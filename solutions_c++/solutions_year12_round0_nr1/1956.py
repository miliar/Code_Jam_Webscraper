#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;


typedef pair < int , int > pii;
typedef vector < int > vi;
typedef long long LL;


#define REP(i, a) for (int i = 0; i < a; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define mp make_pair
#define F first
#define S second
#define pb push_back
#define CLEAR(x, val) memset(x, val, sizeof(x))


int tc;

char pola[] = "yhesocvxduiglbkrztnwjpfmaq";

int main () {
	scanf("%d\n", &tc);
	
	char in[110];
	
	FOR(i, 1, tc) {
		gets(in);
		printf("Case #%d: ", i);
		REP(ii, (int)strlen(in)) {
			if (in[ii] == ' ') {
				printf(" ");
			}
			else {
				printf("%c", pola[in[ii] - 'a']);
			}
		}
		
		printf("\n");
	}
}
