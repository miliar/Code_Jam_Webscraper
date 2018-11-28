#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <list>
#include <algorithm>

using namespace std;

struct str_p 
{
	long double p;
	long double v;
};
	

int main()
{
	int t;
	cin >> t;

	for(int ii=1; ii<=t; ii++)
	{
		int c;
	    long double d;
		cin >> c >> d;
		str_p data[400];

		for(int j=0; j<c; j++)
		{
			long double p, v;
			cin >> p>>v;
			data[j].p= p;
			data[j].v = v;
		}

		long double out = -9999999.0;
		for(int i=0; i<c; i++)
		{
			long double tt = (long double)((data[i].v-1)*d)/2.0;
			if (tt > out) { out = tt;}
		}

		for(int i=0; i<c-1; i++)
		{
			for(int j=i+1; j<c; j++)
			{
				//sum vi to vj
				long double sum = 0;
				for(int k=i; k<=j; k++)
				{
					sum += data[k].v;
				}
				long double t1 = ((long double)(sum) - (data[i].v+data[j].v)/2) * d;
				long double t2 = (long double)(data[j].p) - data[i].p; 
				if ( t1 > t2)
				{
					long double sum2 = ((sum - 1) * d + data[i].p - data[j].p)/2.0;
					if (sum2 > out) { out = sum2;}
				}
			}
		}

		
		cout.precision(10);
		cout << "Case #"<<ii<<": "<<out<<endl;
	}
}
				

				

