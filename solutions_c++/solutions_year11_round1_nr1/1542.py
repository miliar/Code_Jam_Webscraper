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

// get smallest integer that gives integer from percentes
int getSmallestInteger( int percent ){
	if(percent == 0)
		return 1;
	for(int i = 1; i <= 100; i++){
		if( (float)(i*percent)/100 == (int)((i*percent)/100) ){
			return i;
		}
	}
	return 0;
}

void mainFunction(){
	ofstream response_file;
	response_file.open ("response.txt");

	ifstream myfile("A-small-attempt1.in");

	string temp_str;

    if (!myfile) {
        cout << "Unable to open file";
        exit(1); // terminate with error
    }

    cout << getSmallestInteger(53) << endl;
    cout << getSmallestInteger(44) << endl;

	// just parse first line
    getline(myfile,temp_str);

	int i = 0, j;
    int caret;

	int max_games = 0;
	int percent_day = 0;
	int percent_game = 0;

	int games_d;
	int games_g;

	bool possible;

	while(!myfile.eof()){
		i++;
		getline(myfile,temp_str);

		if(temp_str.size() == 0)
			break;

		caret = 0;
		max_games = 0;
		percent_day = percent_game = 0;
		// parse test case
			// get max_games
			while((char)temp_str[caret] != ' '){
				max_games *= 10;
				max_games += chatToInt(temp_str[caret]);
				caret++;
			}

			caret++;

			// get percent_day
			while(temp_str[caret] != ' '){

				percent_day *= 10;
				percent_day += chatToInt(temp_str[caret]);
				caret++;

			}

			caret++;

			// get percent_game
			while(temp_str.size() > caret && temp_str[caret] != ' '){
				percent_game *= 10;
				percent_game += chatToInt(temp_str[caret]);
				caret++;
			}

			// test case
			games_d = getSmallestInteger( percent_day );
			games_g = getSmallestInteger( percent_game );

			possible = false;

			if( percent_day == percent_game && ( percent_day == 0 || percent_day == 100 ) ){
				possible = true;
			}else if( games_d <= max_games ){
				if( ( percent_day == 0 && percent_game < 100 ) || ( percent_day > 0 && percent_day < 100 && percent_game > 0 && percent_game < 100 ) || ( percent_day == 100 && percent_game > 0 ) )
					possible = true;
			}
//			else{
//				possible = false;
//			}

		// save data into file
		if(possible){
			response_file << "Case #" << i << ": Possible" << endl;
			cout << "Case #" << i << ": Possible" << endl;
		}else{
			response_file << "Case #" << i << ": Broken" << endl;
			cout << "Case #" << i << ": Broken" << endl;
		}

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
