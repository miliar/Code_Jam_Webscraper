#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;


int main()
{
	int T;
	scanf("%d",&T);
	for(int Ti = 0;Ti <T ;Ti ++)
	{
		map<double,double> w;
		int X,S,R,t,N;
		scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);

		for(int i=0;i<N;i++)
		{
			int start,end,speed;
			scanf("%d%d%d",&start,&end,&speed);
			int len = end-start;
			w[speed+S] += len;
			X -= len;
		}
		w[S] += X;
	

		double restrun = t;
		double totaltime = 0;
		for(map<double,double>::iterator it=w.begin(); it!=w.end(); it++)
		{
			double speed;
			double timeneed;
			if(restrun == 0)
			{
				timeneed = it->second  /it->first;
				totaltime += timeneed;
			}
			else
			{
				speed = it->first + R - S;
				timeneed = it->second /speed;
				if(timeneed < restrun)
				{
					totaltime += timeneed;
					restrun -= timeneed;
				}
				else
				{
					totaltime += restrun + (it->second-speed*restrun)/ it->first ;
					restrun = 0;
				}
			}

		}
		printf("Case #%d: ",Ti+1);
		printf("%.9lf\n",totaltime);
	}
}
