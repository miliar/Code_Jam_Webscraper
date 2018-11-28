#include <cstdio>
#include <iostream>

using namespace  std;

int N;
long long mas[500100];
long long A[500100];

void init()
{
	scanf("%d", &N);
	int m;
	scanf("%d", &m);
	long long X,Y,Z;
	scanf("%lld%lld%lld", &X, &Y, &Z);
	for (int i=0; i<m; i++)
		scanf("%lld", &A[i]);
	for (int i=0; i<N; i++)
	{
		mas[i] = A[i%m];
		A[i%m] = (X * A[i%m] + Y * (i + 1)) % Z;
	}
}

int arr[500100];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++)
	{
		cerr<<tt<<endl;
		init();
		memset(arr,0,sizeof(arr));
		mas[N] = 1000000;
		mas[N] *= mas[N];
		for (int i=0; i<=N; i++)
		{
			for (int j=0; j<i; j++)
			{
				if (mas[j] < mas[i])
				{
					arr[i] += arr[j];
				}
				arr[i]%=1000000007;
			}
			arr[i]++;
			arr[i]%=1000000007;
		}

		long long res = arr[N]-1;
		printf("Case #%d: %lld\n", tt, res%1000000007);
	}

	return 0;
}