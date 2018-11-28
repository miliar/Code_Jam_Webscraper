#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

struct walkway
{
	int b,e,w;
}W[1001];

int X,S,R,N,t;

bool func(walkway a, walkway b)
{	
	return a.w < b.w;
}

int main()
{
	int te,Te;
	cin >> Te;
	for(int te=1 ; te<=Te ; te++)
	{
		cout << "Case #" << te << ": ";
		cin >> X >> S >> R >> t >> N;
		for(int i=0 ; i<N ; i++) cin >> W[i].b >> W[i].e >> W[i].w;
		sort(W, W+N, func);

		long double rem = X;
		for(int i=0 ; i<N ; i++) rem -= (W[i].e - W[i].b);
		
		long double res = 0,rtime = 0;
		if(rem >= R*t*1.0)
		{
			res += t;
			rem -= R*t;
			res += rem/S;
		}
		
		else
		{
			res += rem/R;
			rtime = t - rem/R;
		}
		
		
		int i=0;
		while(i<N)
		{
			long double rt = (W[i].e - W[i].b)*1.0/(R + W[i].w);
			if(rt <= rtime)
			{
				rtime -= rt;
				res += rt;
			}

			else
			{
				res += rtime;
				long double dist_left = (W[i].e - W[i].b) - (R + W[i].w) * rtime;
				res += dist_left/(S + W[i].w);
				rtime = 0;
			}
			i++;
		}
		
		printf("%.7llf\n",res);
	}
}
