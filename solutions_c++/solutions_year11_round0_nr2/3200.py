#include <iostream>
using namespace std;

int i, j, k, t, T, n, comb, opp;
char co[36][4], op[28][3], N[100];
bool stop = false;

int main()
{
	cin >> t;
	for (T=1; T<=t; ++T)
	{
		int count[256];
		cin >> comb;
		for (i=0; i<comb; ++i)
			scanf("%c%c%c%c",&co[i][3],&co[i][0],&co[i][1],&co[i][2]);
		cin >> opp;
		for (i=0; i<opp; ++i)
			scanf("%c%c%c",&op[i][2],&op[i][0],&op[i][1]);
		cin >> n;
		k = 0;
		for (i=0; i<256; ++i)
			count[i] = 0;
		for (i=0; i<n; ++i)
		{
			cin >> N[k];
			++count[N[k]];
			stop = false;
			while ((k>0) && (!stop))
			{
				stop = true;
				for (j=0; j<comb; ++j)
					if ((co[j][0] == N[k] && co[j][1] == N[k-1]) || (co[j][0] == N[k-1] && co[j][1] == N[k]))
					{
						--count[N[k]];
						--count[N[--k]];
						
						N[k] = co[j][2];
						++count[N[k]];
						stop = false;
					}
			}
			for (j=0; j<opp; ++j)
			{
				if (op[j][0] == op[j][1])
				{
					if (count[op[j][0]] > 1)
						for (; k>=0; --k)
							--count[N[k]];
				}
				else
					if (count[op[j][0]] && count[op[j][1]])
						for (; k>=0; --k)
							--count[N[k]];
			}
			++k;
		}
		cout << "Case #" << T << ": [";
		if (k>0)
			cout << N[0];
		for (i=1; i<k; ++i)
			cout << ", " << N[i];
		cout << "]\n";
	}
	return 0;
}
