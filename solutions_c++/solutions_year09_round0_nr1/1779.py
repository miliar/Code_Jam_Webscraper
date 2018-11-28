#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cstdlib>
#include <fstream>
using namespace std;


typedef set<char> MatchSet;
typedef vector<MatchSet> MatchStr;

void ReadAll(istream & in, int & L, int & D, int & N, vector<string> & VecStr, vector<MatchStr> & VecTest)
{
	string TempStr;
	in >> L >> D >> N;
	for(int i = 0; i < D; i++)
	{
		in >> TempStr;
		VecStr.push_back(TempStr);
	}
	for(int i = 0; i < N; i++)
	{
		MatchStr mstrStr;
		in >> TempStr;
		int size = TempStr.size(), pos = 0;
		while(pos != size)
		{
			while((pos != size) && TempStr[pos] != '(')
		    {
				MatchSet mstrSet;
			    mstrSet.insert(TempStr[pos]);
			    mstrStr.push_back(mstrSet);
			    pos++;
		    }
		    if(pos == size) break;
		    pos++;
		    MatchSet mstrSet;
		    while((pos != size) && TempStr[pos] != ')')
		    {
				mstrSet.insert(TempStr[pos]);
				pos++;
			}
			if(pos == size) break;
			mstrStr.push_back(mstrSet);	
			pos++;		
		}
		VecTest.push_back(mstrStr);
	}
}

bool match(string & str, MatchStr & matchstr)
{
	for(int i = 0; i < str.size(); i++)
	{
		if(! matchstr[i].count(str[i])) return false;
	}
	return true;
}

void MatchAndOutput(ostream & out, int L, int D, int N, vector<string> & VecStr, vector<MatchStr> & VecTest)
{
	for(int i = 0; i < N; i++)
	{
		int cnt = 0;
		for(int j = 0; j < D; j++)
		{
			if(match(VecStr[j], VecTest[i]))
			{
				cnt++;	
			}
		}
		out << "Case #" << i+1 << ": " << cnt << endl;
	}	
}



int main()
{
	int L, D, N;
	vector<string> VecStr;
	vector<MatchStr> VecTest;
	ifstream in_file;
	ofstream out_file;
	
	in_file.open("A-large.in");
	out_file.open("LargeOut.txt");
	
	if(!in_file || !out_file)
	{
		cerr << "cannot open the file!" << endl;
		exit(1);
	}
	
	ReadAll(in_file, L, D, N, VecStr, VecTest);
	MatchAndOutput(out_file, L, D, N, VecStr, VecTest);
	
	in_file.close();
	out_file.close();
	
	system("pause");
	
	return 0;
}
