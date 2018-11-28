/*
TASK: A
LANG: C++
*/
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
typedef long long ll;
typedef long double ld;
#define sz(x) ((int)(x).size())


int main(){
	freopen("A-large.in","rt",stdin);
	freopen("Aa-large.out","wt",stdout);
	int cases = 0;
	scanf("%d",&cases);
	char p[51][51] ;
	
	for (int iii = 1; iii <= cases; iii++) {		
                int R,C;
		scanf("%d%d",&R,&C);
		for (int i = 0; i < R; i++) {
			scanf("%s",p[i]);
		}
		int res = 0;
		
		for (int i = 0; i < R && res != -1; i++){
			for (int j = 0; j < C && res != -1; j++) {
				if (p[i][j] == '#') {
					if (i + 1 >= R || j + 1 >= C){
						res = 	-1;			
					}
					if (p[i+1][j] == '#' && p[i][j+1] == '#' && p[i+1][j+1] == '#') {
						p[i][j] = '/';
						p[i+1][j] = '\\';
						p[i][j+1] = '\\';
						p[i+1][j+1] = '/';
					}else {
						res = -1;
					}
				}
			}
		}
		
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				if (p[i][j] == '#')
					res = -1;
		if (res == -1) 
			printf("Case #%d:\nImpossible\n",iii);
		else {
			printf("Case #%d:\n",iii);
			for (int i = 0; i < R; i++){
				for (int j = 0; j < C; j++)
					printf("%c",p[i][j]);
				printf("\n");
			}
		}
	}
	return 0;
}
