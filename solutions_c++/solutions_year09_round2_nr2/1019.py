#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <sstream>
#include <cstdlib>
using namespace std;

int main()
{
	ifstream fin;
	fin.open ("example.txt");

	ofstream fout;
	fout.open ("number.txt");

	int N;
	fin >> N;

	// read/process dictionary
	for( int i = 0; i < N; i++ ) {
		list<int> alist;
		list<int>::iterator p;
		string number;

		fin >> number;

		int largest = -1;
		int smallest = 10;
		string newnum = "";
		for( int j = number.length()-1; j >= 0; j-- ) {
			int num = number[j] - '0';

			if( num >= largest ) {
				largest = num;
				if( num < smallest && num != 0 ) {
					smallest = num;
				}
				alist.push_back(num);
			}
			else if( num < largest) {
				alist.push_back(num);
				alist.sort();
				p = alist.begin();
				while( p != alist.end() && *p <= num) {
					p++;
				}
				newnum = number.substr(0,j);
				newnum += *p + '0';
				alist.erase(p);
				p = alist.begin();
				while( p != alist.end() ) {
					newnum += *p + '0';
					p++;
				}
				break;
			}
		}
		if( newnum.length() == 0 ) {
			alist.push_back(0);
			alist.sort();
			p = alist.begin();
			while( p != alist.end() && *p != smallest) {
				p++;
			}
			
			newnum += *p + '0';
			alist.erase(p);

			p = alist.begin();
			while( p != alist.end() ) {
				newnum += *p + '0';
				p++;
			}

		}
		cout << "Case #" << i+1 << ": " << newnum << endl;
		fout << "Case #" << i+1 << ": " << newnum << endl;
	}

	return 0;
}
