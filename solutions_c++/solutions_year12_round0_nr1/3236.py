#include<iostream.h>
#include<fstream.h>
#include<string.h>
#include<stdio.h>
void convert(char *x)
{
	switch(*x)
	{       case 'a': *x= 'y';
			  break;

		case 'b': *x= 'h';
			  break;

		case 'c': *x= 'e';
			  break;

		case 'd': *x= 's';
			  break;

		case 'e': *x= 'o';
			  break;

		case 'f': *x= 'c';
			  break;

		case 'g': *x= 'v';
			  break;

		case 'h': *x= 'x';
			  break;

		case 'i': *x= 'd';
			  break;

		case 'j': *x= 'u';
			  break;

		case 'k': *x= 'i';
			  break;

		case 'l': *x= 'g';
			  break;

		case 'm': *x= 'l';
			  break;

		case 'n': *x= 'b';
			  break;

		case 'o': *x= 'k';
			  break;

		case 'p': *x= 'r';
			  break;

		case 'q': *x= 'z';
			  break;

		case 'r': *x= 't'   ;
			  break;

		case 's': *x= 'n'  ;
			  break;

		case 't': *x= 'w' ;
			  break;

		case 'u': *x= 'j';
			  break;

		case 'v': *x= 'p' ;
			  break;

		case 'w': *x= 'f';
			  break;

		case 'x': *x= 'm';
			  break;

		case 'y': *x= 'a';
			  break;

		case 'z': *x= 'q';
			  break;
	}

}

void main()
{
	ifstream ifile("F-small.txt");
	ofstream ofile("fsout.txt");
	char line[102];
	int te;
	ifile>>te;
	int j=1;
	while(!ifile.eof())
	{
		ifile.getline(line,102);
		for(int i=0;i<strlen(line); i++)
		{
			convert(&line[i]);
		}
		if((j!=1)&&(j!=32))
			ofile<<"Case #"<<j-1<<": "<<line<<"\n";
		j++;
	}
	ifile.close();
	ofile.close();
}
