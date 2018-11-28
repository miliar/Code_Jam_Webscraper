#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <fstream>
#include <string>

/* ==================
    Here are comments
================== */

using namespace std;

int chatToInt(char c){
	return (int)(c-48);
}

char getCombination(char char_1, char char_2 ,char combinations[36][3], int combinations_length){
	int i = 0;
	for(i = 0; i < combinations_length; i++){
		if(combinations[i][0] == char_2){
			if(combinations[i][1] == char_1)
				return combinations[i][2];
		}else if(combinations[i][1] == char_2){
			if(combinations[i][0] == char_1)
				return combinations[i][2];
		}
	}

	return ' ';
}

bool isOpposite(char char_1, char opposed[28][2], int opposed_length, char finalspell[100], int finalspell_length){
	int i = 0, j = 0;

	for(i = 0; i < opposed_length; i++){
		if(opposed[i][0] == char_1){
			for(j = 0; j < finalspell_length; j++){
				if(opposed[i][1] == finalspell[j])
					return true;
			}
		}else if(opposed[i][1] == char_1){
			for(j = 0; j < finalspell_length; j++){
				if(opposed[i][0] == finalspell[j])
					return true;
			}
		}
	}

	return false;
}

void mainFunction(){
	ofstream response_file;
	response_file.open ("response.txt");

	ifstream myfile("B-large.in");

	string temp_str;

    if (!myfile) {
        cout << "Unable to open file";
        exit(1); // terminate with error
    }

	// just parse first line
    getline(myfile,temp_str);

	int i, j, k = 0;
    int test_length;
    int caret;


    int combinations_length;
    char combinations[36][3];

    int opposed_length;
    char opposed[28][2];

	int spell_length;
    char spell[100];

	int finalspell_length;
    char finalspell[100];

	while(!myfile.eof()){
		k++;
		getline(myfile,temp_str);
		if(temp_str.size() == 0)
			break;

		// nullify all the data
		caret = 0;
		combinations_length = 0;
		for(i = 0; i < 36; i++){
			for(j = 0; j < 3; j++){
				combinations[i][j] = ' ';
			}
		}

		opposed_length = 0;
		for(i = 0; i < 28; i++){
			for(j = 0; j < 2; j++){
				opposed[i][j] = ' ';
			}
		}

		spell_length = finalspell_length = 0;
		for(i = 0; i < 100; i++){
			spell[i] = ' ';
			finalspell[i] = ' ';
		}


		// parse test case
			// get combinations_length
			while(temp_str[caret] != ' '){
				combinations_length *= 10;
				combinations_length += chatToInt(temp_str[caret]);
				caret++;
			}

			// get all combinations
			for(i = 0; i < combinations_length; i++){
				for(j = 0; j < 3; j++){
					caret++;
					combinations[i][j] = temp_str[caret];
				}
				caret++;
			}

			caret++;
			// get opposed_length
			while(temp_str[caret] != ' '){
				opposed_length *= 10;
				opposed_length += chatToInt(temp_str[caret]);
				caret++;
			}
			// get all oposites
			for(i = 0; i < opposed_length; i++){
				for(j = 0; j < 2; j++){
					caret++;
					opposed[i][j] = temp_str[caret];
				}
				caret++;
			}

			caret++;
			// get string_length
			while(temp_str[caret] != ' '){
				spell_length *= 10;
				spell_length += chatToInt(temp_str[caret]);
				caret++;
			}
			// get string
			for(i = 0; i < spell_length; i++){
				caret++;
				spell[i] = temp_str[caret];
			}

		// Make additions one by one to string
		for( i = 0; i < spell_length; i++){
			if(i == 0 || finalspell_length == 0){
				finalspell[finalspell_length] = (char)spell[i];
				finalspell_length++;
			}else{
				// Parse last two for combinations
				if(getCombination(spell[i], finalspell[finalspell_length-1],combinations, combinations_length) != ' '){
					finalspell[finalspell_length-1] = getCombination(spell[i], finalspell[finalspell_length-1],combinations, combinations_length);
				}else{
					finalspell[finalspell_length] = spell[i];
					finalspell_length++;
				}
				// Parse last for opposites
				if(isOpposite(finalspell[finalspell_length-1], opposed, opposed_length, finalspell, finalspell_length)){
					finalspell_length = 0;
				}
			}
		}




		// save data into file
		response_file << "Case #" << k << ": [";
		for(i = 0; i < finalspell_length; i++){
			response_file << finalspell[i];
			if(i < finalspell_length-1)
				response_file << ", ";
		}
		response_file << "]" << endl;
		// output
		cout << "Case #" << k << ": [";
		for(i = 0; i < finalspell_length; i++){
			cout << finalspell[i];
			if(i < finalspell_length-1)
				cout << ", ";
		}
		cout << "]" << endl;
	}

    myfile.close();
    response_file.close();
}

int main(){
    int begin, end;
    begin = clock();
    mainFunction();
    end = clock();
    cout << "Time: " << ((double)( end - begin )/CLOCKS_PER_SEC ) << endl;
    return 0;
}
