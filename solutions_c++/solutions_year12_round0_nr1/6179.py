#include<fstream.h>

void main()
	{
	int line;
	char ch;
	ifstream inf("ques1.txt");
	ofstream outf("output1.txt");
	inf>> line;
	inf.get(ch);
	for(int i=1; i<=line; i++)
		{
		outf<<"Case #"<<i<<": ";
		inf.get(ch);
		while((ch!='\n')|| (inf.eof()!=0))
		{
		switch(ch)
			{
			case 'a':
				outf.put('y');
				break;
			case 'b':
				outf.put('h');
				break;
			case 'c':
				outf.put('e');
				break;
			case 'd':
				outf.put('s');
				break;
			case 'e':
				outf.put('o');
				break;
			case 'f':
				outf.put('c');
				break;
			case 'g':
				outf.put('v');
				break;
			case 'h':
				outf.put('x');
				break;
			case 'i':
				outf.put('d');
				break;
			case 'j':
				outf.put('u');
				break;
			case 'k':
				outf.put('i');
				break;
			case 'l':
				outf.put('g');
				break;
			case 'm':
				outf.put('l');
				break;
			case 'n':
				outf.put('b');
				break;
			case 'o':
				outf.put('k');
				break;
			case 'p':
				outf.put('r');
				break;
			case 'q':
				outf.put('z');
				break;
			case 'r':
				outf.put('t');
				break;
			case 's':
				outf.put('n');
				break;
			case 't':
				outf.put('w');
				break;
			case 'u':
				outf.put('j');
				break;
			case 'v':
				outf.put('p');
				break;
			case 'w':
				outf.put('f');
				break;
			case 'x':
				outf.put('m');
				break;
			case 'y':
				outf.put('a');
				break;
			case 'z':
				outf.put('q');
				break;
			case ' ' :
				outf.put(' ');
				break;
			default :
				outf.put(ch);
			}
			inf.get(ch);
		 } 					//while
		outf<<"\n";
		}         				//for
		inf.close();
		outf.close();
	}                                                    //main
