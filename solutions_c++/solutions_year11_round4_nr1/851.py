#include <stdio.h>
#include <vector>
#include "heap.h"


void main(void)
{
	FILE *f = fopen("A-large.in","r");

	int T;
	fscanf(f,"%d\n",&T);

	for(int t=0;t<T;t++)
	{
		int X,walk,run,time_,n;
		fscanf(f,"%d %d %d %d %d\n",&X,&walk,&run,&time_,&n);

		HEAPB<int,int> heap;
		heap.clear();
		double totaltime=0;
		int rest = X;
        for(int i=0;i<n;i++)
		{
			int x0,x1,speed;
			fscanf(f,"%d %d %d\n",&x0,&x1,&speed);
			int len = x1-x0;
            rest -= len;
			heap.additem(speed,len);
			totaltime += (double)len/(double)(walk+speed);
		};
		heap.additem(0,rest);
		totaltime += (double)rest/(double)walk;

		double time = time_;
		while(time>0 && heap.available())
		{
			int speed = heap.smallestvalue();
            int len = heap.smallest();
			heap.takesmallest();

			double timeon = (double)len / ((double)speed + (double)run);
			double runtime = timeon;
			if (runtime>time) runtime = time;

			time-=runtime;

			double savemeter = runtime *  ( (double)run - (double)walk );
			totaltime -= savemeter  / ((double)walk+(double)speed);
		};

		printf("Case #%d: %.9f\n",t+1,totaltime);
	};



};