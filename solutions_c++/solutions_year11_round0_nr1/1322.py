#include <stdio.h>
#include <math.h>

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t,n,p;
	char r;
	int o,b;
	int to,tb;
	int od,bd;
	scanf("%d",&T);
	for (t = 1;t <= T;t++)
	{
		scanf("%d",&n);
		o = b = 1;
		to = tb = 0;
		od = bd = 0;
		while (n--)
		{
			scanf(" %c%d",&r,&p);
			if(r == 'O'){
				if(abs(p - o) > bd)
					to += abs(p - o) + 1;
				else
					to += bd + 1;
				od += abs(p - o) + 1 - bd;
				if(od < 1)
					od = 1;
				bd = 0;
				o = p;
			}
			else if(r == 'B'){
				if( abs(p - b) > od)
					tb += abs(p - b) + 1;
				else
					tb += od + 1;
				bd += abs(p - b) + 1 - od;
				if(bd < 1)
					bd = 1;
				od = 0;
				b = p;
			}
		}
		printf("Case #%d: %d\n",t,to>tb?to:tb);
	}
	return 0;
}