#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> a;
int tempC[10000];
int main()
{
	int tt;
	scanf("%d", &tt);
	int tp = 0;
	int N, L, t, C, i, j, k;
	while(tt--)
	{
		tp++;
		a.clear();
		scanf("%d%d%d%d", &L, &t, &N, &C);
		for(i=0; i<C; ++i)
		{
			scanf("%d", &tempC[i]);
		}
		//make the main array

		int total = 0;
		for(i=0; i<N; )
		{
			for(j=0; j<C; ++j)
			{
				a.push_back(tempC[j]);
				total += tempC[j];
				i++;
				if(i == N)
					break;
			}
		}
/*		for(i=0; i<a.size(); ++i)
			printf("%d ", a[i]);
		printf("\n");*/

		int sum = 0;
		t = t/2;
		for(i=0; i<a.size(); ++i)
		{
			sum += a[i];
			if(sum > t)
				break;

		}

		for(k=0; k<i; k++)
		{
			t -= a[k];
			a[k] = 0;
		}
		a[i] -= t;
		sort(a.begin(), a.end());

/*		for(i=0; i<a.size(); ++i)
			printf("%d ", a[i]);
		printf("\n");*/

		sum = 0;

		k=0;
		for(i=a.size()-1; i>=0 && k<L; --i, k++)
		{
			sum += a[i];
		}
//		printf(">>%d %d\n", sum , total);

		total -= sum;
		printf("Case #%d: %d\n", tp, total*2+sum);
	}
	return 0;

}

