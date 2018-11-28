#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	int s;
	int p;
	int n;

	scanf("%d", &t);
	int cnt = 1;
	while(t--)
	{
		scanf("%d%d%d", &n, &s, &p);
		int point;
		vector<int> v;
		int ans = 0;
		int can = 0;
		for(int i = 0; i < n; i++)
		{
			scanf("%d", &point);
			if((point / 3) >= p)
			{
				++ans;
				v.push_back(point);
				continue;
			}
			if(p <= 1){
				if(point >= 1)
				{
					++ans;
					continue;
				}
			}
			else if(point >= (3 * p - 4))
			{
				if(point == 3 * p - 4 || point == 3*p - 3)
				{
					if(s > 0){
						++ans;
						s--;
					}
				}
				else{
		     		++ans;
				}
			}
			
		}
		printf("Case #%d: %d\n", cnt++, ans);
	}
	return 0;
}




					

					



	

    