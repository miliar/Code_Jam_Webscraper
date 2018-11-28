#include <iostream>
#include <fstream>
#include <string>
 
#include <windows.h>
using namespace std;

int main()
{
	long start = GetTickCount();
	ifstream input("A-small-attempt1.in",ios::in);
	if(!input)
	{
		cerr<<"Cannot read target file"<<endl;
		exit(1);
	}

	ofstream output("A-small-attempt1.out",ios::trunc);//out
	if(!output)
	{
		cerr<<"Cannot open output file"<<endl;
		exit(1);
	}
	int lines ;
	input>>lines;
	
	int i =0;
	string str = "";
	for (i=0;i<lines;i++)
	{
		//Spell(i,line,input,output);
		string out = "Case #";
		
		char ch[256];
		sprintf(ch,"%d",i+1);
		out = out + ch + ": ";
		getline(input,str);
		if(0 == i)
			getline(input,str);
		for (string::size_type ix = 0; ix != str.size(); ++ix)
		{
			switch(str[ix])
			{
			case 'a':
				str[ix] = 'y';
				break;
			case 'b':
				str[ix] = 'h';
				break;
			case 'c':
				str[ix] = 'e';
				break;
			case 'd':
				str[ix] = 's';
				break;
			case 'e':
				str[ix] = 'o';
				break;
			case 'f':
				str[ix] = 'c';
				break;
			case 'g':
				str[ix] = 'v';
				break;
			case 'h':
				str[ix] = 'x';
				break;
			case 'i':
				str[ix] = 'd';
				break;
			case 'j':
				str[ix] = 'u';
				break;
			case 'k':
				str[ix] = 'i';
				break;
			case 'l':
				str[ix] = 'g';
				break;
			case 'm':
				str[ix] = 'l';
				break;
			case 'n':
				str[ix] = 'b';
				break;
			case 'o':
				str[ix] = 'k';
				break;
			case 'p':
				str[ix] = 'r';
				break;
			case 'q':
				str[ix] = 'z';
				break;
			case 'r':
				str[ix] = 't';
				break;
			case 's':
				str[ix] = 'n';
				break;
			case 't':
				str[ix] = 'w';
				break;
			case 'u':
				str[ix] = 'j';
				break;
			case 'v':
				str[ix] = 'p';
				break;
			case 'w':
				str[ix] = 'f';
				break;
			case 'x':
				str[ix] = 'm';
				break;
			case 'y':
				str[ix] = 'a';
				break;
			case 'z':
				str[ix] = 'q';
				break;
			case ' ':
				str[ix] = ' ';
				break;
			default:
				//str[ix] = ' ';
				;
			}
		}
		out = out + str + "\n";
		output<<out;
	}

	input.close();
	output.close();
	long end = GetTickCount();
	cout<<"Time : "<<end - start<<" ms"<<endl;
	system("pause");
	return 0;
}



