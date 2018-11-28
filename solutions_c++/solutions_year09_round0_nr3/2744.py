#include<iostream>
#include<fstream>
#include<stdlib.h>

using namespace std;

int chgDigit(char *str) {

    int digit = 0;


    for (int i = 0; str[i]; i++) {

        digit = digit * 10 + str[i] - 48;

    }

    return digit;

}

char *convertResult(long digit) {

    char *str = new char[5];

    if (digit >= 10000) {
        digit %= 10000;
    }

    for (int i = 3; i >= 0; i--) {
        if (digit) {
            str[i] = digit % 10 + 48;
            digit /= 10;
        }else {
            str[i] = 48;
        }
    }
    str[4] = 0;

    return str;

}

//char * const mainString = "welcome to code jam";
int mainCount[19];
int *mainPtr[19];
long *mainVP[19];
int mainCursor[19];

long countCodeJam(char *str) {

    int i, j, k;
    long value;

    for (i = 0; i < 19; i++) {
	mainCount[i] = 0;
	mainCursor[i] = 0;
    }

    for (i = 0; str[i]; i++) {
        switch (str[i]) {
            case 'w': 
		mainCount[0]++;
                break;
            case 'e': 
		mainCount[1]++;
                mainCount[6]++;
                mainCount[14]++;
                break;
            case 'l': 
		mainCount[2]++;
                break;
            case 'c': 
		mainCount[3]++;
                mainCount[11]++;
                break;
            case 'o': 
		mainCount[4]++;
                mainCount[9]++;
                mainCount[12]++;
                break;
            case 'm': 
		mainCount[5]++;
                mainCount[18]++;
                break;
            case 't': 
		mainCount[8]++;
                break;
            case 'd': 
		mainCount[13]++;
                break;
            case 'j': 
		mainCount[16]++;
                break;
            case 'a': 
		mainCount[17]++;
                break;
            case ' ': 
		mainCount[7]++;
                mainCount[10]++;
                mainCount[15]++;
                break;
        }
    }

    for (i = 0; i < 19; i++) {
        mainPtr[i] = new int[mainCount[i]];
        mainVP[i] = new long[mainCount[i]];
        for (j = 0; j < mainCount[j]; j++) {
            mainPtr[i][j] = 0;
            mainVP[i][j] = 0;
        }
    }

    for (j = 0; j < mainCount[18]; j++) {
        *(mainVP[18] + j) = 1;
    }


    //have to write code to get position of characters
    for (i = 0; str[i]; i++) {
	j=0;
        switch (str[i]) {
            case 'w': 
		mainPtr[0][mainCursor[0]]=i; mainCursor[0]++;
                break;
            case 'e': 
		mainPtr[1][mainCursor[1]]=i; mainCursor[1]++;
		mainPtr[6][mainCursor[6]]=i; mainCursor[6]++;
		mainPtr[14][mainCursor[14]]=i; mainCursor[14]++;
                break;
            case 'l':
		mainPtr[2][mainCursor[2]]=i; mainCursor[2]++;
                break;
            case 'c':
		mainPtr[3][mainCursor[3]]=i; mainCursor[3]++;
		mainPtr[11][mainCursor[11]]=i; mainCursor[11]++;
                break;
            case 'o':
		mainPtr[4][mainCursor[4]]=i; mainCursor[4]++;
		mainPtr[9][mainCursor[9]]=i; mainCursor[9]++;
		mainPtr[12][mainCursor[12]]=i; mainCursor[12]++;
                break;
            case 'm':
		mainPtr[5][mainCursor[5]]=i; mainCursor[5]++;
		mainPtr[18][mainCursor[18]]=i; mainCursor[18]++;
                break;
            case 't':
		mainPtr[8][mainCursor[8]]=i; mainCursor[8]++;
                break;
            case 'd':
		mainPtr[13][mainCursor[13]]=i; mainCursor[13]++;
                break;
            case 'j':
		mainPtr[16][mainCursor[16]]=i; mainCursor[16]++;
                break;
            case 'a':
		mainPtr[17][mainCursor[17]]=i; mainCursor[17]++;
                break;
            case ' ':
		mainPtr[7][mainCursor[7]]=i; mainCursor[7]++;
		mainPtr[10][mainCursor[10]]=i; mainCursor[10]++;
		mainPtr[15][mainCursor[15]]=i; mainCursor[15]++;
                break;
        }
    }

    /*cout << "\nPositions => \n";
    for(i=0; i < 19; i++){
	for(j=0; j<mainCount[i]; j++){
	    cout << " " << (int)mainPtr[i][j]; 
	}
	cout << endl;
    }*/

    for (i = 17; i >= 0; --i) {

        for (j = 0; j < mainCount[i]; ++j) {
            for (k = mainCount[i + 1] - 1; k >= 0; --k) {

                if (*(mainPtr[i] + j) > *(mainPtr[i + 1] + k)) break;
                mainVP[i][j] += mainVP[i + 1][k];

            }
        }
    }

    /*cout << "Values => \n";
    for(i=0; i < 19; i++){
	for(j=0; j<mainCount[i]; j++){
	    cout << " " << mainVP[i][j]; 
	}
	cout << endl;
    }*/


    for(i=0, value=0; i< mainCount[0]; i++){
	value += mainVP[0][i];
    }

    return value;

}


// prog input_file output_file isSmall 0 => small & 1 => large

int main(int argc, char **argv) {

    char *line;
    int length;
    int count = 0;
    long result;



    if (argc != 4) {
        cout << "prog input_file output_file isSmall\n small => 0 & large => 1" << endl;
        exit(0);
    }

    length = (argv[3][0] == '0' ? 31 : 501);

    line = new char[length];

    ifstream ifl(argv[1]);

    if (!ifl) {
        cout << "File Can't Open" << endl;
        exit(0);
    }

    ofstream ofl(argv[2]);

    if (!ofl) {
        cout << "File Can't Open, check permission!!" << endl;
        exit(0);
    }


    ifl.getline(line, length);
    count = chgDigit(line);


    for (int i = 1; !ifl.eof() && i <= count; i++) {

        ifl.getline(line, length);

        result = countCodeJam(line);

        ofl << "Case #" << i << ": " << convertResult(result) << endl;


    }


    ofl.close();
    ifl.close();


}

