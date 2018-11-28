#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using  namespace std;

const int LINE_LENGTH = 65536;
const int WORD_LENGTH = 64;


int main(int argc, char ** argv)
{
    char * filename = argv[1];
    ifstream inp (filename);
    ofstream outp("C_output");
    
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
    
    int i, ii, iii, limitIdx;
    int A, B, M, N, numM, numN, tempM, tempN, temp1, temp2;
    int digitArray[10];
    bool flag;
    int numRecycle[numTestcase]; for (i = 0; i < numTestcase; i++) numRecycle[i] = 0;

    for (i = 0; i < numTestcase; i++) {
        inp.getline(line_buffer, LINE_LENGTH);
	lp = line_buffer; limitIdx = 0;
	do {
	    wp = word_buffer;
	    while (*lp && ((*lp == ' ') || (*lp == '\t'))) lp++;
	    while (*lp && (*lp != ' ') && (*lp != '\t') && (*lp != '\n')) *(wp++) = *(lp++);
	    *wp = '\0';
	    
	    if (limitIdx == 0) {A = atoi(word_buffer); limitIdx ++;}
	    else B = atoi(word_buffer);
	} while (*lp);

	for (N = A; N < B; N++) {
	    tempN = N; numN = 0;
	    while (tempN != 0) { numN ++; tempN = tempN / 10; }
	    int digitsN[numN];
	    tempN = N; ii = 0;
	    while (tempN != 0) { digitsN[ii] = tempN % 10; tempN = tempN / 10; ii++; }
	    
	    for (M = N + 1; M <= B; M++) {
	        tempM = M; numM = 0;
		while(tempM != 0) { numM ++; tempM = tempM / 10; }
		int digitsM[numM];
		if (numN != numM) break;
		tempM = M; ii = 0;
		while(tempM != 0) { digitsM[ii] = tempM % 10; tempM = tempM / 10; ii++; }
		flag = false;
		for (ii = 0; ii < 10; ii++) digitArray[ii] = 0;
		for (ii = 0; ii < numN; ii++) digitArray[digitsN[ii]] ++;
		for (ii = 0; ii < numM; ii++) digitArray[digitsM[ii]] --;
		for (ii = 0; ii < 10; ii++) if (digitArray[ii] != 0) { flag = true; break; }
		if (flag == true) continue;
		
		iii = numN; temp2 = 1;
		while (iii != 0) { temp2 = temp2 * 10; iii--; } //temp2 = 10^numN
		for (ii = 1; ii < numN; ii++) {
		    iii = ii; temp1 = 1;
		    while (iii != 0) { temp1 = temp1 * 10;  iii --; } //temp1 = 10^ii
		    tempN = N / temp1 + (N % temp1) * (temp2 / temp1);
		    if (tempN == M) { numRecycle[i]++; break; }
		}
	    }
	}
	
	outp << "Case #" << i+1  <<": " << numRecycle[i] << endl;
    }

    return 0;
}
