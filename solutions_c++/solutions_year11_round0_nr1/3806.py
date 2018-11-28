#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <queue>
using namespace std;
int main () {
	int case_number = 0;
	scanf("%d", &case_number);
	for(int cn=1; cn<=case_number; cn++) {
		printf("Case #%d: ", cn);
		int n;
		scanf("%d", &n);
		int day = 0;
		int poses[2], days[2];
		for (int r=0; r<2; r++) {
			poses[r] = 1;
			 days[r] = 0;
		}
		for (int i=0; i<n; i++) {
			char tmp; int pos;
			scanf(" %c %d", &tmp, &pos);
			int r=(tmp-'B')/('O'-'B');
			//printf(" [%d: %d]", i , pos);
			day = days[r]=max(day, days[r]+abs(pos-poses[r]))+1;
			poses[r] = pos;
		}
		printf("%d\n", day);
	}
	return 0;
}
