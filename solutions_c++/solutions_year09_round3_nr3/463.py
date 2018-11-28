#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

int arr[10005];

bool cmp(int a, int b)
{
	return a < b;
}

bool used[10005];

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);
	int test, cases = 1, i, j, p, q;
	scanf("%d", &test);
	while(test --)
	{
		scanf("%d %d", &p, &q);
		for(i=0; i<q; i++)
			scanf("%d", &arr[i]);
		int Min = -1;
		do
		{
			for(i=1; i<=p; i++)
				used[i] = true;
			int number = 0;
			for(i=0; i<q; i++)
			{
				for(j=arr[i]-1; j>=1; j--)
				{
					if(!used[j])
						break;
					number ++;
				}
				for(j=arr[i]+1; j<=p; j++)
				{
					if(!used[j])
						break;
					number ++;
				}
				used[arr[i]] = false;
			}
			if(Min == -1 || Min > number)
				Min = number;
		}while(next_permutation(arr, arr + q, cmp));
		printf("Case #%d: %d\n", cases ++, Min);
	}
	return 0;
}