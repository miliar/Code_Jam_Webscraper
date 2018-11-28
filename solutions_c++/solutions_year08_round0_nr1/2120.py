#include <iostream>
#include <fstream>
#include <map>

using namespace std;

ifstream fin;
ofstream fout;

char line[1024];
int N, S, Q;



struct ltstr
{
  bool operator()(string s1, string s2) const
  {
    return strcmp(s1.c_str(), s2.c_str()) < 0;
  }
};

map<string, int, ltstr> servers;

void solve()
{
}

int main()
{
	int i, j, num, res;
	string str;
	map<string, int, ltstr>::iterator cur;

	fin.open("b.in");
	fout.open("A-small.out");

	fin >> N;
	fin.getline(line, 1024);

	for(i = 0; i < N; i ++)
	{
		fin >> S;
		fin.getline(line, 1024);

		for(j = 0; j < S; j ++)
		{
			fin.getline(line, 1024);
		//	string s;
		//	s = line;
			cout << line << endl;
			servers[line] = 0;
		}

		for(cur = servers.begin(); cur != servers.end(); cur ++)
		{
			str = (*cur).first;
			cout << "maps " << str.c_str() << endl;
		}

		fin >> Q;
		fin.getline(line, 1024);

		num = 0;
		res = 0;

		for(j = 0; j < Q; j ++)
		{
			fin.getline(line, 1024);
			if(servers[line] == 0)
			{
				num ++;
				servers[line] = 1;
			}

			if(num == S)
			{
				res ++;
				for(cur = servers.begin(); cur != servers.end(); cur ++)
				{
					(*cur).second = 0;
				}
				servers[line] = 1;
				num = 1;
			}
		}

		cout << "Case #" << i + 1 << ": " << res << endl;
		fout << "Case #" << i + 1 << ": " << res << endl;

		servers.clear();
		cout << "\n\n";
	}
}