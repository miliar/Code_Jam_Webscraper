#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <iostream>

#define LL long long

using namespace std;

struct Inter
{
	double b, e, w;
	
	bool operator<(const Inter& i) const
	{
		return w < i.w;
	}
};

int main()
{
	int Q;
	scanf("%d", &Q);
	
	for (int q = 1; q <= Q; ++q)
	{
		printf("Case #%d: ", q);
		
		double X, S, R, T;
		int N;
		double res = 0;
		scanf("%lf%lf%lf%lf%d", &X, &S, &R, &T, &N);
		
		double p = 0;
		vector<Inter> vet;
		for (int i = 0; i < N; ++i)
		{
			Inter inter;
			scanf("%lf%lf%lf", &inter.b, &inter.e, &inter.w);
			vet.push_back(inter);
			double e = inter.e;
			if (inter.b-p > 1e-9)
			{
				inter.e = inter.b;
				inter.b = p;
				inter.w = 0;
				vet.push_back(inter);
			}
			p = e;
		}
		if (X-p > 1e-9)
		{
			Inter inter;
			inter.e = X;
			inter.b = p;
			inter.w = 0;
			vet.push_back(inter);
		}
		
		sort(vet.begin(), vet.end());
		for (int i = 0; i < (int) vet.size(); ++i)
		{
			Inter inter = vet[i];
			double time = (inter.e-inter.b)/(R+inter.w);
			if (time <= T)
			{
				res += time;
				T -= time;
				p = inter.e;
			}
			else
			{
				double delta = T*(R+inter.w);
				res += T;
				T = 0;
				p = inter.b+delta;
			}
			res += (inter.e-p)/(S+inter.w);
		}
		printf("%lf\n", res);
	}
	
	return 0;
}

