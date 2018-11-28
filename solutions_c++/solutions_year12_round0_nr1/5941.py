#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	char strInput[110];
	char strTotalCase[5];
	int intTotalCase;
	int currentCase;
	int intStringLength;

	int i;

	gets(strTotalCase);
	intTotalCase = atoi(strTotalCase);

	for(currentCase = 1; currentCase <= intTotalCase; currentCase++){
		gets(strInput);
		printf("Case #%d: ", currentCase);

		for(i = 0; strInput[i] != '\0'; i++){
			switch(strInput[i]){
				case 'a':
					putchar('y');
					break;
				case 'b':
					putchar('h');
					break;
				case 'c':
					putchar('e');
					break;
				case 'd':
					putchar('s');
					break;
				case 'e':
					putchar('o');
					break;
				case 'f':
					putchar('c');
					break;
				case 'g':
					putchar('v');
					break;
				case 'h':
					putchar('x');
					break;
				case 'i':
					putchar('d');
					break;
				case 'j':
					putchar('u');
					break;
				case 'k':
					putchar('i');
					break;
				case 'l':
					putchar('g');
					break;
				case 'm':
					putchar('l');
					break;
				case 'n':
					putchar('b');
					break;
				case 'o':
					putchar('k');
					break;
				case 'p':
					putchar('r');
					break;
				case 'q':
					putchar('z');
					break;
				case 'r':
					putchar('t');
					break;
				case 's':
					putchar('n');
					break;
				case 't':
					putchar('w');
					break;
				case 'u':
					putchar('j');
					break;
				case 'v':
					putchar('p');
					break;
				case 'w':
					putchar('f');
					break;
				case 'x':
					putchar('m');
					break;
				case 'y':
					putchar('a');
					break;
				case 'z':
					putchar('q');
					break;
				case 'A':
					putchar('Y');
					break;
				case 'B':
					putchar('H');
					break;
				case 'C':
					putchar('E');
					break;
				case 'D':
					putchar('S');
					break;
				case 'E':
					putchar('O');
					break;
				case 'F':
					putchar('C');
					break;
				case 'G':
					putchar('V');
					break;
				case 'H':
					putchar('X');
					break;
				case 'I':
					putchar('D');
					break;
				case 'J':
					putchar('U');
					break;
				case 'K':
					putchar('I');
					break;
				case 'L':
					putchar('G');
					break;
				case 'M':
					putchar('L');
					break;
				case 'N':
					putchar('B');
					break;
				case 'O':
					putchar('K');
					break;
				case 'P':
					putchar('R');
					break;
				case 'Q':
					putchar('Z');
					break;
				case 'R':
					putchar('T');
					break;
				case 'S':
					putchar('N');
					break;
				case 'T':
					putchar('W');
					break;
				case 'U':
					putchar('J');
					break;
				case 'V':
					putchar('P');
					break;
				case 'W':
					putchar('F');
					break;
				case 'X':
					putchar('M');
					break;
				case 'Y':
					putchar('A');
					break;
				case 'Z':
					putchar('Q');
					break;
				case ' ':
					putchar(' ');
					break;
			}
		} // end of for
		putchar('\n');
	}
	system("pause");
	return 0;
}