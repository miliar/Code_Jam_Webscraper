//============================================================================
// Name        : B.cpp
// Author      : Artem A. Khizha
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdio>
#include <cmath>
using namespace std;

int main() {
    int tnum;
	scanf("%d", &tnum);
	for (int ti = 1; ti <= tnum; ti++) {
	    long long l, p, c;
	    int cnt = 0;
	    scanf("%lld%lld%lld", &l, &p, &c);
	    long long m = 1;
	    for (int i = 1; ; i++) {
	        m *= c;
	        if (m*l < p)
	            cnt++;
	        else
	            break;
	    }
	    if (cnt)
	        cnt = (int)log2(cnt)+1;
	    printf("Case #%d: %d\n", ti, cnt);
	}
	return 0;
}
