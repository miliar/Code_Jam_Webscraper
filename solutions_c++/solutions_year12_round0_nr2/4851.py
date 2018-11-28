#include <iostream>
#include <algorithm>
#include <cstdio>
#include <memory>
#include <string.h>
using namespace std;

int v1[] = {0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9,  9,  9, 10, 10, 10};
int v2[] = {0, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 10};

int main()
{
    int nn;
    scanf("%d\n", &nn);
    for (int ii = 1; ii <= nn; ++ii) {
    	int n, s, p;
    	int v[128];
    	scanf("%d%d%d", &n, &s, &p);
    	for (int i = 0; i < n; ++i) {
        	scanf("%d", v + i);
    	}
    	sort(v, v + n);

    	int res = 0;
    	for (int i = n-1, k = s; i >= 0; --i) {
    		if (v1[v[i]] >= p) {
    			// OK
    			++res;
    		} else if (k > 0 && v2[v[i]] >= p) {
    			--k;
    			++res;
    		}
    	}

    	printf("Case #%d: %d\n", ii, res);
    }

	return 0;
}
