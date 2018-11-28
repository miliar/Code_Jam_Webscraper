
#include <stdio.h>
#include <vector>

int main(int argc, char* argv[])
{

	freopen("c:\\input.in","r",stdin);
	freopen("C:\\output.txt","w",stdout);


	int T = 0;

	scanf("%d", &T);

	for(int t = 0 ; t < T ; t++)
	{
		int N = 0 ;
		scanf("%d", &N);
		std::vector<int> A;
		std::vector<int> B;
		std::vector<int> M;
		A.resize(N);
		B.resize(N);
		M.resize(N);
		for(int n = 0 ; n < N ; n ++)
		{
			int a = 0;
			int b = 0;
			scanf("%d %d", &a, &b);
			A[n] = a;
			B[n] = b;
			M[n] = b-a;
		}

		long long ans = 0;
		for(int i = 0 ; i < N ; i++)
		{
			int curA = A[i];
			int curB = B[i];
			int curM = M[i];

			for(int j = 0 ; j < N ; j++)
			{
				if( i == j )
					continue;
				else if( curM == M[j])
					continue;
				else
				{
					if( (A[j] > curA && B[j] < curB) || A[j] < curA && B[j] > curB)
						ans++;
				}
			}
		}


		printf("Case #%d: %d\n", t+1, ans/2);
	}

	return 0;
}