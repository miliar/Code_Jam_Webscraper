#include <cstdio>
#include <vector>
#include <algorithm>

using std::vector;

struct walkway
{
	walkway() {}
	walkway(const int& bb, const int& ee, const int& ww) : b(bb), e(ee), w(ww) {}
	
	int b;
	int e;
	int w;
};

inline int operator< (const walkway& a, const walkway& b)
{
	return a.w < b.w;
}

int main()
{
	int ntests;
	std::scanf("%d", &ntests);
	for (int ctest = 1; ctest <= ntests; ctest++)
	{
		int x, s, r, t, n;
		std::scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		
		vector<walkway> walkways;
		int lwp = -1;
		for (int i = 0; i < n; i++)
		{
			walkway w;
			std::scanf("%d%d%d", &(w.b), &(w.e), &(w.w)); w.e--;
			if (w.b > lwp+1)
				walkways.push_back(walkway(lwp+1, w.b-1, 0));
			walkways.push_back(w);
			lwp = w.e;
		}
		
		if (x > lwp+1)
			walkways.push_back(walkway(lwp+1, x-1, 0));
		
		std::sort(walkways.begin(), walkways.end());
		
		double time = 0;
		
		double remt = t;
		for (int i = 0; i < (int)walkways.size(); i++)
		{
			double runt = ((double)(walkways[i].e - walkways[i].b + 1)) / (r + walkways[i].w);
			if (runt >= remt)
			{
				double rundist = remt * (r + walkways[i].w);
				double walkdist = ((double)(walkways[i].e - walkways[i].b + 1)) - rundist;
				
				time += remt + walkdist / (s + walkways[i].w);
				remt = 0;
			}
			else
			{
				time += runt;
				remt -= runt;
			}
		}
		
		std::printf("Case #%d: %.9lf\n", ctest, time);
	}
	
	return 0;
}
