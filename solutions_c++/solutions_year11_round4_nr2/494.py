#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long int64;

int r,c,d;
char w[500][509];
int rs[500][500],cs[500][500];

int main() {
	int tests;
    freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    scanf("%d",&tests);
    for (int test=1;test<=tests;test++) {
    	cerr << test << endl;
    	scanf("%d %d %d",&r,&c,&d);
    	for (int i=0;i<r;i++) scanf("%s",w[i]);
    	for (int i=0;i<r;i++) {
    		for (int j=0;j<c;j++) {
    			rs[i][j]=(j>0?rs[i][j-1]:0)+d+w[i][j]-'0';
    			cs[i][j]=(i>0?cs[i-1][j]:0)+d+w[i][j]-'0';
    		}
    	}
    	for (int s=min(r,c);s>=3;s--) {
    		for (int i=0;i+s<=r;i++) {
    			for (int j=0;j+s<=c;j++) {
    				int64 w1,w2;
    				int ok=1;
    				if (s&1) { // liho
    					w1=0; w2=0;
    					for (int k=1;2*k<s;k++) {
    						int c1=j+s/2-k, c2=j+s/2+k;

    						int col1=cs[i+s-1][c1] - (i>0?cs[i-1][c1]:0);
    						int col2=cs[i+s-1][c2] - (i>0?cs[i-1][c2]:0);
    						w1+=col1*(k); w2+=col2*(k);
    					}
    					w1-=(s/2)*(2*d+w[i][j]-'0'+w[i+s-1][j]-'0');
    					w2-=(s/2)*(2*d+w[i][j+s-1]-'0'+w[i+s-1][j+s-1]-'0');
    					if (w1!=w2) { ok=0; continue; }

    					w1=0; w2=0;
    					for (int k=1;2*k<s;k++) {
    						int r1=i+s/2-k, r2=i+s/2+k;
    						int row1=rs[r1][j+s-1] - (j>0?rs[r1][j-1]:0);
    						int row2=rs[r2][j+s-1] - (j>0?rs[r2][j-1]:0);
    						w1+=row1*(k); w2+=row2*(k);
    					}
    					w1-=(s/2)*(2*d+w[i][j]-'0'+w[i][j+s-1]-'0');
    					w2-=(s/2)*(2*d+w[i+s-1][j]-'0'+w[i+s-1][j+s-1]-'0');
    					if (w1!=w2) { ok=0; continue; }

    				} else { // sodo
    					w1=0; w2=0;
    					for (int k=0;2*k<s;k++) {
    						int c1=j+s/2-1-k, c2=j+s/2+k;
    						int col1=cs[i+s-1][c1] - (i>0?cs[i-1][c1]:0);
    						int col2=cs[i+s-1][c2] - (i>0?cs[i-1][c2]:0);
    						w1+=col1*(1+k*2); w2+=col2*(1+k*2);
    					}
    					w1-=(s-1)*(2*d+w[i][j]-'0'+w[i+s-1][j]-'0');
    					w2-=(s-1)*(2*d+w[i][j+s-1]-'0'+w[i+s-1][j+s-1]-'0');
    					if (w1!=w2) { ok=0; continue; }

    					w1=0; w2=0;
    					for (int k=0;2*k<s;k++) {
    						int r1=i+s/2-1-k, r2=i+s/2+k;
    						int row1=rs[r1][j+s-1] - (j>0?rs[r1][j-1]:0);
    						int row2=rs[r2][j+s-1] - (j>0?rs[r2][j-1]:0);
    						w1+=row1*(1+k*2); w2+=row2*(1+k*2);
    					}
    					w1-=(s-1)*(2*d+w[i][j]-'0'+w[i][j+s-1]-'0');
    					w2-=(s-1)*(2*d+w[i+s-1][j]-'0'+w[i+s-1][j+s-1]-'0');
    					if (w1!=w2) { ok=0; continue; }
    				}
    				if (ok) {
    					printf("Case #%d: %d\n",test,s);
    					goto finish;
    				}
    			}
			}
    	}
    	printf("Case #%d: IMPOSSIBLE\n",test);
    	finish:;
    }
    return 0;
}
