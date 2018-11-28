#include <sstream>
#include <fstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

int main()
{

	map<char, char> rel;
	map<char, char> relrev;
	rel['a'] = 'y';
	rel['o'] = 'e';
	rel['z'] = 'q';
	relrev['y'] = 'a';
	relrev['e'] = 'o';
	relrev['q'] = 'z';
	string string1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string string2 = "our language is impossible to understand";

	int len = string1.length();
	for(int i = 0; i < len; i++)
	{
		rel[string2.at(i)] =  string1.at(i);
		relrev[string1.at(i)] =  string2.at(i);
	}

	string1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string2 = "there are twenty six factorial possibilities";

	len = string1.length();
	for(int i = 0; i < len; i++)
	{
		rel[string2.at(i)] =  string1.at(i);
		relrev[string1.at(i)] =  string2.at(i);
	}

	string1 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string2 = "so it is okay if you want to just give up";

	len = string1.length();
	for(int i = 0; i < len; i++)
	{
		rel[string2.at(i)] =  string1.at(i);
		relrev[string1.at(i)] =  string2.at(i);
	}

	int relsize = rel.size();

	vector<char> missingleft;
	vector<char> missingright;

	for(char x = 'a'; x <= 'z'; x++)
	{
		if(rel.find(x) == rel.end())
		{
			missingleft.push_back(x);
		}
	}

	for(char x = 'a'; x <= 'z'; x++)
	{
		if(relrev.find(x) == relrev.end())
		{
			missingright.push_back(x);
		}
	}

	if(missingleft.size() != missingright.size())
	{
		return 1;
	}

	for(int i = 0; i < missingleft.size(); i++)
	{
		rel[missingleft[i]] = missingright[i];
		relrev[missingright[i]] = missingleft[i];
	}

  
  ifstream ifs("input.txt");
  ofstream ofs("output.txt");

  string line;
  getline(ifs, line);
  istringstream ss(line);
  int cases;
  ss >> cases;
  
  for(int i = 0; i < cases; i++)
  {
	string res = "";
	getline(ifs, line);
	int len = line.length();
	for(int j = 0; j < len; j++)
	{
		char test = line.at(j);
		if(relrev.find(line.at(j)) == relrev.end())
		{
			int kk = 0;
		}
		res += relrev[line.at(j)];
	}
	ofs <<  "Case #" << i+1 << ": " << res << endl;
  }

	
	return 0;

  

}