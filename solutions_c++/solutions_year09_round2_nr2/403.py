#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cfloat>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <deque>
#include <list>
#include <algorithm>

#define loop(a, b) for(a = 0; a < b; ++a)
#define iter(a, b, c) for(a = b; a < c; ++a)

using namespace std;

int main(void) {
	char ln[128];
	int ds, len, i, tc = 1;
	scanf("%d ", &ds);
	while(ds--) {
		gets(ln);
		len = strlen(ln);
		loop(i, len) {
			if (!(ln[i] >= ln[i+1]))
				break;
		}
		printf("Case #%d: ", tc++);
		if (i == len) {
			strcat(ln, "0");
			sort(ln, ln+len+1);
			loop(i, len+1)
				if (ln[i] != '0')
					break;
			swap(ln[0], ln[i]);
			sort(ln+1, ln+len+1);
			puts(ln);
		} else {
			next_permutation(ln, ln+len);
			puts(ln);
		}
	}
	return 0;
}
