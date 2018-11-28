#include <cstdio>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <climits>

using namespace std;

int matrix[100][100];
int h[100][25];

int wno[16];
unsigned best[1<<16];

int main(){
	int tc, tcN;
	
	scanf("%d", &tcN);
	for(tc=1; tc<=tcN; ++tc){
		int n, k;
		scanf("%d %d", &n, &k);
		for(int i=0; i<n; ++i)
			for(int j=0; j<k; ++j)
				scanf("%d", &h[i][j]);
		for(int i=0; i<n; ++i){
			for(int j=0; j<n; ++j){
				bool ok = true;
				for(int l=0; l<k; ++l)
					ok = ok && (h[i][l] != h[j][l]);
				for(int l=0; l<k-1; ++l)
					ok = ok && (h[i][l] < h[j][l]) == (h[i][l+1] < h[j][l+1]);
				matrix[i][j] = ok;
			}
			matrix[i][i] = true;
		}
		
		memset(best, 255, sizeof(best));
		for(int i=0; i<n; ++i){
			wno[i] = 0;
			for(int j=0; j<n; ++j){
				if(!matrix[i][j])
					wno[i] |= 1<<j;
			}
		}

		for(int i=0; i<1<<n; ++i){
			bool good = true;
			for(int j=0; good && j<n; ++j){
				if(1<<j & i && wno[j] & i)
					good = false;
			}
			if(good)
				best[i] = 1;
		}
		for(int a=0; a<1<<n; ++a){
			if(best[a] == n-1)
				continue;
			for(int i=a+1; i<1<<n; ++i){
				if((i & a) != a)
					continue;
				if(best[i|a] <= best[a] + 1)
					continue;
				int test = i ^ a;
				bool good = true;
				for(int j=0; good && j<n; ++j){
					if(1<<j & test && wno[j] & test)
						good = false;
				}
				if(good)
					best[i|a] = min(best[i|a], best[a] + 1);
			}
		}
		if(best[(1<<n)-1] != UINT_MAX)
			printf("Case #%d: %d\n", tc, best[(1<<n)-1]);
		else
			printf("Case #%d: %d\n", tc, n);
	}
}
