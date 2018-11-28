#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
//	string file = "sample";
//	string file = "A-small-attempt0";
	string file = "A-large";
	ifstream ifs((file+".in").c_str());
	ofstream ofs((file+".out").c_str());
	int T;
	string buf;
	int N;
	vector<int> v;
	int res;

	getline(ifs, buf);
	T = atoi(buf.c_str());
	for(int t=0; t<T; t++)
	{
		res = 0;
		v.clear();
		getline(ifs, buf);

		N = atoi(buf.c_str());
		for(int n=0; n<N; n++)
		{
			getline(ifs, buf);
			v.push_back(buf.rfind("1"));
//			cout << buf.rfind("1") << "  !!!!" << endl;
		}

		for(int n=0; n<N; n++)
		{
			for(int r=0; r<v.size(); r++) if(v[r] <= n)
			{
				res += r;
				v.erase(v.begin()+r);
				break;
			}
		}

		ofs << "Case #" << t+1 << ": " << res <<endl;
		cout << t+1 << endl;
	}

	return 0;
}


