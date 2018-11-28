// a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector>

using namespace std;

string getParent(string path)
{
	int s = path.find_last_of('/');
	return path.substr(0,s);
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	ifstream fin("a.in");
	ofstream fout("a.out");
	fin>>t;
	for(int i = 0; i < t; i++)
	{
		int n,m;
		int count = 0;
		fin>>n>>m;
		set<string> paths;
		for(int k = 0; k < n;k++)
		{
			string path;
			fin>>path;
			paths.insert(path);
		}
		
		for(int k = 0; k < m; k++)
		{
			string path, parent, child;
			fin>>path;
			parent = path;
			while(!parent.empty())
			{
				if(paths.find(parent) == paths.end())
				{
					count++;
					paths.insert(parent);
				}
				parent = getParent(parent);
				cout<<parent<<endl;
			}
		}
		fout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}

