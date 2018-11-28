#include <cassert>
#include <cmath>
#include <cstdio>
#include <set>
#include <string>
#include <vector>
#include <time.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#pragma comment(linker, "/STACK:10000000")
using namespace std;


__int64 val[1000000];
vector<__int64> vn;
const __int64 inf = 2000000000000000000LL;
void prec()
{
	memset(val, 0, sizeof(val));
	for (int i=0;i<1000000;i++)
	{
		val[i] = inf;
		if (i == 0)
			val[i] = 0;
		for (int j=0;j<(int)vn.size();j++)
			if (vn[j] <= i)
				val[i] = min(val[i], val[i - vn[j]] + 1);
	}
}




int main()
{ 
/*	time_t ct = time(0);
	int dt =5*60 + 0*1800 +0*3600;//5*3600 + 1800;
	while (time(0) - ct < dt)
	{
		cout<<(dt + ct - time(0))<<' ';
	}
	for (;;)
	{
		cout<<char(7);
	}
	return 0;*/

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tn;
	cin>>tn;
	for (int aaa=0;aaa<tn;aaa++)
	{
		__int64 n;
		__int64 vl;
		cin>>vl;
		cin>>n;
		vn.resize(n);
		for (int i=0;i<n;i++)
			cin>>vn[i];
		prec();
		__int64 ans = vl + 1;
		for (int i=0;i<n;i++)
		{
			__int64 testb = vl / vn[i];
			__int64 vr = vl % vn[i];
			for (int j=0;j<10000;j++)
			{
				if (vr < 1000000)
				{
					__int64 test = testb + val[vr];
					ans = min(ans, test);
				}
				vr += vn[i];
				--testb;

/*				for (int k=i+1;k<n;k++)
				{
					__int64 testb2 = vr / vn[k];
					__int64 vrk = vr % vn[k];
					for (int jk=0;jk<100 && testb2 >= 0;jk++)
					{
						if (vrk < 1000000)
						{
							__int64 test = testb + testb2 + val[vrk];
							ans = min(ans, test);
						}
						vrk += vn[k];
						--testb2;
					}
				}*/
			}


		}

		if (ans == vl + 1)
			cout<<"Case #"<<aaa+1<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<aaa+1<<": "<<ans<<endl;
	}

	return 0;
}