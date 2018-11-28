#include <fstream>

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

int A, N, M;
int x1, x2, x3, y1, y2, y3;

void calc()
{
	for (int a = 0; a <= N; a++)
		for (int c = 0; c <= N; c++)
		{
			for (int b = 0; b <= M; b++)
				for (int d = 0; d <= M; d++)
				{
					int tmp = b*c - d*a;
					if (tmp < 0)
						tmp = -tmp;
					if (tmp == A)
					{
						x1 = 0;
						y1 = 0;
						x2 = a;
						x3 = c;
						y2 = b;
						y3 = d;
						return;
					}
				}
		}
}


int main()
{
	int C;
	cin >> C;
	for (int i = 0; i < C; i++)
	{
		cin >> N >> M >> A;
		x1 = -1;
		calc();
		cout << "Case #" << i+1 << ":";
		if (x1 == -1)
			cout << " IMPOSSIBLE";
		else
			cout << " " << 0 << " " << 0 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
		cout << endl;
	}
}
