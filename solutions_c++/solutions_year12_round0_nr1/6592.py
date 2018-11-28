

#include <iostream>
#include <fstream>

using namespace std;
char languageTranslate(char c);

int main()
{
const int max = 1000;
char buffer[max];
int T;
ifstream infile("\\A-small-attempt0.in");
ofstream outfile("\\output.txt");
infile >> T;
for(int i =0 ; i<=T;i++)
{
	//infile.getline(buffer,max);
	infile.getline(buffer,max);
	for(int j=0;j<max;j++)
	{
		buffer[j]=languageTranslate(buffer[j]);
	}
	if(i>0)
	outfile<<"Case #"<<i<<": " <<buffer<<endl;
}
//cin.ignore();
return 0;
}

char languageTranslate(char c)
{
switch(c)
{
case 'a':
	return 'y';
case 'b':
	return 'h';
case 'c':
	return 'e';
case 'd':
	return 's';
case 'e':
	return 'o';
case 'f':
	return 'c';
case 'g':
	return 'v';
case 'h':
	return 'x';
case 'i':
	return 'd';
case 'j':
	return 'u';
case 'k':
	return 'i';
case 'l':
	return 'g';
case 'm':
	return 'l';
case 'n':
	return 'b';
case 'o':
	return 'k';
case 'p':
	return 'r';
case 'q':
	return 'z';
case 'r':
	return 't';
case 's':
	return 'n';
case 't':
	return 'w';
case 'u':
	return 'j';
case 'v':
	return 'p';
case 'w':
	return 'f';
case 'x':
	return 'm';
case 'y':
	return 'a';
case 'z':
	return 'q';
default:
	return c;

}

return c;
}
