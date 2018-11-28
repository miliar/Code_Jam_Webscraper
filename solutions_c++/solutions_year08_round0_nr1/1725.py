// Alien.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <deque>
#include <map>
#include <string>
#include <algorithm>
#include <fstream>


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream fin("input.txt");
	std::ofstream fout("output.txt");

	if( !fin )
		return 0;

	int N;
	fin >> N;
	for( int case_no = 1; case_no <= N; case_no++ )
	{
		std::map<std::string,size_t> engines;
		//std::vector<std::string> engines;
		int S;
		fin >> S;
		for( int i = 0; i < S; i++ )
		{
			std::string str;
			while( str.empty() )
			{
				bool b = fin.eof();
				std::getline( fin, str );
				//fout << str << std::endl;
			}
			//engines.push_back( str );
			engines[str] = i;
		}
		std::vector<int> table;
		table.resize(S);
		int answer = 0;
		int counter = 0;
		int Q;
		int last_k = -1;
		int next_v = -1;
		fin >> Q;
		for( int q = 0; q < Q; q++ )
		{
			std::string str;
			while( str.empty() )
				std::getline( fin, str );
			//fout << str << std::endl;
			if( engines.find(str) != engines.end() )
			{
				if( last_k >=0 )
				{
					if( next_v == answer )
						counter--;
					table[last_k] = next_v;
				}
				size_t k = engines[str];
				if( table[k] == answer )
				{
					if( counter == S-1 )
					{
						counter = 1;
						answer++;
					}
					else
						counter++;
				}
				table[k] = -1;
				last_k = k;
				next_v = answer+1;
			}
		}
		fout << "Case #" << case_no << ": " << answer << "\n";
	}

	return 0;
}

