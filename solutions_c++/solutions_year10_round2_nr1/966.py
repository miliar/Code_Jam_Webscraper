// CodeJam2010-2.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <algorithm>

using namespace std;

static int total = 0;

struct Tree
{
	bool add(list<string>& path)
	{
		if(path.empty()) return true;

		path.pop_front();
		if(path.empty()) return true;

		for(size_t i = 0; i < m_vChild.size(); ++i)
		{
			if(0 == m_vChild[i].m_name.compare(path.front()))
			{
				m_vChild[i].add(path);
				return true;
			}
		}

		//not found
		++total;
		Tree new_child;
		new_child.m_name = path.front();
		m_vChild.push_back(new_child);
		m_vChild.back().add(path);

		return true;
	}

	string m_name;
	vector<Tree> m_vChild;

};


int main(long argc, char* argv[])
{
	ifstream in(argv[1]);

	string line;
	
	getline(in, line);
	
	int counter = atoi(line.c_str());

	for(int i = 0; i < counter; ++i)
	{
		int N = 0;
		int M = 0;
		getline(in, line);
		sscanf(line.c_str(), "%d %d", &N, &M);

		Tree tree;
		tree.m_name = "root";

		for(int j = 0; j < N; ++j)
		{
			getline(in, line);
			list<string> path;
			path.push_back("root");
			char* tok = (char*)line.c_str();
			path.push_back(string(strtok(tok, "/")));
			while(true)
			{
				char* tmp = strtok(NULL, "/");
				if(!tmp) break;
					
				path.push_back(string(tmp));
			}
			tree.add(path);
		}

		int total_ = total;
		//if(total_ == 0) total_ += 1;

		for(int j = 0; j < M; ++j)
		{
			getline(in, line);
			list<string> path;
			path.push_back("root");
			char* tok = (char*)line.c_str();
			path.push_back(string(strtok(tok, "/")));
			while(true)
			{
				char* tmp = strtok(NULL, "/");
				if(!tmp) break;
					
				path.push_back(string(tmp));
			}
			tree.add(path);
		}

	/*	vector<int> vec;
		char* tok = (char*)line.c_str();
		vec.push_back(atoi(strtok(tok, "/")));
		for(int j = 1; j < N; ++j)
		{
			vec.push_back(atoi(strtok(NULL, "/")));
		}*/



		printf("Case #%d: %d\n", i+1, total - total_);
	


	}
	return 0;
}

