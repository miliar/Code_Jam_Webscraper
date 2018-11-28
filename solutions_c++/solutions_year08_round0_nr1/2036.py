#include <map>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
map<string, int> smap;
int d[1001][101];
int main(void){
	char temp[200];
	int i,j,k,s,q,t;
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d", &t);
	for(int out=1; out<=t ;out++){
		memset(d, 0, sizeof(d));
		smap.clear();
		scanf("%d\n", &s);
		for(i=1; i<=s; i++){
			gets(temp);
			smap[temp] = i;
		}
		scanf("%d\n", &q);
		for(i=1; i<=q; i++){
			gets(temp);
			int v = smap[temp];
			for(j=1; j<=s; j++){
				if(j==v) d[i][j] = 12345;
				else d[i][j] = d[i-1][j];
				for(k=1; k<=s; k++)
					if(j!=k)
						d[i][j] = min(d[i][j], 1+d[i-1][k]);
			}
		}
		int Min = INT_MAX;
		for(i=1; i<=s; i++)
			Min = min(Min, d[q][i]);
		printf("Case #%d: %d\n", out, Min);
	}
}