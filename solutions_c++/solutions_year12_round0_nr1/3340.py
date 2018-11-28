// Googelerese -- translate characters

#include <iostream>

int main(){
	int num_cases, counter = 0, pos = 0;
	char output[150];
	char ch;

	std::cin >> num_cases;
	std::cin.get( ch );

	while ( counter < num_cases ){
		pos = 0;

		std::cin.get( ch );
		while ( ch != '\n' ){//watch here for potential issue
			switch ( ch ) {
				case 'a':
					ch = 'y';
					break;
				case 'b':
					ch = 'h';
					break;
				case 'c':
					ch = 'e';
					break;
				case 'd':
					ch = 's';
					break;
				case 'e':
					ch = 'o';
					break;
				case 'f':
					ch = 'c';
					break;
				case 'g':
					ch = 'v';
					break;
				case 'h':
					ch = 'x';
					break;
				case 'i':
					ch = 'd';
					break;
				case 'j':
					ch = 'u';
					break;
				case 'k':
					ch = 'i';
					break;
				case 'l':
					ch = 'g';
					break;
				case 'm':
					ch = 'l';
					break;
				case 'n':
					ch = 'b';
					break;
				case 'o':
					ch = 'k';
					break;
				case 'p':
					ch = 'r';
					break;
				case 'q':
					ch = 'z';
					break;
				case 'r':
					ch = 't';
					break;
				case 's':
					ch = 'n';
					break;
				case 't':
					ch = 'w';
					break;
				case 'u':
					ch = 'j';
					break;
				case 'v':
					ch = 'p';
					break;
				case 'w':
					ch = 'f';
					break;
				case 'x':
					ch = 'm';
					break;
				case 'y':
					ch = 'a';
					break;
				case 'z':
					ch = 'q';
					break;
				case ' ':
					ch = ' ';
					break;
			}


			output[pos] = ch;
			pos++;
			std::cin.get( ch );

		}

		int counter_2 = 0;


		std::cout << "Case #" << counter + 1 <<": ";

		while ( counter_2 < pos ){
			std::cout << output[counter_2];
			counter_2++;
		}

		counter++;
		std::cout << std::endl;
	}

	return 0;
}
