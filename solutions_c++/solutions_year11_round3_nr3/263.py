#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
using namespace std;

// #define input cin
// #define output cout
ifstream input("C-small-attempt1.in");
ofstream output("C-small-out.txt");

int T,N,L,H;

int fre[105];

int main()
{
	input >> T;
	int count;
	for(count = 0; count < T; count++)
	{
		input >> N >> L >> H;
		int i,j;
		for(i = 0; i < N; i++)
		{
			input >> fre[i];
		}
		bool flag = false;
		for(j = L; j <= H; j++)
		{
			for(i = 0; i < N; i++)
			{
				if(j % fre[i] != 0 && fre[i] % j != 0)
					break;
			}
			if(i == N)
				flag = true;
			if(flag == true)
				break;
		}
		output << "Case #" << count+1 << ": ";
		if(!flag)
			output<<"NO"<<endl;		
		else
			output << j << endl;
	}
	return 0;
}














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