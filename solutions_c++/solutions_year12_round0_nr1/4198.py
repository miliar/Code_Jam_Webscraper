#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream f("read.txt");
	ofstream g("output.txt");
	char 	s[110],result[110],ch;
	int	t,i,j;
	f>>t;
	f.getline(s,101,'\n');
	for(j=0;j<t;j++)
	{	
		f.getline(s,101,'\n');
		cout<<"s:"<<s<<"\n";
		for(i=0;s[i]!='\0';i++)
		{
			switch(s[i])
			{
				case 'a':result[i]='y';break;
				case 'b':result[i]='h';break;
				case 'c':result[i]='e';break;
				case 'd':result[i]='s';break;
				case 'e':result[i]='o';break;
				case 'f':result[i]='c';break;
				case 'g':result[i]='v';break;
				case 'h':result[i]='x';break;
				case 'i':result[i]='d';break;
				case 'j':result[i]='u';break;
				case 'k':result[i]='i';break;
				case 'l':result[i]='g';break;
				case 'm':result[i]='l';break;
				case 'n':result[i]='b';break;
				case 'o':result[i]='k';break;
				case 'p':result[i]='r';break;
				case 'q':result[i]='z';break;
				case 'r':result[i]='t';break;
				case 's':result[i]='n';break;
				case 't':result[i]='w';break;
				case 'u':result[i]='j';break;
				case 'v':result[i]='p';break;
				case 'w':result[i]='f';break;
				case 'x':result[i]='m';break;
				case 'y':result[i]='a';break;
				case 'z':result[i]='q';break;
				case ' ':result[i]=' ';break;
				case 'A':result[i]='Y';break;
				case 'B':result[i]='H';break;
				case 'C':result[i]='E';break;
				case 'D':result[i]='S';break;
				case 'E':result[i]='O';break;
				case 'F':result[i]='C';break;
				case 'G':result[i]='V';break;
				case 'H':result[i]='X';break;
				case 'I':result[i]='D';break;
				case 'J':result[i]='U';break;
				case 'K':result[i]='I';break;
				case 'L':result[i]='G';break;
				case 'M':result[i]='L';break;
				case 'N':result[i]='B';break;
				case 'O':result[i]='K';break;
				case 'P':result[i]='R';break;
				case 'Q':result[i]='Z';break;
				case 'R':result[i]='T';break;
				case 'S':result[i]='N';break;
				case 'T':result[i]='W';break;
				case 'U':result[i]='J';break;
				case 'V':result[i]='P';break;
				case 'W':result[i]='F';break;
				case 'X':result[i]='M';break;
				case 'Y':result[i]='A';break;
				case 'Z':result[i]='Q';break;
			}
		}
		result[i]='\0';
		cout<<result<<"\n";
		g<<"Case #"<<j+1<<": "<<result<<'\n';
	}
	return 0;
}
