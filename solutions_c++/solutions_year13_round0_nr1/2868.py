#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

int main(){
	ifstream in("A-large.in");
	ofstream out("answer1.txt");
	
	int T;
	in >> T;

	for (int p = 0; p < T; p++){
		string array[4];
		for (int i = 0; i < 4; i ++){
			in >> array[i];
		}
		int sum = 0;
		bool flag = 0;
		for (int i = 0; i < 4; i ++){
			sum = array[i][0] * array[i][1] * array[i][2] * array[i][3];
			if (sum == 'X' * 'X' * 'X' * 'X' || sum == 'X' * 'X' * 'T' * 'X'){
				if (flag == 0)
					out << "Case #" << p+1 << ": X won" << endl;
				flag = 1;
			}
			else if (sum == 'O' * 'O' * 'O' * 'O' || sum == 'O' * 'O' * 'O' * 'T'){
				if (flag == 0)

					out << "Case #" << p+1 << ": O won" << endl;
				flag = 1;
			}
			
			sum = array[0][i] * array[1][i] * array[2][i] * array[3][i];
			if (sum == 'X' * 'X' * 'X' * 'X' || sum == 'X' * 'X' * 'T' * 'X'){
if (flag == 0)

                                out << "Case #" << p+1 << ": X won" << endl;
				flag = 1;
			}
                        else if (sum == 'O' * 'O' * 'O' * 'O' || sum == 'O' * 'O' * 'O' * 'T'){
if (flag == 0)

                                out << "Case #" << p+1 << ": O won" << endl;
				flag = 1;
			}
		}
		 sum = array[0][0] * array[1][1] * array[2][2] * array[3][3];
                        if (sum == 'X' * 'X' * 'X' * 'X' || sum == 'X' * 'X' * 'T' * 'X'){
if (flag == 0)

                                out << "Case #" << p+1 << ": X won" << endl;
                                flag = 1;
                        }
                        else if (sum == 'O' * 'O' * 'O' * 'O' || sum == 'O' * 'O' * 'O' * 'T'){
if (flag == 0)

                                out << "Case #" << p+1 << ": O won" << endl;
                                flag = 1;
                        }

                        sum = array[0][3] * array[1][2] * array[2][1] * array[3][0];
                        if (sum == 'X' * 'X' * 'X' * 'X' || sum == 'X' * 'X' * 'T' * 'X'){
if (flag == 0)

                                out << "Case #" << p+1 << ": X won" << endl;
                                flag = 1;
                        }
                        else if (sum == 'O' * 'O' * 'O' * 'O' || sum == 'O' * 'O' * 'O' * 'T'){
if (flag == 0)

                                out << "Case #" << p+1 << ": O won" << endl;
                                flag = 1;
                        }

                        for (int i = 0; i < 4; i++){
                                for (int j = 0; j < 4; j++){
                                        if (array[i][j] == '.' && flag == 0){
                                                out << "Case #" << p+1 << ": Game has not completed" << endl;
                                        	flag = 1;
					}
                                }
                        }
                        if (flag == 0)
				out << "Case #" << p+1 << ": Draw" << endl;
			
	}
	
}
