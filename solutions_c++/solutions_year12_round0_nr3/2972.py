#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <iostream>
#include <list>
#include <deque>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

#define MM 2000020

int a[MM], i, j,  sum;
char g[20];
int po[]={1,10,100,1000,10000,100000,1000000,10000000};
bool zz[MM];
int main (){
	int t, x, y;
	scanf("%d", &t);
	for(int cc=1;cc<=t;++cc){
		scanf("%d%d", &x, &y);
		sum=0;
		for(int k=x;k<y;++k){
			sprintf(g,"%d", k);
			int n=strlen(g);
			int z=k;
			int w;
			memset(zz,1,sizeof(zz));
			for(i=1;i<n;++i){
				w=z%10;
				z/=10;
				z+=w*po[n-1];
				// printf("%d %d\n", k, z);
				if(k<z&&z<=y){
					if(zz[z]){
						sum++;
						zz[z]=0;
					}
				}
			}
		}
		printf("Case #%d: %d\n", cc, sum);
	}
	
	
	return 0;
}
