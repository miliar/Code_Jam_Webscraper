#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<string> combinations;
vector<string> opposites;

char getCombination(char a, char b)
{
	for(int i = 0; i<combinations.size(); ++i)
		if( (combinations[i][0] == a && combinations[i][1] == b) ||
			(combinations[i][0] == b && combinations[i][1] == a))
				return combinations[i][2];
	return '#';
}

char getOpposed(char c)
{
	for(int i = 0; i<opposites.size(); ++i)
		if(opposites[i][0] == c)
			return opposites[i][1];
		else if (opposites[i][1] == c)
			return opposites[i][0];
	return '#';
}


string getAnswer(string& stack)
{
	string list;
	list.reserve(stack.size());
	list += stack[0];

	int j = 1;

	for(int i = 1; i<stack.size(); ++i)
	{
		list += stack[i];
		j++;
		if(list.size() < 2)
			continue;

		char replace = getCombination(list[list.size()-1], list[list.size()-2]);
		if(replace != '#') 
		{
			list.erase(list.end()-2, list.end());
			list += replace;
		}
		
		char del = getOpposed(list[list.size()-1]);
		if(list.find(del) != string::npos)
			list.clear();
	}

	return list;
}

string format(string s)
{
	string f;
	f.reserve(s.size() * 2 + 2);
	f += "[";
	if(s.size() > 1) for(int i = 0; i<s.size()-1; ++i)
	{
		f += s[i];
		f += ',';
		f += ' ';
	}
	if(s.size() > 0)
		f += s[s.size()-1];
	f += "]";
	return f;
}

int main()
{
	ifstream f("b.in");
	ofstream f2("b.out");

	int T;
	f>>T;

	for(int testcase = 1; testcase <= T; ++testcase)
	{
		combinations.clear();
		opposites.clear();
		string stack;

		int nr;

		f>>nr;
		for(int h = 0; h<nr; ++h)
		{
			string s;
			f>>s;
			combinations.push_back(s);
		}

		f>>nr;
		for(int h = 0; h<nr; ++h)
		{
			string s;
			f>>s;
			opposites.push_back(s);
		}

		f>>nr;
		f>>stack;

		f2<<"Case #"<<testcase<<": "<<format(getAnswer(stack))<<"\n";
	}

	return 0;
}