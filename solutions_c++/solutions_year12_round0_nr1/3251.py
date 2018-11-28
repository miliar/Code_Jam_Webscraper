#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using  namespace std;

const int LINE_LENGTH = 128;
const int WORD_LENGTH = 64;


int main(int argc, char ** argv)
{
    char * filename = argv[1];
    ifstream inp (filename);
    ofstream outp("A_output");
    
    if (!inp) {
      cerr << "Can't open input file" << endl;
      exit(1);
    }
    
    if (!outp) {
      cerr << "Can't open output file" << endl;
      exit(1);
    }
    
    char line_buffer[LINE_LENGTH]; char *lp;
    char copy_buffer[LINE_LENGTH];
    char word_buffer[WORD_LENGTH]; char *wp;
    
    inp.getline(line_buffer, LINE_LENGTH);
    lp = line_buffer; wp = word_buffer;
    while (*lp && ((*lp == ' ') || (*lp == '\t'))) lp++;
    while (*lp && (*lp != ' ') && (*lp != '\t') && (*lp != '\n')) *(wp++) = *(lp++);
    *wp = '\0';
    int numTestcase = atoi(word_buffer);
    
    int i, ii;
    char map[26];
    map[0]  = 'y'; map[1]  = 'h'; map[2]  = 'e'; map[3]  = 's'; map[4]  = 'o';
    map[5]  = 'c'; map[6]  = 'v'; map[7]  = 'x'; map[8]  = 'd'; map[9]  = 'u';
    map[10] = 'i'; map[11] = 'g'; map[12] = 'l'; map[13] = 'b'; map[14] = 'k';
    map[15] = 'r'; map[16] = 'z'; map[17] = 't'; map[18] = 'n'; map[19] = 'w';
    map[20] = 'j'; map[21] = 'p'; map[22] = 'f'; map[23] = 'm'; map[24] = 'a';
    map[25] = 'q';
    
    for (i = 0; i < numTestcase; i++) {
        inp.getline(line_buffer, LINE_LENGTH);
	lp = line_buffer; ii = 0;
	
	do {
	    if (*lp == ' ') { copy_buffer[ii] = ' '; ii++; lp++; }
	    else {
	      int idx = *lp - 'a';
	      copy_buffer[ii] = map[idx];
	      ii++;
	      lp++;
	    }
	} while(*lp);
	copy_buffer[ii] = '\0';
	
	outp << "Case #" << i+1  <<": " << copy_buffer << endl;
    }
    
    return 0;
}
