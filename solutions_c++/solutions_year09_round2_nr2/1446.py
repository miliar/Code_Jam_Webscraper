#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <cstring>

using namespace std;

string calc(string& s,int val)
{
	sort(s.begin(),s.end());
	do
	{
		 char * cstring = new char [s.size()+1];
		 strcpy (cstring, s.c_str());
		 if(atoi(cstring) == val) break;
	}while(next_permutation(s.begin(),s.end()));
	next_permutation(s.begin(),s.end());
	char * cstring = new char [s.size()+1];
	strcpy (cstring, s.c_str());
	if(atoi(cstring)<=val) 
	{
		s.push_back('0');
		return calc(s,val);
	}
	else return s;
}

int main()
{
	int n;
	cin >> n;
	int c = 0;
	while(n)
	{
		n--;
		c++;
		string s;
		cin >> s;
		char * cstring = new char [s.size()+1];
		strcpy (cstring, s.c_str());
		cout << "Case #" << c << ": " << calc(s,atoi(cstring)) << endl;
	}
}

