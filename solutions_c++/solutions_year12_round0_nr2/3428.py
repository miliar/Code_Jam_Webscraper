#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <assert.h>

using namespace std;

const int LINE_LENGTH = 65536;
const int WORD_LENGTH = 64;


int main(int argc, char ** argv)
{
    char * filename = argv[1];
    ifstream inp (filename);
    ofstream outp("B_output");
    
    if (!inp) {
        cerr << "Can't open input file" << endl;
	exit(1);
    }
    
    if (!outp) {
        cerr << "Can't open output file" << endl;
	exit(1);
    }
    
    char line_buffer[LINE_LENGTH]; char *lp;
    char word_buffer[WORD_LENGTH]; char *wp;
    
    inp.getline(line_buffer, LINE_LENGTH);
    lp = line_buffer; wp = word_buffer;
    while (*lp && ((*lp == ' ') || (*lp == '\t'))) lp++;
    while (*lp && (*lp != ' ') && (*lp != '\t') && (*lp != '\n')) *(wp++) = *(lp++);
    *wp = '\0';
    int numTestcase = atoi(word_buffer);
    
    int i, ii, idx;
    int numMax[numTestcase]; for (i = 0; i < numTestcase; i++) numMax[i] = 0;
    int N, S, p, avg, res, t;
    
    for (i = 0; i < numTestcase; i++) {
        inp.getline(line_buffer, LINE_LENGTH);
	lp = line_buffer; idx = 0;
	do {
	    wp = word_buffer;
	    while (*lp && ((*lp == ' ') || (*lp == '\t'))) lp++;
	    while (*lp && (*lp != ' ') && (*lp != '\t') && (*lp != '\n')) *(wp++) = *(lp++);
	    *wp = '\0';
	    
	    if (idx == 0) { N = atoi(word_buffer); idx ++;}
	    else if (idx == 1) { S = atoi(word_buffer); idx ++; }
	    else if (idx == 2) { p = atoi(word_buffer); idx ++; }
	    else {
	        t = atoi(word_buffer); idx ++;
		avg = t/3; res = t%3;
		if (avg >= p ) { numMax[i] ++; continue; }
		if (avg < p-2) { continue; }
		if (avg == p-2 && res == 2 && S > 0) { numMax[i] ++; S --; continue; }
		if (avg == p-1 && S > 0 && res == 0 && (avg - 1 >= 0)) { numMax[i] ++; S --; continue; }
		if (avg == p-1 && res != 0) { numMax[i] ++; continue; }
	    }
	} while (*lp);
	
	assert(idx == N+3);

	outp << "Case #" << i+1  <<": " << numMax[i] << endl;
    }
    
    return 0;
}
