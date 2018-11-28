#include <cstdio>
#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int n, k, h;
	
	ifstream myfile;
	myfile.open("A-large.in"); 
	myfile >> h;
	
	ofstream out;
	out.open("A-large.out");
	
	for(int j = 0; j < h; j++) {
		myfile >> n; myfile >> k;
		k++;
		bool flag = true;
		for(int i = 0; i < n; i++) {
			if(k % 2 == 1) {
				flag = false;
				break;
			} else if(k > 0) 
				k /= 2;
			else {
				flag = false;
				break;
			}
		}
		
		out << "Case #" << j+1 << ": ";
		if(flag)
			out << "ON" << endl;
		else
			out << "OFF" << endl;
			
		cout << j << endl;
	}
}
