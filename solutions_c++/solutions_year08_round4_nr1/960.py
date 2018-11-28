#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main(int argc, char* argv[])
{
	int C;
	cin >> C;
	for (int k = 0; k < C; k++)
	{
		int M = 0;
		cin >> M;
		int V = 0;
		cin >> V;
		vector<int> op(M+1);
		vector<int> cp(M+1);
		vector<int> mc1(M+1);
		vector<int> mc0(M+1);

		for (int i = 1; i <= (M-1)/2; i++)
		{
			int g = 0, c = 0;
			cin >> g >> c;
			op[i] = g;
			cp[i] = c;
		}

		for (int i = (M-1)/2 + 1; i <= M; i++)
		{
			int g = 0;
			cin >> g;
			op[i] = g;
			cp[i] = 0;
			if (g)
			{
				mc0[i] = 100000;
				mc1[i] = 0;
			}
			else
			{
				mc0[i] = 0;
				mc1[i] = 100000;
			}
		}

		for (int i = (M-1)/2; i > 0; i--)
		{
			if (cp[i])
			{
				if (op[i])
				{
					int t = mc1[i*2] + mc1[i*2+1];
					t = min(t, min(mc1[i*2]+mc0[i*2+1], mc0[i*2]+mc1[i*2+1])+1);
					if (t > M)
						t = 100000;
					mc1[i] = t;

					t = min(mc0[i*2]+mc0[i*2+1], min(mc1[i*2]+mc0[i*2+1], mc0[i*2]+mc1[i*2+1]));
					if (t > M)
						t = 100000;
					mc0[i] = t;
				}
				else
				{
					int t = min(mc1[i*2]+mc1[i*2+1], min(mc1[i*2]+mc0[i*2+1], mc0[i*2]+mc1[i*2+1]));
					if (t > M)
						t = 100000;
					mc1[i] = t;

					t = mc0[i*2] + mc0[i*2+1];
					t = min(t, min(mc1[i*2]+mc0[i*2+1], mc0[i*2]+mc1[i*2+1])+1);
					if (t > M)
						t = 100000;
					mc0[i] = t;
				}
			}
			else
			{
				if (op[i])
				{
					int t = mc1[i*2] + mc1[i*2+1];
					if (t > M)
						t = 100000;
					mc1[i] = t;

					t = min(mc0[i*2]+mc0[i*2+1], min(mc1[i*2]+mc0[i*2+1], mc0[i*2]+mc1[i*2+1]));
					if (t > M)
						t = 100000;
					mc0[i] = t;
				}
				else
				{
					int t = min(mc1[i*2]+mc1[i*2+1], min(mc1[i*2]+mc0[i*2+1], mc0[i*2]+mc1[i*2+1]));
					if (t > M)
						t = 100000;
					mc1[i] = t;

					t = mc0[i*2] + mc0[i*2+1];
					if (t > M)
						t = 100000;
					mc0[i] = t;
				}
			}
		}
		if (V)
		{
			if (mc1[1] > M)
			{
				cout << "Case #" << (k+1) << ": " << "IMPOSSIBLE" << endl;
			}
			else
			{
				cout << "Case #" << (k+1) << ": " << mc1[1] << endl;
			}
		}
		else
		{
			if (mc0[1] > M)
			{
				cout << "Case #" << (k+1) << ": " << "IMPOSSIBLE" << endl;
			}
			else
			{
				cout << "Case #" << (k+1) << ": " << mc0[1] << endl;
			}
		}
		
	}
	return 0;
}
