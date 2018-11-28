#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char a[26] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
char b[200];

int main()
{
//	ifstream f1("in.txt");
//	ifstream f2("in2.txt");
	
//	string s1,s2;

//	getline(f1, s1);
//	getline(f2, s2);

//	for (int i = 0; i < s1.length(); i++)
//		b[s2[i] - 'a'] = s1[i];// - 'a';

	for(int i = 0; i < 26; i++)
		b[a[i]] = i + 'a';

	int t;
	cin >> t;
	string temp;
	getline(cin, temp);

	for(int i=0; i <t; i++)
	{
		string s;
		getline(cin, s);
		//cout << i <<' ' << s;

		string res;

		for (int j = 0; j < s.length(); j++)
			if (s[j] == ' ')
				res.push_back(' ');
			else
				res.push_back(b[s[j]]);

		cout << "Case #" << i+1 << ": "<<res << endl;
	}

	return 0;
}