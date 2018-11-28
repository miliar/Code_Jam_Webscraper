#define debug if(1)
// Grzegorz Guspiel
#include <iostream>
#include <vector>
#include <cassert>
#include <cstring>
#include <cmath>
#include <sstream>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(ii,nn) for(int (ii)=0; (ii)<int(nn); (ii)++)
#define FOR(ii,bb,ee) for(int (ii)=(bb); (ii)<=(ee); (ii)++)
#define REPD(ii,nn) for(int (ii)=(nn)-1; (ii)>=0; (ii)--)
#define FORD(ii,ee,bb) for(int (ii)=(ee); (ii)>=(bb); (ii)--)
#define FORE(ii,vv) for(__typeof((vv).begin()) ii=(vv).begin(); (ii)!=(vv).end(); (ii)++)
#define st first
#define nd second
#define pb push_back
#define pp pop_back
#define mp make_pair
int stmp; 
#define scanf stmp=scanf

// In g++, you can use the little known __uint128_t type.

char from[] = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvyeq";
char to[] = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upaoz";

char t[255];
char e[255];
char buf[1000];

int main() {
	int n = strlen(from);
	REP(i,n) t[from[i]] = to[i];
	for(char i = 'a'; i <= 'z'; i++) e[t[i]] = 1;
	char m;
	for(char i = 'a'; i <= 'z'; i++) if(!e[i]) m = i;
	for(char i = 'a'; i <= 'z'; i++) if(!t[i]) t[i] = m;
	int z; scanf("%d\n", &z);
	FOR(zz,1,z) {
		printf("Case #%d: ", zz);
		fgets(buf,1000,stdin);
		for(int i = 0; buf[i]; i++) buf[i] = t[buf[i]];
		printf("%s\n", buf);
	}
	return 0;
}
