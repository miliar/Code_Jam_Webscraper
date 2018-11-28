#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

/* ==================
    Here are comments
================== */

using namespace std;

int chatToInt(char c){
	return (int)(c-48);
}

void mainFunction(){
	ofstream response_file;
	response_file.open ("response.txt");

	ifstream myfile("C-small-attempt3.in");

	string temp_str;

    if (!myfile) {
        cout << "Unable to open file";
        exit(1); // terminate with error
    }

	// just parse first line
    getline(myfile,temp_str);

    int tests_length = 0;
    int caret = 0;
    while(caret < temp_str.size() && temp_str[caret] != ' '){
		tests_length *= 10;
		tests_length += chatToInt(temp_str[caret]);
		caret++;
	}

	int k;

	int test_length, i, j, temp_int;
	vector<long> candies;
	vector<long>::iterator it;

	string binary_map;

	long candies_max, candies_bbig, candies_bsmall;
	long candies_bbig_int, candies_bsmall_int;

	for(k = 0; k < tests_length; k++){
		// Get number of candies
		getline(myfile,temp_str);
		test_length = caret = 0;
		while(caret < temp_str.size() && temp_str[caret] != ' '){
			test_length *= 10;
			test_length += chatToInt(temp_str[caret]);
			caret++;
		}

		// Get candies
		getline(myfile,temp_str);
		candies.clear();
		caret = 0;
		for(i = 0; i< test_length; i++){
			temp_int = 0;
			while(caret < temp_str.size() && temp_str[caret] != ' '){
				temp_int *= 10;
				temp_int += chatToInt(temp_str[caret]);
				caret++;
			}
			caret++;
			candies.push_back(temp_int);
		}
		// Sort
//		candies.sort();

		candies_max = 0;

		// Will go through all subsets
		// Test for possible division
		candies_bsmall = 0;
		for(j = 0; j < candies.size(); j++){
			candies_bsmall ^= (int)candies[j];
		}
		// Create strings of 01 with all posible amounts of 0s and 1s
		if(candies_bsmall == 0){
//			cout <<ceil((double)candies.size()/2) <<endl;
//			for(i=1; i < candies.size(); i++){
			for(i=1; i < ceil((double)candies.size()/2)+1; i++){
				binary_map = "";

				for(j = 0; j < candies.size(); j++){
					if(j < i)
						binary_map.append("0");
					else
						binary_map.append("1");
				}

				// Permotate tham to obtain all possible subsets
				do{
					candies_bbig = candies_bsmall = 0;
					candies_bbig_int = candies_bsmall_int = 0;
					for(j = 0; j < candies.size(); j++){
						if(binary_map[j] == '0'){
							// small brother
							candies_bsmall ^= (int)candies[j];
							candies_bsmall_int += (int)candies[j];
						}else{
							// big brother
							candies_bbig ^= (int)candies[j];
							candies_bbig_int += (int)candies[j];
						}
					}
					if(candies_bsmall == candies_bbig && min(candies_bbig_int, candies_bsmall_int) > 0 && max(candies_bbig_int, candies_bsmall_int) > candies_max)
						candies_max = max(candies_bbig_int, candies_bsmall_int);
	//				cout << binary_map << endl;
				}while (std::next_permutation(binary_map.begin(), binary_map.end()));

	//			cout << candies_bsmall << " " << candies_bbig << " " << candies_bsmall_int << " " << candies_bbig_int << endl;


			}
		}

		if(candies_max > 0){
			cout << "Case #" << k+1 << ": " << candies_max << endl;
			response_file << "Case #" << k+1 << ": " << candies_max << endl;
		}else{
			cout << "Case #" << k+1 << ": NO" << endl;
			response_file << "Case #" << k+1 << ": NO" << endl;
		}


//		for (it=candies.begin(); it!=candies.end(); ++it)
//			cout << *it << endl;
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
