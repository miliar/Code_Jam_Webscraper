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
#include <iomanip>
#include <math.h>


using namespace std;

vector <string> split(const string _s, const string del);
int toInt(string s) {int r = 0; istringstream ss(s); ss >> r; return r;}
string toStr(int n) {ostringstream ss; ss << n; return ss.str();}
double toDouble(string s) {
    setprecision(15);
    istringstream is;
    is.str(s);
    double x;
    is >> x;
	return x;
}

std::ofstream ofs("out.txt");
string line;
int A;
int B;

//string run(vector <string> inputs)
string run(string str)
{
    vector <string> strVec = split(str, string(" "));
    A = toInt(strVec[0]);
    B = toInt(strVec[1]);

	return("\n");
}

string run2(string str)
{
	double p[99999];
	vector <string> strVec = split(line, string(" "));
	for (int i = 0; i < A; i++)
	{
        p[i] = toDouble(strVec[i]);
	}

	vector<double> pp;
	for (int i = 0; i < A+1; i++)
	{
		double ppp = 1;
		for (int j = 0; j < A; j++)
		{
			if (j+i == A)
			{
	    		ppp *= (1-p[j]);
				break;
			}
			else
			{
				ppp *= p[j];
			}
		}
		pp.push_back(ppp);
	}

	vector<double> sumsum;
	for (int k = 0; k < A+1; k++)
	{
		double base = B-A+1+k*2;
		double sum = 0;
		for (int i = 0; i< A+1; i++)
		{
			if (k < i)
			{
				sum += pp[i] * (base+B+1);
			}
			else
			{
				sum += pp[i] * base;
			}
		}
		sumsum.push_back(sum);
	}
	sumsum.push_back(B+2);

	double min = sumsum[0];
	for(int i = 0; i < sumsum.size(); i++)
	{
		if (sumsum[i] < min)
		{
			min = sumsum[i];
		}
	}
	char c[100];
	sprintf(c, "%f",min);
	return(string(c));
}



int main(int argc, char ** argv)
{
  if (argc != 2)
  {
    cout << "Usage " << argv[0] << " <input file name>\n";
    return 0;
  }

  ifstream file (argv[1]);
  vector <string> tmp;
  vector <int> args;

  getline(file, line);
  tmp = split(line, " ");
  for (int i=0; i<tmp.size(); i++) args.push_back(toInt(tmp[i]));

  for (int lineNum = 0; lineNum<args[0]; lineNum++)
    {
      string result;

      getline(file, line);
	  run (line);

	  getline(file, line);
      result = run2(line);

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
