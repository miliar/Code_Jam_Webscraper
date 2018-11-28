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

int getNextPosition(string str, char c, int caret){
	int temp = 0;
	while(caret < str.size() && str[caret] != c){
		caret++;
	}
	caret += 2;
	while(caret < str.size() && str[caret] != ' '){
		temp = temp * 10;
		temp += chatToInt(str[caret]);
		caret++;
	}

	return temp;
}

void mainFunction(){
	ofstream response_file;
	response_file.open ("response.txt");

	ifstream myfile("A-large.in");

	string temp_str;

    if (!myfile) {
        cout << "Unable to open file";
        exit(1); // terminate with error
    }

	// just parse first line
    getline(myfile,temp_str);

	int i = 0, j;
    int test_length;
    int caret;

    int position_blue, position_orange;
    char next_color;
    int next_position, next_oposite_position;


    int total_seconds;

	while(!myfile.eof()){
		i++;
		getline(myfile,temp_str);
		if(temp_str.size() == 0)
			break;

		caret = 0;
		test_length = 0;

		position_blue = position_orange = 1;
		total_seconds = 0;
		// parse test case
			// get test_length
			while(temp_str[caret] != ' '){
				test_length *= 10;
				test_length += chatToInt(temp_str[caret]);
				caret++;
			}

			// go through each step
			for( j = 0; j < test_length; j++){
				// Get next color
				caret++;
				next_color = temp_str[caret];
				// Get next position
				next_position = 0;
				caret+=2;
				while(caret < temp_str.size() && temp_str[caret] != ' '){
					next_position *= 10;
					next_position += chatToInt(temp_str[caret]);
					caret++;
				}

				if(next_color == 'B'){

					// Blue moves
					total_seconds += abs(next_position - position_blue) + 1;
					// Orange moves
					next_oposite_position = getNextPosition(temp_str, 'O', caret );
					if(next_oposite_position > 0 && next_oposite_position != position_orange){
						if(next_oposite_position > position_orange){
							// add
							position_orange += abs(next_position - position_blue) + 1;
							if(position_orange > next_oposite_position)
								position_orange = next_oposite_position;
						}else{
							// substract
							position_orange -= abs(next_position - position_blue) + 1;
							if(position_orange < next_oposite_position)
								position_orange = next_oposite_position;
						}
					}
					// Save time
					position_blue = next_position;
				}else if(next_color == 'O'){
					// Orange moves
					total_seconds += abs(next_position - position_orange) + 1;
					// Blue moves
					next_oposite_position = getNextPosition(temp_str, 'B', caret );
					if(next_oposite_position > 0 && next_oposite_position != position_blue){
						if(next_oposite_position > position_blue){
							// add
							position_blue += abs(next_position - position_orange) + 1;
							if(position_blue > next_oposite_position)
								position_blue = next_oposite_position;
						}else{
							// substract
							position_blue -= abs(next_position - position_orange) + 1;
							if(position_blue < next_oposite_position)
								position_blue = next_oposite_position;
						}
					}
					// Save time
					position_orange = next_position;
				}
//				cout << total_seconds << " " << position_blue << " " << position_orange << endl;
			}


		// save data into file
		response_file << "Case #" << i << ": " << total_seconds << endl;
		cout << "Case #" << i << ": " << total_seconds << endl;
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
