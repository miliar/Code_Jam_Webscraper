#include <iostream>
#include <vector>
#include <iterator>
#include <sstream>
#include <algorithm>
#include <set>
#include <string>


using namespace std;

set<string> dirs;
int mkdir_count;


void make_dir(string path)
{
	string parent = path.substr(0, path.rfind('/'));
	if ( parent == "") parent = "/";
	if ( dirs.find(parent) == dirs.end() )
		make_dir( parent );
	dirs.insert(path);
	mkdir_count++;
}

int main()
{
	int cases; cin >> cases;		// number of cases T
	//cin.ignore();

	for ( int ca = 1; ca <= cases; ++ca )
	{   
		cerr << "Test: " << ca << endl;  
		mkdir_count = 0;
		dirs.clear();
		dirs.insert("/");
		string path;

		int N, M;
		cin >> N >> M;
		for (int i = 1; i <= N; ++i)
		{
			cin >> path;
			//cout << path << endl;
			dirs.insert(path);
		}

		for (int i = 1; i<=M; ++i)
		{
			cin >> path;
			//cout << path << endl;
			if ( dirs.find(path) == dirs.end() )
				make_dir(path);
		}

		cout << "Case #" << ca << ": " 
	    	 << mkdir_count 
			 << endl;
	}
	return 0;
}
