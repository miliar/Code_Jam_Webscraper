// b1.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;

set<string> dirset;

int Add(string dir)
{
	int startingwith=0;
	int endingwith=0;
	int count = 0;
	while(endingwith!=string::npos)
	{
		endingwith = dir.find_first_of('/', startingwith+1);
		string rootdir = dir.substr(0, endingwith); //probably need to fix this when endingwith=npos
		startingwith=endingwith;
		if(dirset.find(rootdir)!=dirset.end())
		{
			continue;
		}
		dirset.insert(rootdir);
		count++;
	}
	return count;
}


int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	int N, M;
	for(int i=0; i<T; i++)
	{
		int count=0;
		cin >> N >> M;
		//Add("/home");
		for(int j=0; j<N; j++)
		{
			string directory;
			cin >> directory;
			Add(directory);
		}
		for(int j=0;j<M;j++)
		{
			string directory;
			cin >> directory;
			count += Add(directory);
		}
	
		cout << "Case #" << i+1 << ": " << count << endl;
		dirset.clear();
	}



	return 0;
}

