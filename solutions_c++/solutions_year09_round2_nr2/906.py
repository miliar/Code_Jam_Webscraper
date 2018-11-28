#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	string file = "B-large";
	ifstream ifs((file+".in").c_str());
	ofstream ofs((file+".out").c_str());
	int n;
	string buf;
	bool flag;
	string tmp = "";

	getline(ifs, buf);
	n = atoi(buf.c_str());
	for(int i=0; i<n; i++)
	{
		flag = true;
		getline(ifs, buf);
		flag = next_permutation(buf.begin(), buf.end());
		if(!flag)
		{
			sort(buf.begin(), buf.end());
			for(int j=0; j<buf.size(); j++) if(buf[j] != '0')
			{
				tmp = buf.substr(j, 1);
				buf.erase(j, 1);
				break;
			}
			buf.insert(0, "0");
			buf.insert(0, tmp);
		}
		ofs << "Case #" << i+1 << ": " << buf << endl;
		cout << i << endl;
	}

	return 0;
}

