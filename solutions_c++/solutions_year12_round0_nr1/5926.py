#include <fstream>
#include <string>
#include <map>

using namespace std;

int main()
{
	int T,i,j;
	string s;
	ifstream f("A-small-attempt1.in");
	ofstream g("out.txt");
	map<char,char> M;
	M['y']='a';
	M['n']='b';
	M['f']='c';
	M['i']='d';
	M['c']='e';
	M['w']='f';
	M['l']='g';
	M['b']='h';
	M['k']='i';
	M['u']='j';
	M['o']='k';
	M['m']='l';
	M['x']='m';
	M['s']='n';
	M['e']='o';
	M['v']='p';
	M['z']='q';
	M['p']='r';
	M['d']='s';
	M['r']='t';
	M['j']='u';
	M['g']='v';
	M['t']='w';
	M['h']='x';
	M['a']='y';
	M['q']='z';

	f>>T;
	getline(f,s);

	for(i=1;i<=T;i++)
	{
		g<<"Case #"<<i<<": ";
		getline(f,s);
		for(j=0;j<s.length();j++)
		{
			if(s[j]==' ')
				g<<" ";
			else
			{
			g<<M[s[j]];
			}
		}
		g<<"\n";
	}

	f.close();
	g.close();
	return 0;
}