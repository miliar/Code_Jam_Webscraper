
#include <iostream>
#include <algorithm>
#include <iomanip>


using namespace std;

const double EPSILON = 1e-12;

struct Walk
{
	int id;
	int len;
	int st, en;
	int v;
};

bool operator < (const Walk &w1, const Walk &w2)
{
	return w1.v < w2.v;
}

int main()
{
	int N;

	cin >> N;

	for (int n = 1; n <= N; n++)
	{
		int X, S, R, T, W;
		cin >> X >> S >> R >> T >> W;

		Walk w[1000];

		int totalw_len = 0;

		for (int i = 0; i < W; i++)
		{
			cin >> w[i].st >> w[i].en >> w[i].v;
			w[i].id = i;
			w[i].v += S;
			w[i].len = w[i].en - w[i].st;
			totalw_len += w[i].len;
		}

		w[W].id = W;
		w[W].len = X - totalw_len;
		w[W].v = S;

		int Ra = R - S;

		sort(w, w+W+1);

		double tleft = T;
		double t = 0;

		for (int i = 0; i <= W; i++)
		{
			//cout << "w" << w[i].id << ": " << w[i].len << " " << w[i].v << " ";
			if (tleft < EPSILON)
			{
				t += (double) w[i].len / (double) w[i].v;
				//cout << "not running, t = " << ((double) w[i].len / (double) w[i].v) << endl;
			} else
			{
				double tr = (double) w[i].len / (double) (w[i].v + Ra);
				//cout << "tr = " << tr << " ";
				if (tr <= tleft)
				{
					tleft -= tr;
					t += tr;
					//cout << "running all the time, t = " << tr << endl;
				} else
				{
					double lenl = tleft * (double) (w[i].v + Ra);
					double ot = ((double) w[i].len - lenl) / (double) w[i].v;

					//cout << "ending, running for t = " << tleft << " and ot = " << ot << endl;

					t += tleft + ot;
					tleft = 0;
				}
			}
		}

		cout << "Case #" << n << ": " << setprecision(10) << t << endl;
	}
}

