#include "iostream"
#include "fstream"
#include "string"
#include "stack"

using namespace std;

#define small_in "C-small.in"
#define small_out "C-small.out"
#define large_in "C-large.in"
#define large_out "C-large.out"

int tbl[500][19];

int Find(const int src, const int welcome_index, const string line, const string welcome)
{
	int n_src = line.length();
	int n_welcome = welcome.length();
	if(tbl[src][welcome_index] != -1)
	{
		return tbl[src][welcome_index];
	}
	if(n_src - src < n_welcome - welcome_index)
	{
		tbl[src][welcome_index] = 0;
		return 0;
	}
	if(n_src - src == n_welcome - welcome_index)
	{
		string sub_src = line.substr(src, n_src - src);
		string sub_welcome = welcome.substr(welcome_index, n_welcome - welcome_index);
		tbl[src][welcome_index] = (sub_src == sub_welcome) ? 1:0;
		return tbl[src][welcome_index];
	}
	int total = 0;
	total += Find(src+1, welcome_index, line, welcome);
	total %= 10000;
	if(line[src] == welcome[welcome_index])
	{
		total += Find(src+1, welcome_index+1, line, welcome);
		total %= 10000;
	}
	tbl[src][welcome_index] = total;
	return total;
}

void main()
{
	ifstream infile;
	infile.open(small_in);
	ofstream outfile;
	outfile.open(small_out);

	string welcome = "welcome to code jam";
	int N;
	infile >> N;
	infile.get();
	for(int i=0; i<N; i++)
	{
		string line;
		char* c_str = new char[501];
		infile.getline(c_str, 501);
		line = c_str;
		for(int j=0; j<(int)line.length(); j++)
		{
			int found = welcome.find_first_of(line[j]);
			if(found == string::npos)
			{
				line.erase(line.begin() + j);
				j--;
			}
		}
		int found = line.find_first_of("w");
		if(found != string::npos)
		{
			line.erase(line.begin(), line.begin() + found);
		}
		found = line.find_last_of("m");
		if(found != string::npos)
		{
			line.erase(line.begin() + found + 1, line.end());
		}

		memset(tbl, -1, 500*19);
		int count = Find(0, 0, line, welcome);
		outfile << "Case #" << i+1 << ": ";
		if(count < 10) outfile << "000";
		else if(count < 100) outfile << "00";
		else if(count < 1000) outfile << "0";
		outfile << count;
		outfile << endl;
	}

	infile.close();
	outfile.close();
}