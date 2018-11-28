#include<set>
#include<cstdio>
#include<vector>
#include<string>
#include<fstream>
#include<iostream>
using namespace std;

ifstream in("plik.in");
ofstream out("plik.out");

typedef long long lint;

lint N, K, B, T;
lint X[55], V[55];
lint mini[55];

void lecim()
{
	in >> N >> K >> B >> T;
	for(int i = 0; i < N; ++i) in >> X[i];
	for(int i = 0; i < N; ++i) in >> V[i];
	int ret = -1;
		lint tmp = 0;
		int ile = 0;
		for(int i = N - 1; i >= 0; --i)
		{
			if (T * V[i] >= B - X[i])
			{
				mini[i] = (N - i - 1);
				for(int j = i + 1; j < N; ++j)
				{
					if (mini[j] >= 0)
					{
						mini[i] = min(mini[i], mini[j] + (j - i - 1));
						break;
					}
				}
				++ile;
				if(ile <= K) tmp += mini[i];
			}
			else
			{
				mini[i] = -1;
			}
		}
		if(ile >= K && (ret == -1 || ret > tmp))
		{
			ret = tmp;
		}
	if (ret < 0) out << "IMPOSSIBLE";
	else out << ret;
}

int main()
{
	int t;
	in >> t;

	for(int i = 1; i <= t; ++i)
	{
		cout << i << "\n";
		out << "Case #" << i << ": ";
		lecim();
		out << "\n";
	}
	in.close();
	out.close();
	//cin >> N;
	return 0;
}