#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

const int MAX_C = 37;
const int MAX_D = 29;
const int PLANE = 0;
const int COMBINED = 1;

int C, D, N, T;

typedef char combine[3];
typedef char oppose[2];

combine COM[MAX_C];
oppose OPP[MAX_D];
string elem;
vector<char> list;

bool exist(char c)
{
	for(int i=0; i<list.size(); i++)
	{
		if(c == list[i])
		{
			return true;
		}
	}

	return false;
}

void solve()
{
	list.clear();
	int flag = PLANE;

	for(int n=0; n<N; n++)
	{
		flag = PLANE;
		list.push_back(elem[n]);

		if(list.size() <= 1)
			continue;

		char end1 = list[list.size()-2];
		char end2 = list[list.size()-1];

		for(int c=0; c<C; c++)
		{
			if((end1==COM[c][0] && end2==COM[c][1]) || (end1==COM[c][1] && end2==COM[c][0]))
			{
				list.erase(list.begin() + list.size()-1);
				list.erase(list.begin() + list.size()-1);
				list.push_back(COM[c][2]);
				flag = COMBINED;
				break;
			}
		}

		if(flag!=PLANE)
		{
			continue;
		}

		for(int d=0; d<D; d++)
		{
			if(exist(OPP[d][0]) && exist(OPP[d][1]))
			{
				list.clear();
			}
		}
	}
}

int main()
{
	ifstream ifs("input.txt", ios::in);
	ofstream ofs("output.txt", ios::out);
	
	ifs >> T;
	for(int t=0; t<T; t++)
	{
		ifs >> C;
		for(int c=0; c<C; c++)
		{
			ifs >> COM[c];
		}

		ifs >> D;
		for(int d=0; d<D; d++)
		{
			ifs >> OPP[d];
		}

		ifs >> N;
		ifs >> elem;
		
		solve();

		ofs << "Case #" << t+1 << ": [";
		for(int i=0; i<list.size(); i++)
		{
			if(i!=0)
			{
				ofs << ", ";
			}

			ofs << list[i];
		}
		ofs << "]" << endl;
	}
	
}