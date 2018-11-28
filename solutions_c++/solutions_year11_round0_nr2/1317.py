#include <iostream>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <map>
#include <string>

using namespace std;

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	
	int T;
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		fout << "Case #" << i+1 << ": ";
		
		int C;
		string combine[40];
		int D;
		string oppose[40];
		int N;
		string input;
		fin >> C;
		for(int j = 0; j < C; j++)
			fin >> combine[j];
		fin >> D;
		for(int j = 0; j < D; j++)
			fin >> oppose[j];
		fin >> N;
		fin >> input;
		
		map<string,char> MC;
		for(int j = 0; j < C; j++)
		{
			string s;
			s += combine[j][0];
			s += combine[j][1];
			MC[s] = combine[j][2];
			swap(s[0],s[1]);
			MC[s] = combine[j][2];
		}
		
		bool OPP[26][26];
		for(int j = 0; j < 26; j++)
			for(int k = 0; k < 26; k++)
			OPP[j][k] = 0;
	
		for(int j = 0; j < D; j++)
			OPP[oppose[j][0]-'A'][oppose[j][1]-'A'] = OPP[oppose[j][1]-'A'][oppose[j][0]-'A'] = 1;
		
		string curr;
		for(int j = 0; j < N; j++)
		{
			curr += input[j];
			while(curr.size() > 1)
			{
				string tmp;
				tmp += curr[curr.size()-1];
				tmp += curr[curr.size()-2];
				if(MC.find(tmp) != MC.end())
				{
					curr[curr.size()-2] = MC[tmp];
					curr.erase(curr.size()-1);
				}
				else break;
			}
			
			int bad = 0;
			for(int k = 0; k < curr.size()-1; k++)
			{
				if(OPP[curr[curr.size()-1]-'A'][curr[k]-'A'])
				{
					bad = 1;
					break;
				}
			}
			if(bad) curr = "";
		}
		
		fout << "[";
		if(curr == "") fout << "]\n";
		else 
		{
			fout << curr[0];
			for(int t = 1; t < curr.size(); t++)
				fout << ", " << curr[t];
			fout << "]\n";
		}
	}
	return 0;
}