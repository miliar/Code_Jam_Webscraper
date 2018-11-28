#include <windows.h>
#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <math.h>
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
typedef long s32;
typedef unsigned long u32;

#define MAX_CHARS_IN_CASE 100
#define ESCAPE_CHAR '!'

char GoogleleseToEnglish(char input)
{
	switch(input)
	{
		case 'a' : return 'y';
		case 'b' : return 'h';
		case 'c' : return 'e';
		case 'd' : return 's';
		case 'e' : return 'o';
		case 'f' : return 'c';
		case 'g' : return 'v';
		case 'h' : return 'x';
		case 'i' : return 'd';
		case 'j' : return 'u';
		case 'k' : return 'i';
		case 'l' : return 'g';
		case 'm' : return 'l';
		case 'n' : return 'b';
		case 'o' : return 'k';
		case 'p' : return 'r';
		case 'q' : return 'z';
		case 'r' : return 't';
		case 's' : return 'n';
		case 't' : return 'w';
		case 'u' : return 'j';
		case 'v' : return 'p';
		case 'w' : return 'f';
		case 'x' : return 'm';
		case 'y' : return 'a';
		case 'z' : return 'q';
		default:
			return ' ';
	}
}

int main(int argc, char* argv[])
{

    HANDLE hStdin = GetStdHandle(STD_INPUT_HANDLE); 
    DWORD mode = 0;
    GetConsoleMode(hStdin, &mode);
    SetConsoleMode(hStdin, mode & (~ENABLE_ECHO_INPUT));

	/* reverse engineering like a beaatch */
	/* pass it the googlerese string and then english */

	char char_read = 0;
	char char_out;

	u32 T;

	u32 ii;
	
	/* get case count */
	cin >> T;

	/* skip over first newline*/
	cin.get(char_read);

	for(ii = 0 ; ii < T; ii++)
	{
		cout << "Case #" << ii + 1 << ": ";
		do{
			cin.get(char_read);
			char_out = GoogleleseToEnglish(tolower(char_read));
			if(isupper(char_read))
			{
				cout << toupper(char_out);
			}
			else
			{
				cout << char_out;
			}
		
		}while( char_read != '\n' );

		cout << endl;
	}


}



//int main(int argc, char* argv[])
//{
//
//    HANDLE hStdin = GetStdHandle(STD_INPUT_HANDLE); 
//    DWORD mode = 0;
//    GetConsoleMode(hStdin, &mode);
//    SetConsoleMode(hStdin, mode & (~ENABLE_ECHO_INPUT));
//
//	/* reverse engineering like a beaatch */
//	/* pass it the googlerese string and then english */
//
//	typedef struct{
//		char in;
//		char out;
//	} conversion;
//
//	char input_string[MAX_CHARS_IN_CASE];
//	u32 input_index;
//
//	conversion mapping[26];
//	char char_read = 0;
//
//	u32 map_index;
//
//	u32 ii;
//
//	/* steal z input char from text */
//	mapping['z' - 97].in = 'z';
//	mapping['z' - 97].out = 'q';
//
//	/* steal q from deduction */
//	mapping['q' - 97].in = 'q';
//	mapping['q' - 97].out = 'z';
//
//	while(char_read != ESCAPE_CHAR)
//	{
//		cin.get(char_read);
//
//		input_index = 0;
//		/* first read input googlerese */
//		while((char_read != '\n') && (char_read != ESCAPE_CHAR))
//		{			
//			if(char_read != ' ')
//			{
//				input_string[input_index++] = char_read;
//			}
//			cin.get(char_read);
//
//		}
//
//		if(char_read != ESCAPE_CHAR)
//			cin.get(char_read);
//
//		input_index = 0;
//		/* now read english */
//		while((char_read != '\n') && (char_read != ESCAPE_CHAR))
//		{
//			if(char_read != ' ')
//			{
//				map_index = input_string[input_index] - 97;
//				mapping[map_index].in = input_string[input_index++];
//				mapping[map_index].out = char_read;
//			}
//			cin.get(char_read);
//
//		}
//
//		/*rinse repeat until escape char is pressed*/
//
//	}
//
//	for(ii = 0; ii < 26; ii++)
//	{
//		cout << "case '" << mapping[ii].in <<"' : return '" << mapping[ii].out <<"';" << endl;
//	}
//
//}
