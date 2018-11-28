#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

typedef unsigned long long int ull;
typedef long double ld;

int N, M;
int cnt = 0;
string path[100];

void counting()
{
	cnt++;
}

class filetree
{
	public:
	string name;
	vector<class filetree*> dirs;
			bool add(string path)
			{
//			cout << "here" << endl; 
			if (path.length() == 1)
				return 0;
			string cur;
			cur = path.substr(1, path.find('/', 1)-1);
			int found = 0; 		
			vector<class filetree*>::iterator temp;
			for (vector<class filetree*>::iterator i=dirs.begin();i<dirs.end();i++)
			{
				if ((*i)->name == cur)
				{
					found = 1;
					temp = i;
					break;
				}
			}
			
			if (found == 0)
			{
//			cout << "here" << endl;
				dirs.push_back(new class filetree);
				dirs.back()->name = cur;
				temp = dirs.end()-1;
				counting(); //			cout << "also "  << path.substr(path.find('/', 1), path.length()-1) << endl;
			}
					
//			cout << "heres " << cur << " and " << path << endl << path.find('/', 1) << endl << path.length()-1  << endl;

				(*temp)->add(path.substr(path.find('/', 1), path.length()-1));

			return 0;
		}
			
};


int main()
{
	ofstream out;
	ifstream in;
	out.open("A-large.OUT");
	in.open("A-large.in");
	int T;
	in >> T;
	for (int testcase=0;testcase<T;testcase++)
	{
		in >> N >> M;
class filetree ft;
		for (int i=0;i<N;i++)
		{
			in >> path[i];
			path[i] = path[i] + "/";
			ft.add(path[i]);
		}
		cnt = 0;
		for (int i=0;i<M;i++)
		{
			in >> path[i];
			path[i] = path[i] + "/";
//		cout << path[i] << endl;
			ft.add(path[i]);
		}	
		out <<  "Case #" << testcase+1 << ": " << cnt << endl;
		cout << "Case #" << testcase+1 << ": " << cnt << endl;
	}
	system("PAUSE");	
	return 0;
}

