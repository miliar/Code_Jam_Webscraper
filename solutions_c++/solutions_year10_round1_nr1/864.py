#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <queue> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 
#include <fstream>
using namespace std;

int getCount(int i, int j, vector<string> vs, char ch, int M)
{
	int r = 0;
				int b = 0;
				int k;
				for(k = 0; k < M; k++)
				{
					int index = j+k;
					if(index>=0 && index<vs[0].size())
					{
						if(vs[i][index] == ch)
							r++;
						else break;
					}
				}
				if(r >= M)
					return r;
				r = 0;
				b = 0;
				for(k = 0; k < M; k++)
				{
					int index = i+k;
					if(index>=0 && index<vs.size())
					{
						if(vs[index][j] == ch)
							r++;
						else break;
					}
				}
				if(r >= M)
					return r;
				r = 0;
				b = 0;
				for(k = 0; k < M; k++)
				{
					int index1 = i + k;
					int index2 = j + k;
					if(index1>=0 && index1<vs.size() && index2>=0 && index2<vs[0].size())
					{
						if(vs[index1][index2] == ch)
							r++;
						else 
							break;
					}
				}
				if(r >= M)
					return r;
				r = 0;
				for(k = 0; k < M; k++)
				{
					int index1 = i + k;
					int index2 = j - k;
					if(index1>=0 && index1<vs.size() && index2>=0 && index2<vs[0].size())
					{
						if(vs[index1][index2] == ch)
							r++;
						else 
							break;
					}
				}
				if(r >= M)
					return r;
				return 0;
}

string getA(vector<string> vs, int M)
{
	int i;
	for(i = vs.size()-1; i >= 0; i--)
	{
		for(int j = vs[0].size()-1; j >= 0; j--)
		{
			if(vs[i][j] == '.')
			{
				int cPos = j;
				for(int k = j; k>= 0; k--)
				{
					if(vs[i][k] != '.' && cPos >= 0)
					{
						vs[i][cPos] = vs[i][k];
						vs[i][k] = '.';
						cPos --;
					}
				}
			}
		}
	}
	
		bool red = false, blue = false;
		for(i = 0; i < vs.size(); i++)
		{
			for(int j = 0; j < vs[0].size(); j++)
			{
				int rr = getCount(i,j,vs,'R', M);
				if(rr == M)
				{
					red = true;
				}
				rr = getCount(i,j,vs,'B', M);
				if(rr == M)
				{
					blue = true;
				}

			}
		}
		
		if(red && blue)
			return "Both";
		if(red)
			return "Red";
		if(blue)
			return "Blue";
		return "Neither";
}

int main()
{
	ifstream ifs("A-large.in", ios::in);
	ofstream cout("A-large.out", ios::out);
	int N;
	ifs>>N;
	for(int i = 0; i < N; i++)
	{
		int r, M;
		vector<string> vs;
		ifs>>r>>M;
		for(int j = 0; j<r; j++)
		{
			string str;
			ifs >> str;
			vs.push_back(str);
		}
		cout<<"Case #"<<(i+1)<<": "<<getA(vs, M)<<endl;
	}
	return 0;
}