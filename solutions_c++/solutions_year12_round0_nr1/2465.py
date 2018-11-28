#include <cstdio>
#include <iostream>
#include <cstring>
 
using namespace std;
char map[30];
int numCase;
 
int main() {
        FILE *fin = fopen("A-small-attempt0.in", "r");
		FILE *fout = fopen("A.out", "w");
        map[0] = 'y'; map[1] = 'h'; map[2] = 'e'; map[3] = 's'; map[4] = 'o'; map[5] = 'c'; 
        map[6] = 'v'; map[7] = 'x'; map[8] = 'd'; map[9] = 'u'; map[10] = 'i'; map[11] = 'g'; 
        map[12] = 'l'; map[13] = 'b'; map[14] = 'k'; map[15] = 'r'; map[16] = 'z'; map[17] = 't'; 
        map[18] = 'n'; map[19] = 'w'; map[20] = 'j'; map[21] = 'p'; map[22] = 'f'; map[23] = 'm'; 
        map[24] = 'a'; map[25] = 'q';
        fscanf (fin, "%d\n", &numCase);
        for (int i = 0; i < numCase; i++) {
                char buffer[110];
                fscanf (fin, "%[^\n]\n", buffer);
                int stringlength = strlen(buffer);
				fprintf(fout, "Case #%d: ", i + 1);
                for (int j = 0; j < stringlength; j++) {
						if (buffer[j] == ' ')
							fprintf(fout, " ");
						else
							fprintf (fout, "%c", map[buffer[j] - 'a']);
                }
				fprintf (fout, "\n");
        }
        return 0;
}