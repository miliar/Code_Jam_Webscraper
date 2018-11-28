#include <iostream> //for cout
#include <stdio.h> //for freopen(), scanf()
#include <string> //for std::string

/**
 */

int T,G;
char S[100];
const char * c = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d",&T); //loads the number of cases
	G = getc(stdin); //lazily clears the first new line

	for (int i = 1; (i <= T); i++) //iterate the cases
	{
		int j = 0;
		do {
			G = getc(stdin);
			if ((G>=97)&&(G<=122)) {
				S[j] = c[(G-97)];
			}
			else {
				S[j] = G;
			}
		} while (S[j++] != '\n');

		while (j<100) {
			S[j]='\0';
			j++;
		}
		std::cout << "Case #" << i << ": " << S;
	}
	return 0;
}
