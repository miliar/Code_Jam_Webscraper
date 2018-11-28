//google code jam question 1
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main(){
	map<char,char> table;
	table['a']='y';table['b']='h';table['c']='e';table['d']='s';table['e']='o';
	table['f']='c';table['g']='v';table['h']='x';table['i']='d';table['j']='u';
	table['k']='i';table['l']='g';table['m']='l';table['n']='b';table['o']='k';
	table['p']='r';table['q']='z';table['r']='t';table['s']='n';table['t']='w';
	table['u']='j';table['v']='p';table['w']='f';table['x']='m';table['y']='a';
	table['z']='q';
	
	ifstream input("A-small-attempt0.in");
	ofstream output("out.txt");

	int n;
	input >> n;
	string g;
	getline(input,g);
	for (unsigned int i=0;i<n;i++){
		getline(input,g);
		for (unsigned int j=0;j<g.length();j++){
			if (g[j]!=' '){
				g[j]=table[g[j]];
			}
		}
		output << "Case #" << i+1 << ": " << g << endl;
	}
	
	return 0;
}
