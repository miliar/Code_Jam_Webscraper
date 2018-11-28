#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

int convertString(string S)
{
	stringstream ss;
	ss << S;
	int m;
	ss>>m;
	return m;
}

vector < pair <string, string> > Set;
int main()
{
	ifstream fin ("in.txt");
	ofstream fout ("out.txt");
	int n;
	fin>>n;
	int C = 0;
	for (int i = 1; i <= n; i ++)
	{
		int S1, S2;
		fin>>S1>>S2;
		for (int i = S1+1; i < S2; i++)
		{
			string P1 = convertInt(i);
			for (int j = 0; j < P1.size(); j ++)
			{
				string l,m;
				l = m = "";
				l = P1.substr(j, P1.size()-j+1);
				if (j > 0)
					m = P1.substr(0, j);
				string P2 = l + m ;
				string A1, A2;
				A1 = P1;
				A2 = P2;
				if (A2[0] == '0')continue;
				if (A1 == A2) continue;
				int X = convertString(A2);
				if (X > S2 || X < S1)
					continue;
				pair <string, string> L = make_pair( (A1 > A2)? A2: A1, (A1 > A2)? A1: A2);
				bool found = false;
				for (int k = 0 ; k < Set.size() && !found; k ++)
				{
					if (Set[k] == L)
						found = true;;
				}
				if (!found)
					Set.push_back(L);
			}
		}
		fout<<"Case #"<<i<<": "<<Set.size()<<endl;
		Set.clear();
	}
	return 0;
}