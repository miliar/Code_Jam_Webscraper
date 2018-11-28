#define	_CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <assert.h>

struct Way	{
	int B,E,w;
	int length() const	{
		return E-B;
	}
	void read()	{
		scanf("%d%d%d",&B,&E,&w);
	}
};

static int cmp_way(const void *a, const void *b)	{
	return ((const Way*)a)->w - ((const Way*)b)->w;
}


int main()	{
	int i=0,T=0;
	scanf("%d",&T);
	Way way[1000];
	for(i=0; i<T; ++i)	{
		int X=0,S=0,R=0,N=0;
		double t=0.0;
		scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);
		int j; double walk=X;
		for(j=0; j<N; ++j)	{
			way[j].read();
			walk -= way[j].length();
		}
		double tw = walk / R;
		double time = 0.f;
		if(tw>=t)	{
			walk -= t*R;
			time += t;
			t = 0.0;
			time += walk / S;
		}else	{
			walk = 0.0;
			time += tw;
			t -= tw;
		}
		qsort(way,N,sizeof(Way),cmp_way);
		for(j=0; j<N; ++j)	{
			double dist = way[j].length();
			double speed = R+way[j].w;
			tw = dist / speed;
			if(tw>=t)	{
				dist -= t*speed;
				time += t;
				t = 0.0;
				time += dist / (S+way[j].w);
			}else	{
				dist = 0.0;
				time += tw;
				t -= tw;
			}
		}
		printf("Case #%d: %lf\n", i+1,time);
	}
	return 0;
}