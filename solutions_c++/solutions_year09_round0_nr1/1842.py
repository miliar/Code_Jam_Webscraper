/*
 * Alien.cpp
 *
 *  Created on: Sep 3, 2009
 *      Author: fu4ny
 */

#include <iostream>
#include <vector>
#include <fstream>
using std::vector;
using std::string;
using std::cin;
using std::ifstream;
using std::ofstream;
vector<string> L_;
vector<string> D_;
int L,D,N;
void readInput();


int main() {
readInput();
}


void readInput () {
	ifstream ifs("A-large.in");
	ofstream ofs("A-large.ou");
	ifs >> L >> D >> N;
	ifs.ignore(1,'\n');
	for ( int i=1; i<= D; i++ ) {
		string str;
		getline(ifs,str);
		L_.push_back(str);
	}

	for (int i=1; i<=N; i++ ) {
		string str;
		getline(ifs,str);
		unsigned int j = 0;
		while ( j<str.length() ) {
			if ( str[j] != '(' ) {
				string pk;
				pk += str[j];
				D_.push_back(pk);
				std::cout << pk << " ";
			} else {
				j++;
				string pl;
				while ( str[j] != ')' ) {
					pl += str[j];
					j++;
				}
				std::cout << pl << " ";
				D_.push_back(pl);
			}
			j++;
		}
		std::cout<<std::endl;


				int count = 0;
				for ( int j=0; j<D; j++ ) {
					string temp=L_[j];
					std::cout << temp << std::endl;
					for ( int k=0; k<temp.length(); k++ ) {
						if ( D_[k].find(temp[k]) == std::string::npos ) {
							count--;
							break;
						}
					}
					count ++;
				}

				ofs << "Case #" << i << ": " << count << std::endl;

				D_.clear();
	}
	ofs.close();
	ifs.close();
}
