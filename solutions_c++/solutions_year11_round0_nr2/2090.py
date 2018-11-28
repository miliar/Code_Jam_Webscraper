#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

//vector<int> v;
//for(vector<int>::iterator it = v.begin(), end = v.end(); it != end; ++it)
//{
//}

int main(int argc, char* argv[])
{
	ifstream in("in");
	ofstream out("out");

	int T = 0;
	in >> T;

	REP (t, T)
	{
		map<string, char> replace;
		set<string> remove;
		string elements;

		int C = 0;
		in >> C;
		REP (i, C)
		{
			char buf[4] = {};
			in >> buf;
			replace[string(buf, buf+2)] = buf[2];
			string s;
			s.push_back(buf[1]);
			s.push_back(buf[0]);
			replace[s] = buf[2];
		}

		int D = 0;
		in >> D;
		REP (i, D)
		{
			char buf[3] = {};
			in >> buf;
			remove.insert(buf);
			string s;
			s.push_back(buf[1]);
			s.push_back(buf[0]);
			remove.insert(s);
		}

		int N = 0;
		in >> N;
		in >> elements;

		int i = 1;
		while (i < elements.size())
		{
			string s; s.push_back(elements[i-1]); s.push_back(elements[i]);
			
			map<string, char>::iterator find = replace.find(s);
			if (find != replace.end())
			{
				elements[i] = find->second;
				elements.erase(i-1, 1);
				continue;
			}

			REP (j, i)
			{
				string s; s.push_back(elements[j]); s.push_back(elements[i]);
				if (remove.find(s) != remove.end())
				{
					elements.erase(0, i+1);
					i = 0;
					break;
				}
			}

			++i;
		}

		stringstream stream;
		REP (i, elements.size())
		{
			if (i != 0)
				stream << ", ";
			stream << elements[i];
		}
		out << "Case #" << t+1 << ": " << "[" << stream.str() << "]" << "\n";	
	}

	in.close();
	out.close();

	return 0;
}
