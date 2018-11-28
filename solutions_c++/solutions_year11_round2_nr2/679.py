#include <cstdio>
#include <vector>
using namespace std;

int C,D;

vector<int> vendors(1001000);

bool test(double d)
{
	double pos = vendors[0] - d;	
	pos+=D;

	for(int i=1;i<vendors.size();i++)
	{
		double start = vendors[i] - d;
		double end = vendors[i] + d;

		if(pos < start)
		{
			pos = start;
		}
		else if(pos>end)
		{
			return false;
		}

		pos+=D;
	}

	return true;
}

double find_solution()
{
	double fst = 0, lst = 1e20;
	double ans = -1;
	while(lst-fst > 1e-12 && fst<lst)
	{
		double mid = (fst + lst) / 2.0;
		if(test(mid))
		{
			lst = mid;
			ans = mid;
		}	
		else 
			fst = mid;
	}

	return ans;
}

int main()
{
	int T = 0;
	scanf("%d",&T);

	for(int t=1;t<=T;t++)
	{
		vendors.clear();
		scanf("%d %d", &C, &D);

		for(int i=1;i<=C;i++)
		{
			int a,b;
			scanf("%d %d",&a, &b);

			for(int j=1;j<=b;j++)
				vendors.push_back(a);
		}

		printf("Case #%d: %.10lf\n",t, find_solution());
	}
}