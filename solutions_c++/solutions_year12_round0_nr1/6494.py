#include<iostream>
#include<fstream>
#include<cstring>
#include<cstdio>
using namespace std;


int main()
{
	int T,i,j,p,nsz;
	string G;
	string S(100,' ');
	char s[100];
	char ch;
	ofstream opfile("outfile.txt");
	ifstream infile;
	infile.open("A-small-attempt1.in",ios::in);
	infile>>T;	
	for(ch=infile.peek(),i=1;ch!='\n';i++);
	infile.ignore(i);
	for(i=0;i<T;++i)
	{
		getline(infile,G);
		for(j=0;j<G.length();++j)
		{
			switch(G.at(j))
			{
				case 'a': S.at(j)='y';break;
				case 'b': S.at(j)='h';break;
				case 'c': S.at(j)='e';break;
				case 'd': S.at(j)='s';break;
				case 'e': S.at(j)='o';break;
				case 'f': S.at(j)='c';break;
				case 'g': S.at(j)='v';break;
				case 'h': S.at(j)='x';break;
				case 'i': S.at(j)='d';break;
				case 'j': S.at(j)='u';break;
				case 'k': S.at(j)='i';break;
				case 'l': S.at(j)='g';break;
				case 'm': S.at(j)='l';break;
				case 'n': S.at(j)='b';break;
				case 'o': S.at(j)='k';break;
				case 'p': S.at(j)='r';break;
				case 'q': S.at(j)='z';break;
				case 'r': S.at(j)='t';break;
				case 's': S.at(j)='n';break;
				case 't': S.at(j)='w';break;
				case 'u': S.at(j)='j';break;
				case 'v': S.at(j)='p';break;
				case 'w': S.at(j)='f';break;
				case 'x': S.at(j)='m';break;
				case 'y': S.at(j)='a';break;
				case 'z': S.at(j)='q';break;
				default: S.at(j)=G.at(j);
			}
		}
	G=" ";
	nsz=S.length();
	for(j=0;j<nsz;++j)
		s[j]=S.at(j);
	
	opfile<<"Case #"<<i+1<<": ";
	opfile.write(s,nsz);
	opfile<<endl;
	for(j=0;j<nsz;++j)
	{	s[j]=' ';S.at(j)=' ';}
	
	}
	infile.close();
	opfile.close();
return 0;
}	
