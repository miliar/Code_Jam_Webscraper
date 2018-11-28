//The Googlerese problem

#include <iostream>
#include <map>
#include <cstring>

int main(int argc, char const *argv[])
{
	using namespace std;

	int T;
	string G;
	map<char, char> dict;

	scanf("%d", &T);
	getchar();


	dict['y'] = 'a';
	dict['n'] = 'b';
	dict['f'] = 'c';
	dict['i'] = 'd';
	dict['c'] = 'e';
	dict['w'] = 'f';
	dict['l'] = 'g';
	dict['b'] = 'h';
	dict['k'] = 'i';
	dict['u'] = 'j';
	dict['o'] = 'k';
	dict['m'] = 'l';
	dict['x'] = 'm';
	dict['s'] = 'n';
	dict['e'] = 'o';
	dict['v'] = 'p';
	dict['z'] = 'q';
	dict['p'] = 'r';
	dict['d'] = 's';
	dict['r'] = 't';
	dict['j'] = 'u';
	dict['g'] = 'v';
	dict['h'] = 'x';
	dict['a'] = 'y';
	dict['t'] = 'w';
	dict['q'] = 'z';
	dict[' '] = ' ';


	int c;
	int j;
	int len;

	for(int i = 0; i < T; i++){

		getline(cin, G);
		len = G.length();
		for(j = 0; j < len; j++){		
		
			G[j] = dict[G[j]];
		}	

		cout << "Case #" << i+1 << ": " << G << endl;

	}



	return 0;
}