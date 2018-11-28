#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)

void solve(char* str2, int index) {
	register int ind;
	ind = index;
    char* kG_string = (char *)malloc(100*sizeof(char));
    gets(kG_string);
    int length;
	int l =0;
	int letter;
	length = strlen(kG_string);

	if(length != 0) {
 		printf("Case #%d: ", ind);
         while (l<length) {
			if(*(kG_string+l) == ' ') {
				printf("%c",' ');
			} else {
				letter = *(kG_string+l) - 'a';
		        printf("%c", str2[letter]);
			}
			l++;
		}
		printf("\n");      
		free(kG_string);
	}
}      



int main() {
	freopen("C:/Projects/CodeJam/A-small-attempt1.in", "rt", stdin);
	freopen("C:/Projects/CodeJam/output_final.txt", "wt", stdout);
    char str2[256] = "yhesocvxduiglbkrztnwjpfmaq";
	int tt;
	scanf("%d", &tt);
	forn(ii, tt+1) {
		solve(str2, ii);
	}
	return 0;
}
