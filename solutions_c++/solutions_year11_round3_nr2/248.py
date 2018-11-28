#include <iostream>

using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(long long*)a - *(long long*)b );
}

int main()
{
	long long T, i, j, k, Boost, t, N, c, total_time, L;

	long long a[10000], *Dist;

	Dist = new long long [1000001];
	cin >> T;

	for (i=0; i < T; i++)
	{
		cin >> L >> t >> N >> c;
		for (j=0; j < c; j++) cin >> a[j];
		j=0;
		for (j=0; j < N; j++)
			Dist[j] = a[j % c];
		j = 0; total_time = 0; t = t / 2;
		while ((t > Dist[j]) && (j<N))
		{
			t -= Dist[j];
			total_time += Dist[j]*2;
			j++;
		}
		if (j < N){
			if (t == Dist[j]) 
			{
				total_time +=Dist[j]*2;
				j++; 
			}
			else
			{
				Dist[j] = Dist[j] - t;
				total_time += t*2;
			}
			
			if (j < N)
			{
				qsort (Dist+j, N-j, sizeof(long long), compare);
				Boost = N-j > L ? L: N-j;
				for (k=j; k < N - Boost; k++)
					total_time += Dist[k] * 2;
				for (k=N-Boost; k<N; k++)
					total_time += Dist[k];
			}
		}
		printf("Case #%lld: %lld\n", i+1, total_time);
		
	}

	delete []Dist;
	return 0;
}