#include <iostream>
#include <string>

using namespace std;

int main()
{
	char array[26];
	string str;

	array['y'-'a'] = 'a';
	array['n'-'a'] = 'b';
	array['f'-'a'] = 'c';
	array['i'-'a'] = 'd';
	array['c'-'a'] = 'e';
	array['w'-'a'] = 'f';
	array['l'-'a'] = 'g';
	array['b'-'a'] = 'h';
	array['k'-'a'] = 'i';
	array['u'-'a'] = 'j';
	array['o'-'a'] = 'k';
	array['m'-'a'] = 'l';
	array['x'-'a'] = 'm';
	array['s'-'a'] = 'n';
	array['e'-'a'] = 'o';
	array['v'-'a'] = 'p';
	array['z'-'a'] = 'q';
	array['p'-'a'] = 'r';
	array['d'-'a'] = 's';
	array['r'-'a'] = 't';
	array['j'-'a'] = 'u';
	array['g'-'a'] = 'v';
	array['t'-'a'] = 'w';
	array['h'-'a'] = 'x';
	array['a'-'a'] = 'y';
	array['q'-'a'] = 'z';

	int count = 0;
	cin >> count;
	getline(cin, str);
	
	for(int i = 0; i < count; i++)
	{
		string oldstr, newstr;
		getline(cin, oldstr);
		for(int j = 0; j < oldstr.size(); j++)
		{
			if('a' <= oldstr[j] && oldstr[j] <= 'z')
			{
				newstr += array[int(oldstr[j] - 'a')];
			}
			else
			{
				newstr += oldstr[j];
			}
		}
		cout << "Case #" << (i+1) << ": " << newstr << endl;
	}

	return 0;

}
