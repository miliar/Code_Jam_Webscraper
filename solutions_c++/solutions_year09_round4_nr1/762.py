#include <stdio.h>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

int T, N;

vector <int> m;

int Solve()
{
	int ans = 0;
	bool b = false;
	int num;
	int rep;

	int tmp;

	while(true)
	{
		b = false;

		for(int j = 0; j < N; j++)
		{
			if( m[j] > j )
			{
				b = true;
				num = j;
				break;
			}
		}

		if( b == false )
			break;

		for(int j = num+1; j < N; j++)
		{
			if( m[j] <= num )
			{
				rep = j;
				break;
			}
		}

		for(int j = rep; j > num; j--)
		{
			tmp = m[j];
			m[j] = m[j-1];
			m[j-1] = tmp;
			ans++;
		}
	}

	return ans;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);

	int ans;
	char x;

	for(int ii = 0; ii < T; ii++)
	{
		scanf("%d\n", &N);

		m.clear();
		m.resize(N, 0);

		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < N; j++)
			{
				scanf("%c", &x);
				if( x == '1' )
					m[i] = j;
			}
			scanf("\n");
		}

		ans = Solve();

		printf("Case #%d: %d\n", ii+1, ans);
	}









	return 0;
}