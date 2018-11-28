#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
bool cmp(int a,int b){return a > b ;}
int main()
{
	freopen("output.txt","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for(int testero = 1; testero <= testcase;testero++)
	{
		printf("Case #%d: ",testero);
		long long l, t, n, c, tp, res = 0;
		scanf("%lld%lld%lld%lld",&l,&t,&n,&c);
		vector<long long> d(n);
		  for (int i = 0; i < c; i++)
		  {
			   scanf("%lld",&tp);

			   for (int k = 0; k*c + i < n; k++)
			   {
					d[k*c + i] = tp;
			   }
		  } 

	
		long long time = 0, i;
		for(i=0;i<d.size();i++)
		{
			if(time >= t)
			{break;}
			else {
				time+= 2*d[i];
				res += 2*d[i];
			}
		}
		vector<long long> tim(d.begin()+i,d.end());
		if (time > t)
		{
			res = t;
			tim.push_back((time - t) / 2);
		}

		
		sort(tim.begin(),tim.end(),&cmp);
		
		int builded = 0;
		for (int i = 0; i < tim.size(); i++)
		{
			if (builded < l)
			{
				res += tim[i];
				builded++;
			}
			else
			{
				res += 2 * tim[i];
			}
		}

		printf("%d\n",res);
	}

	
	return 0;
} 