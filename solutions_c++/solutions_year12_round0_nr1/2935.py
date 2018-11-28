#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T;
	char **ch;
	char temp[2];

	ch = new char*[30];
	
	for (int i=0; i<30; i++)
	{
		ch[i] = new char[101];
		for (int j=0; j<101; j++)
		{
			ch[i][j]='\0';
		}
	}

	ifstream fin ("A-small-attempt4.IN");

	fin >> T;
	fin.getline(temp, 2);

	for (int i=0; i<T; i++)
		fin.getline(ch[i], 101);

	ofstream fout ("A.txt");

	for (int j=0; j<T; j++)
	{
		fout << "Case #";
		fout << j+1;
		fout << ": " ;

		for (int i=0; i<100; i++)
		{
			switch (ch[j][i])
			{
			case 'a':	fout << 'y';	break;
			case 'b':	fout << 'h';	break;
			case 'c':	fout << 'e';	break;
			case 'd':	fout << 's';	break;
			case 'e':	fout << 'o';	break;
			case 'f':	fout << 'c';	break;
			case 'g':	fout << 'v';	break;
			case 'h':	fout << 'x';	break;
			case 'i':	fout << 'd';	break;
			case 'j':	fout << 'u';	break;
			case 'k':	fout << 'i';	break;
			case 'l':	fout << 'g';	break;
			case 'm':	fout << 'l';	break;
			case 'n':	fout << 'b';	break;
			case 'o':	fout << 'k';	break;
			case 'p':	fout << 'r';	break;
			case 'q':	fout << 'z';	break;
			case 'r':	fout << 't';	break;
			case 's':	fout << 'n';	break;
			case 't':	fout << 'w';	break;
			case 'u':	fout << 'j';	break;
			case 'v':	fout << 'p';	break;
			case 'w':	fout << 'f';	break;
			case 'x':	fout << 'm';	break;
			case 'y':	fout << 'a';	break;
			case 'z':	fout << 'q';	break;
			case ' ':	fout << ' ';	break;
			}
		}

		fout << endl;
	}

	for (int i=0; i<30; i++)
	{
		delete [] ch [i];
	}

	delete [] ch;
	return 0;
}