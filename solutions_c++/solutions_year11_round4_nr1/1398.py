#include <iostream>

using namespace std;

int main()
{
	int i,j,k,T,X,S,R,N,Temp;;

	double Time, Cost_time, walk; 

	int B[1001], E[1001], W[1001], Q[1001];

	cin >> T;

	for (i=0; i<T; i++)
	{
		cin >> X >> S >> R >> Time >> N;

		for (j=0; j<N; j++)
		{
			cin >> B[j] >> E[j] >> W[j];
		}

		for (j=0; j<N; j++) 
			Q[j]=j;

		for (j=0; j<N; j++)
			for (k=j+1; k<N; k++)
				if (B[Q[j]] > B[Q[k]]) 
				{
					Temp = Q[j];
					Q[j] = Q[k];
					Q[k] = Temp;
				}

		walk = B[Q[0]];
		for (j=0; j<N-1; j++)
			walk += B[Q[j+1]] - E[Q[j]];
		walk += X - E[Q[j]];

		Cost_time = 0;
		if (Time * R > walk)
		{
			Time -= walk / R;
			Cost_time += walk/R;

			for (j=0; j<N; j++)
				for (k=j+1; k<N; k++)
					if (W[Q[j]] > W[Q[k]]) 
					{
						Temp = Q[j];
						Q[j] = Q[k];
						Q[k] = Temp;
					}

			j=0;
			while ((j<N) && (Time * (W[Q[j]] + R) > (E[Q[j]] - B[Q[j]])))
			{
				Time -= double(E[Q[j]] - B[Q[j]]) / (W[Q[j]] + R);
				Cost_time += double(E[Q[j]] - B[Q[j]]) / (W[Q[j]] + R);
				j++;
			}

			if (j < N)
			{
				Cost_time += Time;
				Cost_time += double(E[Q[j]] - B[Q[j]] - (W[Q[j]] + R) * Time) / (W[Q[j]] + S);
				for (k=j+1; k<N; k++)
					Cost_time += double(E[Q[k]] - B[Q[k]]) / (W[Q[k]] + S);
			}
		} else
		{
			Cost_time = Time;
			walk -= Time*R;
			Cost_time += walk/S;
			for (j=0; j<N; j++)
				Cost_time += double(E[j]-B[j])/(W[j]+S);
		}
		printf("Case #%d: %.7f\n", i+1, Cost_time);
	}
}
