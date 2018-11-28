#include<cstdio>

using namespace std;

void ConvertToEnglish(char ArgumentString[])
{	for(unsigned int Ind = 0; ArgumentString[Ind] != '\0'; ++Ind)
		switch(ArgumentString[Ind])
		{	case ' ':	ArgumentString[Ind] = ' ';	break;
			case 'y':	ArgumentString[Ind] = 'a';	break;
			case 'n':	ArgumentString[Ind] = 'b';	break;
			case 'f':	ArgumentString[Ind] = 'c';	break;
			case 'i':	ArgumentString[Ind] = 'd';	break;
			case 'c':	ArgumentString[Ind] = 'e';	break;
			case 'w':	ArgumentString[Ind] = 'f';	break;
			case 'l':	ArgumentString[Ind] = 'g';	break;
			case 'b':	ArgumentString[Ind] = 'h';	break;
			case 'k':	ArgumentString[Ind] = 'i';	break;
			case 'u':	ArgumentString[Ind] = 'j';	break;
			case 'o':	ArgumentString[Ind] = 'k';	break;
			case 'm':	ArgumentString[Ind] = 'l';	break;
			case 'x':	ArgumentString[Ind] = 'm';	break;
			case 's':	ArgumentString[Ind] = 'n';	break;
			case 'e':	ArgumentString[Ind] = 'o';	break;
			case 'v':	ArgumentString[Ind] = 'p';	break;
			case 'z':	ArgumentString[Ind] = 'q';	break;
			case 'p':	ArgumentString[Ind] = 'r';	break;
			case 'd':	ArgumentString[Ind] = 's';	break;
			case 'r':	ArgumentString[Ind] = 't';	break;
			case 'j':	ArgumentString[Ind] = 'u';	break;
			case 'g':	ArgumentString[Ind] = 'v';	break;
			case 't':	ArgumentString[Ind] = 'w';	break;
			case 'h':	ArgumentString[Ind] = 'x';	break;
			case 'a':	ArgumentString[Ind] = 'y';	break;
			case 'q':	ArgumentString[Ind] = 'z';	break;
			default :	ArgumentString[Ind] = ArgumentString[Ind];
		}
}
int main()
{	unsigned int NumberOfTests;
	char TestCase[210];
	
	scanf("%u",&NumberOfTests);
	getchar();
	
	for(unsigned int Ind = 0; Ind < NumberOfTests; ++Ind)
	{	gets(TestCase);
		ConvertToEnglish(TestCase);
		printf("Case #%u: ",Ind+1);
		puts(TestCase);
	}
	return 0;
}