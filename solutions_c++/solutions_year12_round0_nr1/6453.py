#include <fstream>
#include <vector>
using namespace std;
int main()
{
	ifstream in( "A-small-attempt1.in");
	ofstream out( "output.txt");
	int n;
	char c;
	FILE *input = fopen("A-small-attempt1.in", "r");
	fscanf(input, "%d\n", &n);
	for (int i=1;i<=n;++i)
	{
		out<< "Case #"<< i<<": " ;
		while (c!='\n')
		{
			fscanf(input, "%c", &c);
			if (in.eof()) return 0;
			if (c=='y') out << 'a';
			if (c=='e') out << 'o';
			if (c=='q') out << 'z';
			if (c=='j') out << 'u';
			if (c=='p') out << 'r';
			if (c=='m') out << 'l';
			if (c=='s') out << 'n';
			if (c=='l') out << 'g';
			if (c=='k') out << 'i';
			if (c=='d') out << 's';
			if (c=='v') out << 'p';
			if (c=='a') out << 'y';
			if (c=='b') out << 'h';
			if (c=='c') out << 'e';
			if (c=='f') out << 'c';
			if (c=='g') out << 'v';
			if (c=='h') out << 'x';
			if (c=='i') out << 'd';
			if (c=='n') out << 'b';
			if (c=='o') out << 'k';
			if (c=='r') out << 't';
			if (c=='t') out << 'w';
			if (c=='w') out << 'f';
			if (c=='u') out << 'j';
			if (c=='z') out << 'q';
			if (c=='x') out << 'm';
			if (c==' ') out << ' ';
		}
		
		out<<"\n" ;
		c=' ';
	}
	
	return 0;
}
