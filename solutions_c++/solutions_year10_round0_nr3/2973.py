/*
 * 2.cpp
 *
 *  Created on: May 8, 2010
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

int main() {
	ifstream in;
	in.open("C-small.in");
	ofstream out;
	out.open("file.out");
	int k, R, T, N, i, j, index, curr, money, lastindex;
	int groups[15];
	in >> T;
	for (i=0;i<T;i++) {
		money=0;
		index=0;
		in >> R >> k >> N;
		for (j=0;j<N;j++) {
			in >> groups[j];
		}
		//cout << R << " " << k << " "<< N << " : ";
		for (j=0;j<R;j++) {
			curr = 0;
			lastindex=index;
			while(true) {
				//cout << index << " " << curr << " " << lastindex << endl;
				if (curr+groups[index]<=k) {
				curr+=groups[index];
				index++;
				if (index>=N) {
					index=0;
				}
				if (index==lastindex) break;
				} else break;
			}
			//cout << endl;
			money+=curr;
		}
		out << "Case #" << i+1 << ": " << money << endl;
	}
	in.close();
	out.close();
	return 0;
}
