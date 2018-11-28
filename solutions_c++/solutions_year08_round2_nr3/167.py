#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>

using namespace std;

#ifndef DEB
#define DEBUG(out)
#else
#define DEBUG(out) cerr << __LINE__ << ":\t" << out << endl
#endif

int buffer[6000];

int main(){
	int tcs;
	scanf("%d", &tcs);
	for(int tc=0; tc<tcs; ++tc){
		memset(buffer, -1, sizeof(buffer));
		int k;
		scanf("%d", &k);
		int r = k;
		int i=0;
		for(int z=0; z<k; ++z){
			DEBUG(z);
			int c = z%r;
			while(buffer[i] != -1)
				i = (i+1)%k;
			while(c){
				i = (i+1)%k;
				while(buffer[i] != -1)
					i = (i+1)%k;
				--c;
			}
			--r;
			buffer[i] = z;
		}
		printf("Case #%d:", tc+1);
		int n;
		scanf("%d", &n);
		while(n--){
			int q;
			scanf("%d", &q);
			printf(" %d", buffer[q-1]+1);
		}
		puts("");
	}
}
