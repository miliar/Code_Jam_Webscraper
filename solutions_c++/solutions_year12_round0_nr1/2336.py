#include <iostream>
#include <map>
#include <cassert>
#include <string>
#include <cstdlib>

using namespace std;

map<char, char> mapping;

char trans1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
char trans2[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char trans3[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

char orig1[] = "our language is impossible to understand";
char orig2[] = "there are twenty six factorial possibilities";
char orig3[] = "so it is okay if you want to just give up";

void training(char *trans, char *orig)
{
	while (*trans != '\0')
	{
		assert((mapping.find(*trans) == mapping.end()) || mapping[*trans] == *orig);
		if (mapping.find(*trans) == mapping.end())
			mapping[*trans] = *orig;
		trans++;
		orig++;
	}
	assert(*orig == '\0');
	return;
}

int main()
{
	string		s;
	int		n, caseno = 1;

	mapping['q'] = 'z';
	mapping['z'] = 'q';
	training(trans1, orig1);
	training(trans2, orig2);
	training(trans3, orig3);
	getline(cin, s);
	n = atoi(s.c_str());
	for (caseno = 1; caseno <= n; caseno++)
	{
		getline(cin, s);
		cout << "Case #" << caseno << ": ";
		for (int i = 0; i < s.length(); i++)
		{
			assert(mapping.find(s[i]) != mapping.end());
			cout << mapping[s[i]];
		}
		cout << endl;
	}
	return 0;
}
