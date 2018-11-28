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

int p[6];
char c;
char l[1009];
char t[1009];

int main(){
	int tcs;
	scanf("%d", &tcs);
	for(int tc=0; tc<tcs; ++tc){
		int k;
		scanf("%d", &k);
		for(char c='\0'; c != '\n'; c = getchar());
		fgets(l, sizeof(l), stdin);
		int s = strlen(l);
		for(int i=0; i<k; ++i)
			p[i] = i;

		int best = s;
		do{
			for(int i=0; i<s/k; ++i){
				for(int j=0; j<k; ++j){
					t[i*k + j] = l[i*k + p[j]];
				}
			}
			int th = 0;
			char old = t[0];
			for(int i=1; i<s; ++i){
				th += t[i] != old;
				old = t[i];
			}
			best = min(best, th);
		}while(next_permutation(p, p+k));
		printf("Case #%d: %d\n", tc+1, best);
	}
}
