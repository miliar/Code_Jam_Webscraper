#include <iostream>
#include <cmath>

using namespace std;
#define REP(i, n) for(i=0;i<n;i++)

bool isSame(int a[20], int b[20])
{
	int i;
	REP(i, 20)
	{
		if(a[i] != b[i]) return false;
	}
	return true;
}

int main()
{
	int tc;

	freopen("output.out","w",stdout);

	cin >> tc;
	for(int t=1;t<=tc;t++)
	{
		int i, j, k;
		int Max = 0, Sum;
		int N, c[15], C[15][20]={0,}, h[20], d[20];

		cin >> N;
		REP(i, N)
		{
			int tmp, tmp_cnt=0;
			cin >> c[i];
			tmp = c[i];
			while(tmp!=0)
			{
				C[i][tmp_cnt++] = tmp%2;
				tmp/=2;
			}
		}
		
		REP(i, (int)(pow(2.0, N))-2)
		{
			int tmp_cnt = 0, tmp, tmp_binary[20]={0,};
			int tmp_selected[15] = {0,};
			Sum=0;
			tmp = i+1;
			while(tmp!=0)
			{
				tmp_selected[tmp_cnt++] = tmp%2;
				tmp/=2;
			}	

			REP(j, 20)
			{
				h[j] = 0;
				d[j] = 0;
			}

			REP(j, N)
			{
				if(tmp_selected[j] == 1)
				{
					REP(k, 20)
					{
						h[k] += C[j][k];
						h[k] %= 2;
					}
					Sum+=c[j];
				}
				else
				{
					REP(k, 20)
					{
						d[k] += C[j][k];
						d[k] %= 2;
					}
				}
			}

			if( isSame(h, d) && Max < Sum)
			{
				Max = Sum;
			}
		}

		cout << "Case #" << t << ": ";
		if(Max == 0) cout << "NO" << endl;
		else cout << Max << endl;
	}

	return 0;
}
