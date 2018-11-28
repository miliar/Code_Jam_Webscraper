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
#include <fstream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 
using namespace std;

string makeSpaces(string str)
{
	for(int i = 0; i<str.size(); i++)
	{
		if(str[i] == '/')
			str[i] = ' ';
	}
	return str;
}

int xyz(vector<string> e, vector<string> tt)
{
	int k = 0;
	for(int i = 0; i<tt.size(); i++)
	{
		bool flag = false;
		for(int j = 0; j<e.size(); j++)
		{
			if(tt[i] == e[j])
			{
				flag = true;
			}
		}
		if(!flag)
		{
			string str;
			for(int j = 0; j < tt[i].size(); j++)
			{
				if((tt[i][j] == '/' && str.size() > 0))
				{
					bool ff = false;
					for(int k = 0; k < e.size(); k++)
					{
						if(e[k] == str)
						{
							ff = true;
						}
					}
					if(!ff)
					{
						e.push_back(str);
						k++;
					}
				}
				str += tt[i][j];
			}
			bool ff =false;
			for(int k = 0; k < e.size(); k++)
			{
				if(e[k] == str)
				{
					ff = true;
				}
			}
			if(!ff)
			{
				e.push_back(str);
				k++;
			}
		}
	}
	return k;
}

int main()
{
	ifstream ifs("A-large.in", ios::in);
	ofstream ofs("A-large.out", ios::out);
	int C;
	ifs>>C;
	for(int i = 0; i < C; i++)
	{
		int N, M;
		ifs>>N;
		ifs>>M;
		vector<string> exists, toBeMade;
		for(int i = 0; i < N; i++)
		{
			string str;
			ifs>>str;
			//str = makeSpaces(str);
			stringstream ss(str);
			string strr;
			while(ss>>strr)
			{
				exists.push_back(strr);
			}
		}
		for(int i = 0; i < M; i++)
		{
			string str;
			ifs>>str;
			//str = makeSpaces(str);
			toBeMade.push_back(str);
		}
		ofs<<"Case #"<<(i+1)<<": "<<xyz(exists, toBeMade)<<endl;
	}
}
