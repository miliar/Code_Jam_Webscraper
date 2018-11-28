#include <iostream>
using namespace std;

void main()
{
	FILE* Input = fopen("in.in","r");
	FILE* Output = fopen("out.txt","w+");

	int T = 0;
	char buf[150];

	fscanf(Input,"%d\n",&T);

	for(int i=0; i<T; i++)
	{
		fgets(buf,150,Input);

		for(int j=0; j<150; j++)
		{
			switch(buf[j])
			{
			case 'a':
				buf[j] = 'y';
				break;
			case 'b':
				buf[j] = 'h';
				break;
			case 'c':
				buf[j] = 'e';
				break;
			case 'd':
				buf[j] = 's';
				break;
			case 'e':
				buf[j] = 'o';
				break;
			case 'f':
				buf[j] = 'c';
				break;
			case 'g':
				buf[j] = 'v';
				break;
			case 'h':
				buf[j] = 'x';
				break;
			case 'i':
				buf[j] = 'd';
				break;
			case 'j':
				buf[j] = 'u';
				break;
			case 'k':
				buf[j] = 'i';
				break;
			case 'l':
				buf[j] = 'g';
				break;
			case 'm':
				buf[j] = 'l';
				break;
			case 'n':
				buf[j] = 'b';
				break;
			case 'o':
				buf[j] = 'k';
				break;
			case 'p':
				buf[j] = 'r';
				break;
			case 'q':
				buf[j] = 'z';
				break;
			case 'r':
				buf[j] = 't';
				break;
			case 's':
				buf[j] = 'n';
				break;
			case 't':
				buf[j] = 'w';
				break;
			case 'u':
				buf[j] = 'j';
				break;
			case 'v':
				buf[j] = 'p';
				break;
			case 'w':
				buf[j] = 'f';
				break;
			case 'x':
				buf[j] = 'm';
				break;
			case 'y':
				buf[j] = 'a';
				break;
			case 'z':
				buf[j] = 'q';
				break;
			}
		}

		fprintf(Output,"Case #%d: %s",i+1,buf);
	}
}