#include<stdio.h>
#include<queue>
#include<vector>
#include<stdlib.h>

using namespace std;

typedef struct TTime
{
	int d;
	int a;
}tim;

int compare (const void *a, const void *b)
{
	tim *x = (tim*)a;
	tim *y = (tim*)b;
	return x->d - y->d;
}

int Compare( const void *a, const void *b)
{
	return *(int*)a - *(int*)b;
}

int main()
{
	int n,test,i,t,NA,NB,PA,PB;
	int h1,m1,h2,m2;
	int ka,kb,ca,cb,T;
	tim A[105],B[105];
	priority_queue < int , vector < int > , greater < int > > a;
	priority_queue < int , vector < int > , greater < int > > b;
	
	scanf("%d",&n);
	for(test = 1; test <= n;test++)
	{
		scanf("%d",&t);
		scanf("%d %d",&NA,&NB);
		for(i=0;i<NA;i++)
		{
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			A[i].d = h1*60 + m1;
			A[i].a = h2*60 + m2;
		}
		for(i=0;i<NB;i++)
		{
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			B[i].d = h1*60 + m1;
			B[i].a = h2*60 + m2;
		}
		
		if (NA > 0)
			qsort(A,NA,sizeof(tim),compare);
		if (NB > 0)
			qsort(B,NB,sizeof(tim),compare);
			
		PA = 0;
		PB = 0;
		ka = 0;
		kb = 0;
		ca = 0;
		cb = 0;
		
		while((PA < NA)&&(PB < NB))
		{
			if (A[PA].d < B[PB].d)
			{
				T = A[PA].d;
				while((a.size()>0)&&(T >= a.top()+t))
				{
					ka++;
					a.pop();
				}
				b.push(A[PA].a);
				ka--;
				if (ka < 0)
				{
					ka = 0;
					ca++;
				}
				PA++;
			}
			else
			{
				T = B[PB].d;
				while((b.size()>0)&&(T >= b.top()+t))
				{
					kb++;
					b.pop();
				}
				a.push(B[PB].a);
				kb--;
				if (kb < 0) 
				{
					kb = 0;
					cb++;
				}
				PB++;
			}
		}
		
		while(PA < NA)
		{
			T = A[PA].d;
			while((a.size()>0)&&(T >= a.top()+t))
			{
				ka++;
				a.pop();
			}
			b.push(A[PA].a);
			ka--;
			if (ka < 0)
			{
				ka = 0;
				ca++;
			}
			PA++;
		}
		
		while(PB < NB)
		{
			T = B[PB].d;
			while((b.size()>0)&&(T >= b.top()+t))
			{
				kb++;
				b.pop();
			}
			a.push(B[PB].a);
			kb--;
			if (kb < 0)
			{
				kb = 0;
				cb++;
			}
			PB++;
		}
		while(a.size()>0) a.pop();
		while(b.size()>0) b.pop();
		printf("Case #%d: %d %d\n",test,ca,cb);
	}
	while(getchar()!=EOF);
	return 0;
}
