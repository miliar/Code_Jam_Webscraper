#include <iostream>
#include <string>

using namespace std;

char map[256] = {0};

int main()
{
	map['j']='u';
	map['p']='r';
	map['m']='l';
	map['y']='a';
	map['s']='n';
	map['l']='g';
	map['c']='e';
	map['k']='i';
	map['d']='s';
	map['x']='m';
	map['v']='p';
	map['n']='b';
	map['r']='t';
	map['i']='d';
	map['b']='h';
	map['t']='w';
	map['a']='y';
	map['h']='x';
	map['w']='f';
	map['f']='c';
	map['o']='k';
	map['u']='j';
	map['g']='v';
	map['e']='o';
	map['q']='z';
	map['z']='q';

	map['J']='U';
	map['P']='R';
	map['M']='L';
	map['Y']='A';
	map['S']='N';
	map['L']='G';
	map['C']='E';
	map['K']='I';
	map['D']='S';
	map['X']='M';
	map['V']='P';
	map['N']='B';
	map['R']='T';
	map['I']='D';
	map['B']='H';
	map['T']='W';
	map['A']='Y';
	map['H']='X';
	map['W']='F';
	map['F']='C';
	map['O']='K';
	map['U']='J';
	map['G']='V';
	map['E']='O';
	map['Q']='Z';
	map['Z']='Q';
	
	map[' ']=' ';


	int i,n;
	cin>>n;
	cin.ignore();
	for (i=0; i<n; i++)
	{
		string s;
		int j;
		getline(cin,s);

		cout<<"Case #"<<i+1<<": ";

		for(j=0; j<(signed)s.length(); j++)
		{
			cout<<map[(int)s[j]];
		}

		cout<<endl;

	}

	return 0;
}
