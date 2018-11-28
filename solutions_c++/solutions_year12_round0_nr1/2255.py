#include <iostream>
#include <map>
#include <string>
#include <fstream>
using namespace std;

map<char, char> letters;
void initializeLetters(void)
{
	letters['a']='y';
	letters['b']='h';
	letters['c']='e';
	letters['d']='s';
	letters['e']='o';
	letters['f']='c';
	letters['g']='v';
	letters['h']='x';
	letters['i']='d';
	letters['j']='u';
	letters['k']='i';
	letters['l']='g';
	letters['m']='l';
	letters['n']='b';
	letters['o']='k';
	letters['p']='r';
	letters['q']='z';
	letters['r']='t';
	letters['s']='n';
	letters['t']='w';
	letters['u']='j';
	letters['v']='p';
	letters['w']='f';
	letters['x']='m';
	letters['y']='a';
	letters['z']='q';
}

string translate(string googlereseSentence)
{
	string englishSentence="";
	for(unsigned int i=0; i<googlereseSentence.size(); i++)
		englishSentence += letters[googlereseSentence[i]];
	return englishSentence;
}

int main()
{
	initializeLetters();

	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int T=0;
	fin>>T;

	for(int t=1; t<=T; t++)
	{
		string googlereseSentence;
		getline(fin, googlereseSentence);
		fout<<"Case #"<<t<<": "<<translate(googlereseSentence)<<"\n";
	}

	return 0;
}