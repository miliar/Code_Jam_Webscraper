#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main()
{
	int T,N,K;
	map<char, char> dict;

	dict['e']='o';
	dict['j']='u';
	dict['p']='r';

	dict['m']='l';
	dict['y']='a';
	dict['s']='n';
	dict['l']='g';
	dict['j']='u';
	dict['y']='a';
	dict['l']='g';
	dict['c']='e';

	dict['k']='i';
	dict['d']='s';

	dict['k']='i';
	dict['x']='m';
	dict['v']='p';
	dict['e']='o';
	dict['d']='s';
	dict['d']='s';
	dict['k']='i';
	dict['n']='b';
	dict['m']='l';
	dict['c']='e';

	dict['r']='t';
	dict['e']='o';

	dict['j']='u';
	dict['s']='n';
	dict['i']='d';
	dict['c']='e';
	dict['p']='r';
	dict['d']='s';
	dict['r']='t';
	dict['y']='a';
	dict['s']='n';
	dict['i']='d';

	dict['r']='t';
	dict['b']='h';
	dict['c']='e';
	dict['p']='r';
	dict['c']='e';

	dict['y']='a';
	dict['p']='r';
	dict['c']='e';

	dict['r']='t';
	dict['t']='w';
	dict['c']='e';
	dict['s']='n';
	dict['r']='t';
	dict['a']='y';

	dict['d']='s';
	dict['k']='i';
	dict['h']='x';

	dict['w']='f';
	dict['y']='a';
	dict['f']='c';
	dict['r']='t';
	dict['e']='o';
	dict['p']='r';
	dict['k']='i';
	dict['y']='a';
	dict['m']='l';

	dict['v']='p';
	dict['e']='o';
	dict['d']='s';
	dict['d']='s';
	dict['k']='i';
	dict['n']='b';
	dict['k']='i';
	dict['m']='l';
	dict['k']='i';
	dict['r']='t';
	dict['k']='i';
	dict['c']='e';
	dict['d']='s';

	dict['d']='s';
	dict['e']='o';

	dict['k']='i';
	dict['r']='t';

	dict['k']='i';
	dict['d']='s';

	dict['e']='o';
	dict['o']='k';
	dict['y']='a';
	dict['a']='y';

	dict['k']='i';
	dict['w']='f';

	dict['a']='y';
	dict['e']='o';
	dict['j']='u';

	dict['t']='w';
	dict['y']='a';
	dict['s']='n';
	dict['r']='t';

	dict['r']='t';
	dict['e']='o';

	dict['u']='j';
	dict['j']='u';
	dict['d']='s';
	dict['r']='t';

	dict['l']='g';
	dict['k']='i';
	dict['g']='v';
	dict['c']='e';

	dict['j']='u';
	dict['v']='p';



	dict['y']='a';
	dict['e']='o';
	dict['q']='z';
	dict[' ']=' ';


// Z DOES NOT APPEARS!
   dict['z']='q';

	char c;
	string row;
	string result;
	cin >> T;
	getline (cin,row);

	for (int i=0;i<T;i++)
	{
		result = "";
	   
		getline (cin,row);
	   for (int j=0;j<row.length();j++){
		c = row[j];
		result += (char)dict[c];
		}	

	   cout << "Case #" << i+1 << ": " << result <<endl;
	}
	return 0;
}
