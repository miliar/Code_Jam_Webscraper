#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <fstream>
#include <map>
#include <algorithm>
#include <sstream>
#include <list>

using namespace std;

const char INPUT_FILE[] = "Alarge.txt";
const char OUTPUT_FILE[] = "out.txt";

bool good(int r, const string &v)
{
	for(int i = r + 1; i < v.size(); i++)
	{
		if(v[i] > '0')
			return false;
	}
	return true;
}

void solve(ifstream &in, ofstream &out, int testNum)
{
	int N;
	in >> N;
	list<string> M;
	string t;
	for(int i = 0; i < N; i++)
	{
		in >> t;
		M.push_back(t);
	}
	int cnt = 0;
	for(int i = 0; i < N - 1; i++)
	{
		int j = 0;
		for (list<string>::iterator it = M.begin(); it != M.end(); ++it)
		{
			if(good(i, *it))
			{
				M.erase(it);
				cnt += j;
				break;
			}
			j++;
		}
	}
	out << "Case #" << testNum << ": " << cnt << endl;
}

int main()
{
	ifstream in;
	ofstream out;
	in.open(INPUT_FILE);
	out.open(OUTPUT_FILE);
	int N;
	in >> N;
	for(int i = 1; i <= N; i++)
	{
		solve(in, out, i);
	}
	out.close();
	in.close();
}