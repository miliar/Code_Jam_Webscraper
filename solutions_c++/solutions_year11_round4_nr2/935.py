#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <cmath>
using namespace std;

// #define input cin
// #define output cout

ifstream input("B-small-attempt3.in");
ofstream output("B-small-out.txt");

int T, R, C, D;
int map[512][512];

bool isSat(int sr, int sc, int k)
{
	double midx = sc + (k-1)/2.0;
	double midy = sr + (k-1)/2.0;
	double sumx = 0.0;
	double sumy = 0.0;
	for(int i = sr; i < sr + k; i++)
	{
		for(int j = sc; j < sc + k; j++)
		{
			sumx += map[i][j] * (j - midx);
			sumy += map[i][j] * (i - midy);
		}
	}
	sumx = sumx - map[sr][sc] * (sc - midx) - map[sr][sc + k-1] * (sc+k-1 - midx);
	sumx = sumx - map[sr+k-1][sc] * (sc - midx) - map[sr+k-1][sc+k-1] * (sc+k-1-midx);
	sumy = sumy - map[sr][sc] * (sr - midy) - map[sr][sc + k-1] * (sr - midy);
	sumy = sumy - map[sr+k-1][sc] * (sr+k-1 - midy) - map[sr+k-1][sc+k-1] * (sr+k-1-midy);
	if(fabs(sumx) < 1e-6 && fabs(sumy) < 1e-6)
		return true;
	else
		return false;
}

int main()
{
	int count;
	input >> T;
	for(count = 0; count < T; count++)
	{
		input >> R >> C >> D;
		int i,j, k;
		for(i = 0; i < R; i ++)
		{
			for(j = 0; j < C; j++)
			{
				char ch;
				input >> ch;
				map[i][j] = ch - '0';
			}
		}
		if(R < C)
			k = R;
		else
			k = C;

		for(; k >=3; k--)
		{
			bool flag = false;
			for(i = 0; i <= R-k; i++)
			{
				for(j = 0; j <= C -k; j++)
				{
					if(isSat(i, j, k))
					{
						flag = true;
						break;
					}
				}
				if(flag)
					break;
			}
			if(flag)
				break;
		}
		if(k < 3)
			output << "Case #" << count + 1 << ": IMPOSSIBLE" << endl;
		else
			output << "Case #" << count + 1 << ": " << k << endl;
	}

	return 0;
}



// int T, X, S, R, N;
// double t;
// struct node
// {
// 	int bg,ed;
// 	int w;
// };
// bool cmp(node a, node b)
// {
// 	if(a.w < b.w)
// 		return true;
// 	else
// 		return false;
// }
// node walkways[1024];
// 
// int main()
// {
// 	int count;
// 	input >> T;
// 	for(count = 0; count < T; count++)
// 	{
// 		double time = 0.0;
// 		input >> X >> S >> R >> t >> N;
// 		int i, j;
// 		int totalwalk = 0;
// 		for(i = 0; i < N; i++)
// 		{
// 			input >> walkways[i].bg >> walkways[i].ed >> walkways[i].w;
// 			totalwalk += (walkways[i].ed - walkways[i].bg);
// 		}
// 		sort(walkways, walkways+N, cmp);
// 		int left = X - totalwalk;
// 		if(R * t <= left)
// 		{
// 			time = t;
// 			left = left - R * t;
// 			time += (double)left / S;
// 			for(i = 0; i < N; i++)
// 			{
// 				time += (double)(walkways[i].ed-walkways[i].bg) / (S+walkways[i].w);
// 			}
// 		}
// 		else
// 		{
// 			time += (double)left / R;
// 			t = t - time;
// 			for(i = 0; i < N; i++)
// 			{
// 				if(walkways[i].ed - walkways[i].bg < (R+walkways[i].w) * t)
// 				{
// 					time += (double)(walkways[i].ed-walkways[i].bg) / (R+walkways[i].w);
// 					t -= (double)(walkways[i].ed-walkways[i].bg) / (R+walkways[i].w);
// 				}
// 				else
// 				{
// 					time = time + t + (double)(walkways[i].ed-walkways[i].bg-t*(R+walkways[i].w))/(S+walkways[i].w);
// 					t = 0.0;
// 				}
// 			}
// 		}
// 		output << "Case #" << count + 1 << ": " << fixed << setprecision(7) << time << endl;
// 	}
// 
// 	return 0;
// }