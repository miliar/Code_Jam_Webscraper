#include <vector>
#include <iostream>
#include <iomanip>
#include <map>

using namespace std;

class dchar
{
public:
	dchar(char _c) : c(_c) {}
	char c;
	map<string,int> count;
};

int search(char *str, vector<dchar>::iterator it)
{
	//Check in cache
	map<string,int>::iterator cache	= it->count.find(str);
	if(cache != it->count.end())
		return cache->second;
	//Find all instances of first letter of str
	int res	= 0;
	
	vector<dchar>::iterator sr	= it;

	for(;sr->c  != 0;sr++)
		if(sr->c == str[0])
		{
			if(strlen(str) > 1)
				res	+= search(&str[1],sr+1);
			else
				res++;
		}
	res	%= 10000;
	it->count.insert(make_pair(str,res));
	return res;
}

int main()
{
	int c;
	cin >> c;

	vector<dchar> str;

	char buf[502];
	cin.getline(buf,501);

	for(int i = 0; i < c; i++)
	{
		str.clear();
		cin.getline(buf,501);
		

		int j	= strlen(buf);
		for(int i = 0; i < j; i++)
			str.push_back(dchar(buf[i]));

		str.push_back(0);

		int res	= search("welcome to code jam",str.begin());


		cout << "Case #" << i+1 << ": " << setfill('0') << setw(4) << res << endl;
	}
}
