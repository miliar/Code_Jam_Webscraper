#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

int main()
{
	string file = "A-large";
//	string file = "";
//	string file = "";
	ifstream ifs((file+".in").c_str());
	ofstream ofs((file+".out").c_str());
	int N;
	string buf;
	long long res;
	map<char, int> m;
	int count;
	int base;

	getline(ifs, buf);
	N = atoi(buf.c_str());
	for(int n=0; n<N; n++)
	{
		getline(ifs, buf);
		m.clear();
		count = 0;
		res = 0;
		for(int i=0; i<buf.size(); i++) if(m.find(buf[i]) == m.end())
		{
			if(m.size() == 0) { m[buf[i]] = 1; continue; }
			else if(m.size() == 1) { m[buf[i]] = 0; count = 2; continue; }
			m[buf[i]] = count++;
		}
		base = m.size();
		if(base == 1) base = 2;
		for(int i=0; i<buf.size(); i++) res = res * base + m[buf[i]];
		ofs << "Case #" << n+1 << ": " << res << endl;
		cout << n << endl;
	}

	return 0;
}


