#include <iostream>
#include <map>
#include <string>
#include <fstream>

using namespace std;

void init(map <char,char> & ch){
	ch['a'] = 'y';
	ch['b'] = 'h';
	ch['c'] = 'e';
	ch['d'] = 's';
	ch['e'] = 'o';
	ch['f'] = 'c';
	ch['g'] = 'v';
	ch['h'] = 'x';
	ch['i'] = 'd';
	ch['j'] = 'u';
	ch['k'] = 'i';
	ch['l'] = 'g';
	ch['m'] = 'l';
	ch['n'] = 'b';
	ch['o'] = 'k';
	ch['p'] = 'r';
	ch['q'] = 'z';
	ch['r'] = 't';
	ch['s'] = 'n';
	ch['t'] = 'w';
	ch['u'] = 'j';
	ch['v'] = 'p';
	ch['w'] = 'f';
	ch['x'] = 'm';
	ch['y'] = 'a';
	ch['z'] = 'q';
	ch[' '] = ' ';
}

int main(){

	string *line,enter;
	int T,i = 0;
	map <char,char> ch;
	ifstream Fin;
	ofstream Fout;

	init(ch);

	Fin.open("A-small-attempt1.in");

	if(Fin.fail())
		exit(0);

	Fin>>T;
	
	Fout.open("answer.txt");
	line = new string[T + 1];
	while(i <= T){
		getline(Fin,line[i]);
		i++;
	}

	Fin.close();

	for(i = 1;i <= T;i++){
		for(int j = 0;j < line[i].size();j++)
			line[i][j] = ch[line[i][j]];
		Fout<<"Case #"<<i<<": "<<line[i]<<endl;
	}

	Fout.close();

	return 0;

}