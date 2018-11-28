#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
#include <memory.h>

using namespace std;
#define MAXN 1001000
#define MAXV 210
int C, D;
double p[MAXV];
double v[MAXV];

int main()
{
	int cases;
	int casenum = 1;
	freopen("test", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while(cases--)
	{
		memset(p, 0, sizeof(p));
		memset(v, 0, sizeof(v));


		scanf("%d%d", &C, &D);
		for(int i = 0;i < C; i++){
			//read file
			int vnum, pos;
			scanf("%d%d", &pos, &vnum);
			p[i] = pos;
			v[i] = vnum;
		}

		double min = MAXN;
		double max = -MAXN;
		double now = -MAXN;
		for(int i=0; i<C; i++){
	       if(p[i] - now >= D){
	          now = p[i];
	       }
	       if(p[i] - now >= D){
		      now = p[i];
	       }
	       for(int j=0; j<v[i]; j++){
	    	   if(p[i] - now > max)
		            max = p[i] - now;
		       if(p[i] - now < min)
		            min = p[i] - now;
		       now += D;
		    }
		}
		if(min + max)
		     max -= ((max-min)/2);

		printf("Case #%d: %lf\n", casenum++, fabs(max));

	}
	return 0;
}

