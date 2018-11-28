
#include <stdio.h>

#define fi(a,b) for ( i = a; i < b; ++i )
#define fj(a,b) for ( j = a; j < b; ++j )
#define fo(a,b) for ( o = a; o < b; ++o )

int i,j,o;
int n,k,t;
char ch;
int po,pb,to,tb,time;
int d;

int main(){
	scanf("%d",&t);
	fo(0,t)
	{
		po = 1;
		pb = 1;
		to = 0;
		tb = 0;
		time = 0;
		scanf("%d",&n);
		fi(0,n)
		{
			scanf(" %c %d",&ch,&k);
			switch (ch)
			{
			case 'O': 
				d = k - po;
				if (d < 0) d *= -1;
				if (d > time - to)
				{
					time += d - time + to;
				}
				time++;
				po = k;
				to = time;
				break;
			case 'B': 
				d = k - pb;
				if (d < 0) d *= -1;
				if (d > time - tb)
				{
					time += d - time + tb;
				}
				time++;
				pb = k;
				tb = time;
				break;
			}
		}

		printf("Case #%d: %d\n",o+1,time);
	}
	return 0;
}