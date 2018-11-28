#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>

using namespace std;

vector <string> split(const string _s, const string del);
int toInt(string s) {int r = 0; istringstream ss(s); ss >> r; return r;}
string toStr(int n) {ostringstream ss; ss << n; return ss.str();}


//string run(vector <string> inputs)
string run(string str)
{
	int sum = 0;
	int sub = 0;
	vector <string> strVec = split(str, string(" "));
	string A = strVec[0];
	string B = strVec[1];
	int a = toInt(A);
	int b = toInt(B);

	if (a <= 9)
	{
		a = 12;
	}

	for (int i = a; i <= b; i++)
	{
		string I = toStr(i);
		if (I.substr(1, 1) != string("0"))
		{
			string C = I.substr(1) + I.substr(0, 1);
			int c = toInt(C);
			if (a <= c && c <= b && c != i)
			{
				if (12 <= c && c <= 99)
				{
					sub++;
				}
				else
				{
					sum++;
				}
			}
		}
	}

	return toStr(sum + sub/2);
}

int main(int argc, char ** argv)
{
  if (argc != 2)
  {
    cout << "Usage " << argv[0] << " <input file name>\n";
    return 0;
  }

  ifstream file (argv[1]);
  string line;
  vector <string> tmp;
  vector <int> args;

  getline(file, line);
  tmp = split(line, " ");
  for (int i=0; i<tmp.size(); i++) args.push_back(toInt(tmp[i]));

  std::ofstream ofs("out.txt");
  for (int lineNum = 0; lineNum<args[0]; lineNum++)
    {
      string result;

      getline(file, line);

      result = run(line);

      cout << "Case #" << lineNum+1 << ": " << result << endl;
      ofs << "Case #" << lineNum+1 << ": " << result << endl;
    }
  return 0;
}

vector <string> split(const string _s, const string del)
{
  vector <string> ret;
  string s = _s;

  while (!s.empty())
    {
      size_t pos = s.find(del);
      string sub = "";
      sub = s.substr(0, pos);
      ret.push_back(sub);
      if (pos != string::npos)
	pos += del.size();
      s.erase(0, pos);
    }

  return ret;
}
