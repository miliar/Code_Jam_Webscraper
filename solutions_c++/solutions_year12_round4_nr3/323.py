#include <iostream>
#include <vector>
#include <map>
using namespace std;

int N;
vector<int> look;
vector<int> p;
vector<double> slope;
map<int, vector<int> > m;

void solve(int x)
{
	for(int i = 0; i < m[x].size(); i ++)
	{
		if (i == 0)
		{
			int y = m[x][i];
			p[y] = p[x]- slope[x] * (x-y) - 1;
			slope[y] = (p[y] - p[x] + 0.0) / (y-x);
			solve(y);
		}
		else
		{
			int y = m[x][i];
			p[y] = p[m[x][0]];
			slope[y] = (p[y] - p[x] + 0.0) / (y-x);
			solve(y);
			solve(y);
		}
	}
}


int main()
{
	int tn, pn=0;
	cin >> tn;
	while(tn--)
	{
		pn++;
		cout << "Case #" << pn << ": ";
		cin >> N;
		look.clear();
		m.clear();
		N--;
		for(int i = 0; i < N;i++)
		{
			int t;
			cin >> t;
			look.push_back(t-1);
			m[t-1].push_back(i);
		}
		bool impossible = false;
		for(int i = 0 ; i < N; i ++)
			for(int j = i + 1; j < N; j ++)
			{
				if (look[i] > j && look[i] < look[j])
					impossible = true;
			}
		if (impossible)
		{
			cout << "Impossible" << endl;
			continue;
		}

		p.clear();
		N++;
		p.resize(N);
		slope.resize(N);

		p[N-1] = 0;
		slope[N-1] = 0;
		solve(N-1);

		int minh = 0;
		for(int i = 0; i < N; i ++)
			if (minh > p[i]) minh = p[i];

		for(int i = 0 ; i < N; i ++)
		{
			cout << p[i] - minh << ' ';
		}

		cout << endl;

	}

}
