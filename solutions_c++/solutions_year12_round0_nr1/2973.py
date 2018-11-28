#include <fstream>
#include <iostream>

using namespace std;

char replace (char a)	{
	switch (a)	{
	case 'y':return 'a';	break;
	case 'n':return 'b';	break;
	case 'f':return 'c';	break;
	case 'i':return 'd';	break;
	case 'c':return 'e';	break;
	case 'w':return 'f';	break;
	case 'l':return 'g';	break;
	case 'b':return 'h';	break;
	case 'k':return 'i';	break;
	case 'u':return 'j';	break;
	case 'o':return 'k';	break;
	case 'm':return 'l';	break;
	case 'x':return 'm';	break;
	case 's':return 'n';	break;
	case 'e':return 'o';	break;
	case 'v':return 'p';	break;
	case 'z':return 'q';	break;
	case 'p':return 'r';	break;
	case 'd':return 's';	break;
	case 'r':return 't';	break;
	case 'j':return 'u';	break;
	case 'g':return 'v';	break;
	case 't':return 'w';	break;
	case 'h':return 'x';	break;
	case 'a':return 'y';	break;
	case 'q':return 'z';	break;
	default:return a;
	}
}

int main()	{
	ifstream fin("A-small-attempt2.in");
	ofstream fout("a-small.txt", ios::ate);
	int t, count;
	fin >> t;
	char a;

	for (count=1; count <= t; count++)	{
		fout<<"Case #"<<count<<": "; 
		a=fin.get();
		while (a<'a' || a>'z'){
			a=fin.get();
		}
		while(1)	{
			if (a>='a' && a<='z')	{
				a=replace (a);
				fout << a;
			}
			else if (a==' ') fout << a;
			else break;
			a=fin.get();
		}
		fout << '\n';
	}
	return 0;
}