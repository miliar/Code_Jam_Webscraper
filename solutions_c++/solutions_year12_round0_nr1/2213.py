#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int T;
bool u[26];
map<char, char> M;

string A[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string B[3] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};

int main()
{
	M['e']='o';
	M['j']='u';
	M['p']='r';
	M['m']='l';
	M['y']='a';
	M['s']='n';
	M['l']='g';
	M['c']='e';
	M['k']='i';
	M['d']='s';
	M['x']='m';
	M['v']='p';
	M['n']='b';
	M['r']='t';
	M['i']='d';
	M['b']='h';
	M['t']='w';
	M['a']='y';
	M['h']='x';
	M['w']='f';
	M['f']='c';
	M['o']='k';
	M['u']='j';
	M['g']='v';
	M['q']='z';
	M['z']='q';
	
	//freopen("a-small.txt", "r", stdin);
	
	cin >> T;
	string s;
	getline(cin, s);
	for (int test = 0; test < T; test++)
	{
		getline(cin, s);
		//cout << s << endl;
		printf("Case #%d: ", test + 1);
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == ' ') printf(" ");
			else printf("%c", M[s[i]]);
		}
		printf("\n");
	}
	/*int c = 0;
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < A[i].size(); j++)
		{
			if (A[i][j] == ' ') continue;
			if (u[A[i][j] - 'a']) continue;
			u[A[i][j] - 'a'] = true;
			//cout << A[i][j] << "->" << B[i][j] << endl;
			
			printf("M['%c']='%c';\n", A[i][j], B[i][j]);
			c++;
		}
	}
	cout << c << endl;
	
	for (int i = 0; i < 26; i++)
	{
		if (!u[i]) cout << "unused: " << char(i + 'a') << endl;
	}
	*/
	return 0;
}
