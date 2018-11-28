#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define LEN 50000
#define INPUT "C:\\temp\\C-small.in"


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

bool possible(vector<int>& notes, int n)
{
	int less, more;
	for(int i=0; i<notes.size(); i++)
	{
		less = min(notes[i], n);
		more = max(notes[i], n);

		if(more%less != 0)
			return false;
	}
	return true;
}

int main()
{
	ifstream ifs;
	ifs.open(INPUT);

	int ncases = string_to_int(readline(ifs));

	for(int nc=0; nc<ncases; nc++)
	{
		int N, L, H;
		string nlh = readline(ifs);
		istringstream isnlh(nlh);
		isnlh>>N>>L>>H;

		vector<int> onotes;
		string onotestr = readline(ifs);
		istringstream ostr(onotestr);
		int t=N, tn;
		while(t--) 
		{
			ostr>>tn;
			onotes.push_back(tn);
		}

		string res = "NO";
		for(int n=L; n<=H; n++)
		{
			if(possible(onotes,n))
			{
				res = int_to_string(n);
				break;
			}
		}


		cout<<"Case #"<<nc+1<<": "<<res<<endl;
	}

	return 0;
}