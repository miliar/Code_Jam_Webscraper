#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
#include <ios>
#include <functional>

using namespace std;
typedef unsigned long long ull;

int main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");
	if(ifs.is_open() && ofs.is_open())
	{
		int T;
		ifs>>T;
		int t=0;
		while(ifs.good() && t<T)
		{
			int N, M, res = 0;
			ifs>>N>>M;
			vector<string> v;
			string str;
			for(int i=0; i<N; i++)
			{
				ifs>>str;
				v.push_back(str);
			};
			for(int i=0; i<M; i++)
			{
				ifs>>str;
				string str2="";
				int pos = 0;
				while(str!=str2)
				{
					pos++;
					pos = str.find('/', pos);
					if(string::npos != pos)
						str2.assign(str,0,pos);
					else
						str2 = str;
					if(v.end() == find(v.begin(), v.end(), str2))
					{
						v.push_back(str2);
						res++;
					}
				}
			}

			ofs<<"Case #"<<++t<<": "<<res<<"\n";
			cout<<t<<" complited\n";
		}
	}
	ifs.close();
	ofs.close();
	return 0;
}