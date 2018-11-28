/*
 * 1b.cpp
 *
 *  Created on: May 21, 2010
 *      Author: Justin Li
 */
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <queue>
#include <stack>
#include <fstream>
using namespace std;

string existing[200], temp, temp2;
int N;
map<string,bool> dirs;
bool mkdir(string dir) {
	return false;
}

int main() {
	ifstream in;
	in.open("A-large-2.in.txt"); //IS THIS RIGHT?
	ofstream out;
	out.open("file.out"); //IS THIS RIGHT?
	int T,i,M,j;
	unsigned int k;
	in >> T;
	int counter;
	for (i=0;i<T;i++) {
		in >> N >> M;
		dirs.clear();
		counter=0;
		for (j=0;j<N;j++) {
			in >> temp;
			temp2="";
			for (k=1;k<temp.length();k++) {
				if (k==temp.length()-1)
					temp2 += temp[k];
				if (temp[k] == '/'||k==temp.length()-1) {
					dirs.insert(make_pair(temp2,true));
				}
				temp2 += temp[k];
			}
		}
		/*for ( std::map< string, bool, std::less< int > >::const_iterator iter = dirs.begin();
		      iter != dirs.end(); ++iter )
		      cout << "foo "<< iter->first << '\n';*/
		//cout << endl;
		for (j=0;j<M;j++) {
			in >> temp;
			temp2="";
			for (k=1;k<temp.length();k++) {
				if (k==temp.length()-1)
					temp2 += temp[k];
				if (temp[k] == '/'||k==temp.length()-1) {
					//cout << temp2 << endl;
					if(dirs.find(temp2)==dirs.end()) {
						dirs.insert(make_pair(temp2, true));
						counter++;
						//cout << temp2 << endl;
					} else {
						//cout << "!!!";
					}
				}
				temp2 += temp[k];
			}
		}
		cout << "Case #" << i+1 << ": " << counter << endl;
	}
	in.close();
	out.close();
	return 0;
}
