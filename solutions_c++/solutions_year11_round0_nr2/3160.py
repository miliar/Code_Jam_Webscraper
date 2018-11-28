/*
 * =====================================================================================
 *
 *       Filename:  b.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  05/07/2011 09:33:17 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <string>

using namespace std;

int main(){
	int T, C, D, N;
	cin >> T;
	for(int i = 0 ; i  < T; ++i){
		cout << "Case #"<<i+1 <<": [";

		vector<char> output;
		vector<string> comb, oppose;
		string temp;
		cin >> C;
		for(int j = 0; j < C; ++j){
			cin >> temp;
			comb.push_back(temp);
		}
		cin >> D;
		for(int j = 0; j < D; ++j){
			cin >> temp;
			oppose.push_back(temp);
		}   
		cin >> N;
		cin >> temp;
		if(N != 0){
			output.push_back(temp[0]);

			for(int j = 1; j < temp.length(); ++j){
				bool isComb = false;
				bool isOpp = false;
				//first combine
				char op1 = temp[j]; 
				char op2 = output.back();

				for(int k =0; k < comb.size(); ++k){
					char c1 = comb[k][0];
					char c2 = comb[k][1];
					if(max(op1, op2) == max(c1, c2) && min(op1, op2) == min(c1,c2)){
						output.pop_back();
						output.push_back(comb[k][2]);
						isComb = true;
						break;
					}
				}
				//then clear
				if(!isComb){
					for(int k =0; k < oppose.size(); ++k){
						char toSearch = -1;
						if(temp[j] == oppose[k][0]){
							toSearch = oppose[k][1];
						}
						else if(temp[j] == oppose[k][1]){
							toSearch = oppose[k][0];
						}
						if(toSearch != -1 && find(output.begin(), output.end(), toSearch) != output.end()){
							output.clear();
							isOpp = true;
							break;
						}

					}
				}
				if(!isComb && !isOpp) output.push_back(temp[j]);
			}
			for(int k =0; k < output.size(); ++k){
				if( k != 0) cout << ", ";
				cout << output[k];
			}
		}
		cout<< "]" << endl;

	}
}
