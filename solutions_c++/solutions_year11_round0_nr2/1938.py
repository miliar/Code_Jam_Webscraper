#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

ifstream input("B-large.in");
ofstream output("B-largeout.txt");
//  #define input cin
//  #define output cout

int T;
int C,D,N;

char combine[40][4];
char oppose[40][3];
char seq[128];

int main()
{
	input >> T;
	for(int count = 0; count < T; count++)
	{
		string res;
		input >> C;
		for(int i = 0; i < C; i++)
		{
			input >> combine[i];
		}
		input >> D;
		for(int i = 0; i < D; i++)
		{
			input >> oppose[i];
		}
		input >> N;
		input >> seq;
		res.push_back(seq[0]);
		for(int i = 1; i < N; i++)
		{
			if(res.size() == 0)
			{
				res.push_back(seq[i]);
				continue;
			}
			int k;
			for(k = 0; k < C; k++)
			{
				char ch1 = res[res.size()-1];
				char ch2 = seq[i];
				if((combine[k][0] == ch1 && combine[k][1] == ch2) || (combine[k][0] == ch2 && combine[k][1] == ch1))
				{
					res[res.size()-1] = combine[k][2];
					break;
				}
			}
			int j;
			bool flag;
			if(k == C)
			{
				for(j = 0; j < res.size(); j++)
				{
					char ch1 = res[j];
					char ch2 = seq[i];
					flag = false;
					for(int k = 0; k < D; k++)
					{
						if((oppose[k][0] == ch1 && oppose[k][1] == ch2) || (oppose[k][0] == ch2 && oppose[k][1] == ch1))
						{
							res.clear();
							flag =true;
							break;
						}
					}
					if(flag)
						break;
				}
			}

			if(k == C && !flag)
				res.push_back(seq[i]);
		}
		if(res.size() == 0)
		{
			output << "Case #" << count+1 << ": []"<<endl;
		}
		else
		{
			output << "Case #" << count+1 << ": [" << res[0];
			for(int i = 1; i < res.size(); i++)
			{
				output << ", " << res[i];
			}
			output << "]" << endl;
		}

	}
}



// int T, N;
// 
// int main()
// {
// 	input >> T;
// 	int count = 0;
// 	char ch;
// 	int pos;
// 	int oleft = 0;
// 	int bleft = 0;
// 	int op = 1;
// 	int bp = 1;
// 	int time = 0;
// 	int turn = 0; //0: O, 1: B
// 
// 	for(count = 0; count < T; count ++)
// 	{
// 		input >> N;
// 		time = 0;
// 		oleft = bleft = 0;
// 		op = bp = 1;
// 		turn = 0;
// 		for(int i = 0; i < N; i++)
// 		{
// 			input >> ch >> pos;
// 			if(ch == 'O')
// 			{
// 				if(turn == 0)
// 				{
// 					bleft = bleft + abs(pos - op) + 1;
// 					time = time + abs(pos - op) + 1;
// 					op = pos;
// 				}
// 				else
// 				{
// 					if(oleft >= abs(pos - op))
// 					{
// 						time++;
// 						bleft = 1;
// 					}
// 					else
// 					{
// 						time = time + (abs(pos-op)+1-oleft);
// 						bleft = abs(pos-op)+1-oleft;
// 					}
// 					op = pos;
// 				}
// 				turn = 0;
// 			}
// 			else
// 			{
// 				if(turn == 1)
// 				{
// 					oleft = oleft + abs(pos - bp) + 1;
// 					time = time + abs(pos - bp) + 1;
// 					bp = pos;
// 				}
// 				else
// 				{
// 					if(bleft >= abs(pos - bp))
// 					{
// 						time++;
// 						oleft = 1;
// 					}
// 					else
// 					{
// 						time = time + (abs(pos-bp)+1-bleft);
// 						oleft = abs(pos-bp)+1-bleft;
// 					}
// 					bp = pos;
// 				}
// 				turn = 1;
// 			}
// 		}
// 		output << "Case #" << count+1 << ": " << time <<endl;
// 	}
// 	return 0;
// }