#include<iostream>
#include<cstdio>
#include<vector>

using namespace std;

vector<int> Queue[100100];
int v[100100];
int B[110];

int main()
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int test_cases, casen = 0;
	for ( scanf( "%d", &test_cases ); test_cases > 0; test_cases -- )
	{
		long long L; int N;
		cin >> L >> N;
		for (int i = 0; i < N; i++ )
			scanf( "%d", &B[i] );
		int Max = 0;
		for (int i = 0; i < N; i++ )
			if ( B[i] > Max ) Max = B[i];
		//cout << L << endl;
		memset( v, 0xff, sizeof(v) ); v[0] = 0; 
		for (int i = 0; i < Max + 10; i++ ) Queue[i].clear(); Queue[0].push_back(0);
		for (int i = 0; i < Max + 10; i++ )
		{
			for (int j = 0; j < Queue[i].size(); j++ )
			{
				int t = Queue[i][j];
				for (int k = 0; k < N; k++ )
				if ( t + B[k] >= Max )
				{
					if ( v[t + B[k] - Max] == -1 )
					{
						v[t + B[k] - Max] = v[t];
						Queue[i].push_back(t + B[k] - Max);
					}
				}
			}
			for (int j = 0; j < Queue[i].size(); j++ )
			{
				int t = Queue[i][j];
				for (int k = 0; k < N; k++ )
				if ( t + B[k] < Max )
				{
					if ( v[t + B[k]] == -1 )
					{
						v[t + B[k]] = v[t] + 1;
						Queue[i + 1].push_back(t + B[k]);
					}
				}
			}
		}
		printf( "Case #%d: ", ++casen );
		if ( v[L % Max] != -1 ) cout << v[L % Max] + L / Max << endl;
		else cout << "IMPOSSIBLE\n";
	}
}
