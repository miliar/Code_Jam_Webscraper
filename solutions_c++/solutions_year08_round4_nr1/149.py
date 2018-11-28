#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
using namespace std;
#define N 10010
#define M 1000000007
#define INF 9999999

struct node {
	int v, c, op;
	int f[2];
}p[N];
int m, v;

int main()
{
  int t, index, i, j;
  
  scanf("%d", &t);
  for(index = 1; index <= t; index++) {
    scanf("%d%d", &m, &v);
    for(i = 1; i <= (m-1)/2; i++) {
      scanf("%d%d", &p[i].op, &p[i].c);
  	}
  	for(; i <= m; i++)
	    scanf("%d", &p[i].v);
 	for(i = m; i > (m-1)/2; i--) {
 		p[i].f[p[i].v] = 0;
 		p[i].f[p[i].v^1] = INF;
 	}
  	for(i = (m-1)/2; i > 0; i--) {
  		int c[2][2];
  		p[i].f[0] = p[i].f[1] = INF;
  		c[0][0] = p[2*i].f[0]+p[2*i+1].f[0];
  		c[0][1] = p[2*i].f[1]+p[2*i+1].f[1];
  		if(p[2*i].f[1]+p[2*i+1].f[0] < c[0][1])
  			c[0][1] = p[2*i].f[1]+p[2*i+1].f[0];
  		if(p[2*i].f[0]+p[2*i+1].f[1] < c[0][1])
  			c[0][1] = p[2*i].f[0]+p[2*i+1].f[1];
   		c[1][0] = p[2*i].f[0]+p[2*i+1].f[0];
  		if(p[2*i].f[1]+p[2*i+1].f[0] < c[1][0])
  			c[1][0] = p[2*i].f[1]+p[2*i+1].f[0];
  		if(p[2*i].f[0]+p[2*i+1].f[1] < c[1][0])
  			c[1][0] = p[2*i].f[0]+p[2*i+1].f[1];
   		c[1][1] = p[2*i].f[1]+p[2*i+1].f[1];
   		
   		if(c[p[i].op][0] < p[i].f[0])
	     	p[i].f[0] = c[p[i].op][0];
   		if(c[p[i].op][1] < p[i].f[1])
 	    	p[i].f[1] = c[p[i].op][1];
     	if(p[i].c) {
	   		if(c[p[i].op^1][0]+1 < p[i].f[0])
		     	p[i].f[0] = c[p[i].op^1][0]+1;
	   		if(c[p[i].op^1][1]+1 < p[i].f[1])
	 	    	p[i].f[1] = c[p[i].op^1][1]+1;
     	}
  	}
  	if(p[1].f[v] < m)
	    printf("Case #%d: %d\n", index, p[1].f[v]);
 	else
	    printf("Case #%d: IMPOSSIBLE\n", index);
  }
}
