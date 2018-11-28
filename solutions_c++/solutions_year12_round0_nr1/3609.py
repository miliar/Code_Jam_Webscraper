#include <iostream>
#include <fstream>
#define input "A-small-attempt0.in"
#define output "A-small-attempt0.out"
using namespace std;
ifstream in(input);
ofstream out(output);
int N;
char A[1005];
void fill_arr()
{
	A['a']='y';A['b']='h';A['c']='e';
	A['d']='s';A['e']='o';A['f']='c';
	A['g']='v';A['h']='x';A['i']='d';
	A['j']='u';A['k']='i';A['l']='g';
	A['m']='l';A['n']='b';A['o']='k';
	A['p']='r';A['q']='z';A['r']='t';
	A['s']='n';A['t']='w';A['u']='j';
	A['v']='p';A['w']='f';A['x']='m';
	A['y']='a';A['z']='q';A[' ']=' ';
}
int main()
{
	int i,j;
	char c;
	string str;
	fill_arr();
	in >> N;
	getline(in,str);
	for(i=1;i<=N;i++){
		getline(in,str);
		out << "Case #" << i << ": ";
		for(j=0;j<str.size();j++)
			out << A[str[j]];
		out << "\n";
	}
	return 0;
}
