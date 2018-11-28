#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

bool table[2000] = {0};

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; ++i)
	{
		bool found = false;
		int n;
		scanf("%d", &n);
		vector<int> data;
		for (int j = 0; j < n; ++j)
		{
			int tmp;
			scanf("%d", &tmp);
			data.push_back(tmp);
		}
		sort(data.begin(), data.end());
		//subset
		for (int j=0; j<(1<<n); ++j)
		{
			int sean = 0, pat = 0;
			int real_sean = 0; //truth
			int real_pat = 0;
			int index = 0;
			int mask = 1;
			for (int k = 0; k < n; ++k)
			{
				index = mask & j;
				if (index == 0) //sean 
				{
					real_sean += data[k];
					sean ^= data[k];
				} 
				else //poor pat
				{
					real_pat += data[k];
					pat ^= data[k];
				}
				mask<<=1;
			}
			if (sean == pat && real_sean && real_pat) 
			{
				printf("Case #%d: %d\n", i+1, real_sean);
				found = true;
				break;
			}

		}
		if (!found) 
		{
			printf("Case #%d: NO\n", i+1);
		}
	}
	return 0;
}