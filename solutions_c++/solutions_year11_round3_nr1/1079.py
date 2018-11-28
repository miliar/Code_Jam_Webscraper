#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define LEN 50000
#define INPUT "C:\\temp\\A-small.in"


static void print(string i)
{
	cout<<i<<endl;
}

static string readline(ifstream& ifs)
{
	char line[LEN];
	ifs.getline(line, LEN);
	string s = line;
	return s;
}

static string int_to_string(long i)
{
	ostringstream oss;
	oss<<i;
	return oss.str();
}

static long string_to_int(string s)
{
	istringstream iss(s);
	int i;
	iss>>i;
	return i;
}


template<class T>
void println(T var)
{
	cout<<var<<endl;
}


bool trythis(vector<string>& m)
{
	bool ret = false;
	int r = m.size();
	int c = m[0].size();

	for(int i=0; i<r; i++)
	{
		for(int j=0; j<c; j++)
		{
			if(m[i][j] == '#')
			{
				if(i+1 < r && j+1 < c)
				{
					if(m[i][j+1] == '#' && m[i+1][j] == '#' && m[i+1][j+1] == '#')
					{
						m[i][j] = '/';
						m[i+1][j] = '\\';
						m[i][j+1] = '\\';
						m[i+1][j+1] = '/';
					}
				}
			}
		}
	}

	for(int i=0; i<r; i++) 
		for(int j=0; j<c; j++)
			if(m[i][j] == '#')
				return false;
	return true;
}


void solve(vector<string>& m)
{
	int rows = m.size();
	int cols = m[0].size();

	bool success = false;
	if(trythis(m))
	{
		success = true;
		for_each(m.begin(), m.end(), println<string>);
	}

	if(success)
			return;

	cout<<"Impossible"<<endl;
}


int main()
{
	ifstream ifs;
	ifs.open(INPUT);

	int ncases = string_to_int(readline(ifs));

	for(int nc=0; nc<ncases; nc++)
	{
		cout<<"Case #"<<nc+1<<": "<<endl;
		int r,c;
		string rc = readline(ifs);
		istringstream isrc(rc);
		isrc>>r>>c;

		string row(c, ' ');
		vector<string> mat(r, row);
	
		for(int i=0; i<r; i++)
			mat[i] = readline(ifs);

		//for_each(mat.begin(), mat.end(), println<string>);

		solve(mat);
	}

	return 0;
}