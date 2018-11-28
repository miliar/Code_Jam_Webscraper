#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	map<char, char> dic;
	dic['a'] = 'y';
	dic['b'] = 'h';
	dic['c'] = 'e';
	dic['d'] = 's';
	dic['e'] = 'o';
	dic['f'] = 'c';
	dic['g'] = 'v';
	
	dic['h'] = 'x';
	dic['i'] = 'd';
	dic['j'] = 'u';
	dic['k'] = 'i';
	dic['l'] = 'g';
	dic['m'] = 'l';
	dic['n'] = 'b';
	
	dic['o'] = 'k';
	dic['p'] = 'r';
	dic['q'] = 'z';
	dic['r'] = 't';
	dic['s'] = 'n';
	dic['t'] = 'w';
	dic['u'] = 'j';

	dic['v'] = 'p';
	dic['w'] = 'f';
	dic['x'] = 'm';
	dic['y'] = 'a';
	dic['z'] = 'q';

	string buf;
	int testCase = 0;
	cin >> testCase;
	getline(cin,buf);

	
	for(int i=0; i<testCase; ++i)
	{
		getline(cin,buf);

		printf("Case #%d: ", i+1);
		for(int s=0; s<buf.size(); ++s)
		{
			if(dic.find(buf[s]) == dic.end())
				printf("%c", buf[s]);
			else
				printf("%c", dic[buf[s]]);
		}
		printf("\n");
	}


	return 0;
}
