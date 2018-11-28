#include <stdio.h>
#include <stdlib.h>
#include "math.h"
#define rep(i,n) for(i=0;i<n;++i)
#define REP(i,s,n) for(i=s;i <n;++i)
int sum = 0;

/*void main2(FILE* in)
{
	int i,N,S,p;
	fscanf(in,"%d %d %d", &N, &S, &p);
	int *total = (int *)malloc(N*sizeof(int));
	rep(i,N)
		fscanf(in,"%d", &total[i]);
	int k,a,b,c,z,spLarge,nspLarge;
	rep(i,N)
	{
		k=S> 0 ?0:1;
		z = spLarge = nspLarge = 0;
		for(a = (int)((ceil)((float)(total[i] - 4 + 2*k)/3.0));
			a <= (int)((floor)((float)(total[i])/3.0));
			++a)
		{
			if(a < 0)
				continue;
			z = 0;
			k = S> 0 ? 0:1;
			while(1)
			{
				if(z > 2-k)
					break;
				b = a + z;
				z++;
				c = total[i] -a -b;
				if(c < b)
					continue;
				if(b > 10 || c > 10 || c-a > 2-k || c-b > 2-k || b-a > 2-k)
					continue;
				if((a >= p || b>= p || c>= p)) 
				{
					if(b - a == 2 || c - b == 2 || c - a == 2)
					{
						spLarge ++;
					}
					else{
						nspLarge++;
					}
				}
			}
		}
		if(nspLarge > 0 || (spLarge> 0 && S>0))
			sum++;
		if(nspLarge <= 0 && spLarge > 0)
			S--;
	}
}*/


void main3(FILE* in)
{
	int A,B,j,n,m,digits,i,*pair, inc = 0;
	fscanf(in,"%d %d",&A, &B);
	digits = (ceil)(((float)log((double)B))/(float)log((double)10));
	REP(n,A,B)
	{
		pair = (int*)malloc(sizeof(int)*(digits-1));
		rep(j,digits-1)
			pair[j] = -1;
		REP(i,1,digits)
		{
			inc = 1;
			m = (n%(int)pow((double)10,i))* pow((double)10,digits-i) + n/pow((double)10,i);
			if(m > n && m <= B)
			{
				rep(j,digits-1)
				{
					if(pair[j] == -1)
					{
						pair[j] = m;
						inc = 1;
						break;
					}
					if(m == pair[j])
					{
						inc = 0;
						break;
					}
				}
				if(inc)
					sum++;
			}
		}
		free(pair);
	}
}

int main(int argc, char** argv)
{
	int T,i;
	FILE* in = fopen(argv[1], "r");
	FILE*out = fopen("abc.txt","w");
	fscanf(in,"%d",&T);
	if(1 <= T && T<= 50)
	{
		rep(i,T){
			sum = 0;
			main3(in);
			if(i == T -1)
				fprintf(out,"Case #%d: %d",i+1,sum);
			else
				fprintf(out,"Case #%d: %d\n",i+1,sum);
		}
	}
	return 0;
}
