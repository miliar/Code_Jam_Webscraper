#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
vector<string> split( const string& s, const string& delim =" " ) {
	vector<string> res;
	string t;
	for ( int i = 0 ; i != s.size() ; i++ ) {
		if ( delim.find( s[i] ) != string::npos ) {
			if ( !t.empty() ) {
				res.push_back( t );
				t = "";
			}
		} else {
			t += s[i];
		}
	}
	if ( !t.empty() ) {
		res.push_back(t);
	}
	return res;
}

int main()
{
	int res = 0;
	fstream fin,fout;
	fin.open("D:\\coding\\codejam2010_round1\\codejam2010_round1\\A-large.in",ios_base::in);
	fout.open("D:\\coding\\codejam2010_round1\\codejam2010_round1\\A-large.out",ios_base::out);

	int T;
	fin >> T;
	for (int caseId = 0; caseId < T; caseId++)
	{
		int N,M;
		fin >> N >> M;
		int cmds = 0;
		vector<string> dir1,dir2;
		for(int i = 0; i < N; i++)
		{
			string eachline;
			fin >> eachline;
			dir1.push_back(eachline);
		}

		for(int i = 0; i < M; i++)
		{
			string eachline;
			fin >> eachline;
			bool found = false;
			vector<string> tmp = split(eachline,"/");
			vector<int> comm;
			if(dir1.empty())
			{
				dir1.push_back(eachline);
				cmds += tmp.size();
			}
			else
			{
				for(int j = 0; j < dir1.size(); j++)
				{
					if(eachline == dir1[j])
					{
						found = true;
						break;
					}
					else
					{
						vector<string> tmp2 = split(dir1[j],"/");
						int commlen = tmp.size() > tmp2.size() ? tmp2.size() : tmp.size();
						int k = 0;
						while(k < commlen && tmp[k] == tmp2[k])
						{
							k++;
						}
						comm.push_back(k);						
					}
				}
			
				if(!found)
				{
					sort(comm.begin(),comm.end());
					cmds += tmp.size()-comm.back();
					dir1.push_back(eachline);
				}
			}
					
		}

		cout << caseId << endl;
		fout << "Case #" << caseId+1 << ": " << cmds << endl;
	}

	fin.close();
	fout.close();
	return res;
}