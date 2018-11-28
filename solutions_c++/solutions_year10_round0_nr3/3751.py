#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <queue>

using namespace std;
queue<int>				q;
int main (void)
{
	int				t,T,r,k,n,i,g,res = 0,sum,cnt;
	freopen ("C-small.in","r",stdin);
	freopen ("C-small.out","w",stdout);
	scanf ("%d",&T);
	
	for (t=1;t<=T;++t){
		printf ("Case #%d: ",t);
		scanf ("%d%d%d",&r,&k,&n);
		while (!q.empty())q.pop();
		for (i = 0;i < n; ++ i){
			scanf ("%d",&g);
			q.push(g);
		}
		res = 0;
		for (i = 0; i < r; ++ i){
			sum = 0;
			cnt = 0;
			while (!q.empty()){
				g = q.front();
				if (sum + g > k){
					break;
				}else {
					res += g;
					sum += g;
					q.push(g);
					q.pop();
					cnt++;
				}
				if (cnt == n)break;
			}
		}
		printf ("%d\n",res);
	}
	return 0;
}