#include <iostream>
#include <vector>
#include <string>

using namespace std;

int lookupArray[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

void convertString(string &str)
{
	for(int i=0; i<str.size(); i++)
	{
		bool upper = false;
		if(str[i]<91 && str[i]>64)
		{
			upper = true;
		}
		char lookup = tolower(str[i]);

		if(lookup != 32)
		{
			str[i] = lookupArray[lookup-97];
		}
	}
}


int main(void)
{
	int testcases = 0;
	vector<string> mystrings;
	
	string temp;
	getline(cin, temp);
	testcases = atoi(temp.c_str());

	for(int i=0; i<testcases; i++)
	{
		string newtestcase;
		getline(cin,newtestcase);
		convertString(newtestcase);
		mystrings.push_back(newtestcase);
	}

	for(int i=0; i<mystrings.size(); i++)
	{
		cout << "Case #" << i+1 <<  ": " <<mystrings[i] << endl;
	}

	return 0;
}