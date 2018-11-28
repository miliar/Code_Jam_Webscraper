#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

// #define input cin
// #define output cout
ifstream input("B-large.in");
ofstream output("B-large-out.txt");
/*#define MAXINT 1000005*/

__int64 t, res;
int T,L,N,C;
int dis[1000005];
int d[1000005];

int main()
{
	input >> T;
	int count;
	for(count = 0; count < T; count++)
	{
		input >> L >> t >> N >> C;
		int i, j, k;
		for(i = 0; i < C; i++)
		{
			input >> dis[i];
		}
		for(i = C; i < N; i++)
		{
			dis[i] = dis[i-C];
		}
		
		__int64 sum = 0;
		res = 0;
		for(i = 0; i < N; i++)
		{
			sum += (dis[i] << 1);
			if(sum > t)
				break;
		}
		if(i == N)
		{
			output << "Case #" << count+1 << ": " << sum << endl;
			continue;
		}

		int len = 1;
		res = t;
		d[0] = (int)((sum-t)/2);
		i++;
		for(; i < N; i++)
		{
			d[len] = dis[i];
			len++;
		}
		sort(d, d+len);
		for(j = len-1; j >= len-L && j >= 0; j--)
		{
			res += d[j];
		}
		if(len-L-1>=0)
		{
			for(j = len-L-1; j >= 0; j--)
			{
				res += (d[j] << 1);
			}
		}
		output << "Case #" << count+1 << ": " << res << endl;
	}
	return 0;
}

















// int T,N,L,H;
// 
// int fre[105];
// 
// int main()
// {
// 	input >> T;
// 	int count;
// 	for(count = 0; count < T; count++)
// 	{
// 		input >> N >> L >> H;
// 		int i,j;
// 		for(i = 0; i < N; i++)
// 		{
// 			input >> fre[i];
// 		}
// 		bool flag = false;
// 		for(j = L; j <= H; j++)
// 		{
// 			for(i = 0; i < N; i++)
// 			{
// 				if(j % fre[i] != 0 && fre[i] % j != 0)
// 					break;
// 			}
// 			if(i == N)
// 				flag = true;
// 			if(flag == true)
// 				break;
// 		}
// 		output << "Case #" << count+1 << ": ";
// 		if(!flag)
// 			output<<"NO"<<endl;		
// 		else
// 			output << j << endl;
// 	}
// 	return 0;
// }
// 
// 
// 
// 










// int T, R, C;
// char map[55][55];
// 
// 
// int main()
// {
// 	input >> T;
// 	int count;
// 	for(count = 0; count < T; count ++)
// 	{
// 		input >> R>>C;
// 		int i,j;
// 		for(i = 0; i < R; i++)
// 		{
// 			for(j = 0; j < C; j++)
// 			{
// 				input >> map[i][j];
// 			}
// 		}
// 		bool flag = true;
// 		for(i = 0; i < R; i++)
// 		{
// 			for(j = 0; j < C; j++)
// 			{
// 				if(map[i][j] == '#')
// 				{
// 					if(map[i][j+1] == '#' && map[i+1][j] == '#' && map[i+1][j+1] == '#')
// 					{
// 						map[i][j] = map[i+1][j+1] = '/';
// 						map[i][j+1] = map[i+1][j] = '\\';
// 					}
// 					else
// 					{
// 						flag = false;
// 						break;
// 					}
// 				}
// 			}
// 			if(!flag)
// 				break;
// 		}
// 		output << "Case #" << count+1 << ":"<<endl;
// 		if(!flag)
// 			output<<"Impossible"<<endl;
// 		else
// 		{
// 			for(i = 0; i < R; i++)
// 			{
// 				for(j = 0; j < C; j++)
// 				{
// 					output << map[i][j];
// 				}
// 				output << endl;
// 			}
// 		}
// 	}
// 	return 0;
// }