#include<iostream>
#include<string>
using namespace std;

int T, N, S, p, ncase;
int total_score[110];

int Solve()
{
	int i, j, k;
	int ans = 0;
	for(i=0; i<N; i++)
	{
		if((total_score[i]/3) >= p)
		 	ans++;
		else if((total_score[i]/3 + 2) < p)
			continue;
		else
		{
			if((total_score[i]/3) == p-2)
			{
				if((total_score[i]%3) == 0)
				{
					continue;
				}
				else if((total_score[i]%3) == 1)
				{
					continue;
				}
				else if((total_score[i]%3) == 2)
				{
					if(S > 0)
					{
						S--;
						ans++;
					}
					else
					{
						continue;
					}
				}
			}
			else if((total_score[i]/3) == p-1)
			{
				if((total_score[i]%3) == 0)
				{
					if(((total_score[i]/3)-1) < 0)
					{
						continue;
					}
					else if(S > 0)
					{
						S--;
						ans++;
					}
					else
					{
						continue;
					}
				}
				else if((total_score[i]%3) == 1)
				{
					if(((total_score[i]/3) - 1) < 0)
					{
						continue;
					}
					else
						ans++;
				}
				else if((total_score[i]%3) == 2)
				{
					ans++;
				}
			}
		}
	}
	
	return ans;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);

	int i, j, k;
	ncase = 1;
	cin >> T;
	for(i=0; i<T; i++)
	{
		cin >> N;
		cin >> S;
		cin >> p;
		for(j=0; j<N; j++)
			cin >> total_score[j];
		printf("Case #%d: %d\n", ncase++, Solve());
	}

	//system("pause");
	return 0;
}
