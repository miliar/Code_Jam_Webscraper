#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
using namespace std;

// #define input cin
// #define output cout

ifstream input("A-large.in");
ofstream output("A-large-out.txt");

int T, X, S, R, N;
double t;
struct node
{
	int bg,ed;
	int w;
};
bool cmp(node a, node b)
{
	if(a.w < b.w)
		return true;
	else
		return false;
}
node walkways[1024];

int main()
{
	int count;
	input >> T;
	for(count = 0; count < T; count++)
	{
		double time = 0.0;
		input >> X >> S >> R >> t >> N;
		int i, j;
		int totalwalk = 0;
		for(i = 0; i < N; i++)
		{
			input >> walkways[i].bg >> walkways[i].ed >> walkways[i].w;
			totalwalk += (walkways[i].ed - walkways[i].bg);
		}
		sort(walkways, walkways+N, cmp);
		int left = X - totalwalk;
		if(R * t <= left)
		{
			time = t;
			left = left - R * t;
			time += (double)left / S;
			for(i = 0; i < N; i++)
			{
				time += (double)(walkways[i].ed-walkways[i].bg) / (S+walkways[i].w);
			}
		}
		else
		{
			time += (double)left / R;
			t = t - time;
			for(i = 0; i < N; i++)
			{
				if(walkways[i].ed - walkways[i].bg < (R+walkways[i].w) * t)
				{
					time += (double)(walkways[i].ed-walkways[i].bg) / (R+walkways[i].w);
					t -= (double)(walkways[i].ed-walkways[i].bg) / (R+walkways[i].w);
				}
				else
				{
					time = time + t + (double)(walkways[i].ed-walkways[i].bg-t*(R+walkways[i].w))/(S+walkways[i].w);
					t = 0.0;
				}
			}
		}
		output << "Case #" << count + 1 << ": " << fixed << setprecision(7) << time << endl;
	}

	return 0;
}