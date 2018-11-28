#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

const int P = 10007;

int N, H, W, R;
vector<int> rockH, rockW;
vector<int> factor, inverse;

bool compare(int id1, int id2)
{
	return rockW[id1] < rockW[id2];
}

int findGCD(int x, int y, int& a, int& b)
{
	if (y == 0)
	{
		a = 1;
		b = 0;
		return x;
	}
	else
	{
		int a1, b1, d;
		d = findGCD(y, x % y, a1, b1);
		a = b1;
		b = (d - a * x) / y;
		return d;
	}
}

int getFact(int n)
{
	int d = n / P;
	int r = n % P;
	
	if (d % 2 == 0)
		return factor[r];
	else
		return -factor[r];
}

int getComb(int n, int m)
{
	if (n / P > m / P + (n - m) / P) return 0;

	int a = getFact(n);
	int b = getFact(m);
	int c = getFact(n-m);

	int tmp = (a * inverse[b]) % P;
	tmp = (tmp * inverse[c]) % P;
	return tmp;
}

int main()
{
	ifstream input;
	ofstream output;
	input.open("D-small.in");
	output.open("D-small.out");

	factor.resize(P);
	factor[0] = 1;
	for (int i = 1; i < P; i++) factor[i] = (factor[i-1] * i) % P;

	inverse.resize(P);
	for (int i = 1; i < P; i++) 
	{
		int a, b, d;
		d = findGCD(i, P, a, b);
		inverse[i] = (a + P) % P;
	}

	input >> N;
	for (int c = 0; c < N; c++)
	{
		input >> H >> W >> R;

		rockH.resize(R);
		rockW.resize(R);

		for (int i = 0; i < R; i++) 
		{
			input >> rockH[i] >> rockW[i];
			rockH[i]--;
			rockW[i]--;
		}

		int ans = 0;
		for (int i = 0; i < (1 << R); i++)
		{
			vector<int> id;
			for (int j = 0; j < R; j++)
				if ((i & (1 << j)) > 0)
					id.push_back(j);
			
			sort(id.begin(), id.end(), compare);

			vector<int> row, col;
			row.push_back(0);
			col.push_back(0);
			for (int j = 0; j < id.size(); j++)
			{
				row.push_back(rockH[id[j]]);
				col.push_back(rockW[id[j]]);
			}
			row.push_back(H-1);
			col.push_back(W-1);

			int now = 1;
			for (int j = 0; j < row.size() - 1; j++)
			{
				int dr = row[j+1] - row[j];
				int dc = col[j+1] - col[j];

				if (dr < 0 || dc < 0 || dc > 2 * dr || dr > 2 * dc || (dr + dc) % 3 > 0)
				{
					now = 0;
					break;
				}

				now = (now * getComb((dr + dc) / 3, (2 * dr - dc) / 3)) % P;
			}

			if (id.size() % 2 == 0)
				ans = (ans + now) % P;
			else
				ans = (ans + P - now) % P;
		}

		output << "Case #" << c + 1 << ": " << ans << endl;
	}

	input.close();
	output.close();
}
