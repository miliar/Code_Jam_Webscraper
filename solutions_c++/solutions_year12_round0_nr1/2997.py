#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstring>
#include <map>

using namespace std;

map<char, char> google;

void initmap()
{
	google[' '] = ' ';
	google['a'] = 'y';
	google['b'] = 'h';
	google['c'] = 'e';
	google['d'] = 's';
	google['e'] = 'o';
	google['f'] = 'c';
	google['g'] = 'v';
	google['h'] = 'x';
	google['i'] = 'd';
	google['j'] = 'u';
	google['k'] = 'i';
	google['l'] = 'g';
	google['m'] = 'l';
	google['n'] = 'b';
	google['o'] = 'k';
	google['p'] = 'r';
	google['q'] = 'z';
	google['r'] = 't';
	google['s'] = 'n';
	google['t'] = 'w';
	google['u'] = 'j';
	google['v'] = 'p';
	google['w'] = 'f';
	google['x'] = 'm';
	google['y'] = 'a';
	google['z'] = 'q';
}

int main()
{
    initmap();
	int t, cnt;
	char str[110];
	freopen("A-small-attempt4.in","r",stdin);
	freopen("A-small-attempt4.out","w",stdout);
    cin >> t;
	getchar();
	cnt = 1;
	while(t--)
	{
		cin.getline(str, 110);
		
		cout << "Case #" << cnt++ << ": ";
	//	printf("Case #%d: ", cnt++);

		for(int i = 0; i < strlen(str); i++)
		{
		//	printf("%c", google[str[i]]);
			cout << google[str[i]];
		}
		//printf("\n");
		cout << endl;
	}

	return 0;
}



