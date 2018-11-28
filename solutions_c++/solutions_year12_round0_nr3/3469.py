#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;


int digits(int i) {
	int d = 0;
	int n = i;
	while(n!=0){
		n /= 10;
		d++;
	}
	return d;
}
int recycle(int i, int d){
	int num = i;
	int temp = 0;
	for(int k = 0; k < d; k++){
		temp = num%10;
		num /= 10;
		num = num + temp*(pow(10,digits(i)-1));
	}
	return num;
}
int main () {
	ifstream myfile;
	myfile.open("C-small.in");
	ofstream outfile;
	outfile.open("C-small.out");
	string cases;
	getline(myfile,cases);
	int t = atoi(cases.c_str());

	string AA;
	int a;
	string BB;
	int b;
	
		recycle(12345,3);
		recycle(1,0);
		recycle(12345,5);
		recycle(1,1);
		recycle(12345,4);
	for(int j = 0; j < t; j++) {
		
		cout << "Case #" << j+1 << ":";
		outfile << "Case #" << j+1 << ":";
		
		getline(myfile,AA,' ');
		a = atoi(AA.c_str());
		getline(myfile,BB);
		b = atoi(BB.c_str());
	
	int pairs = 0;
		
		for(int x = a; x < b; x++) {
			
			for(int y = b; y > x; y--) {
				if(digits(x) == digits(y) ){
					for(int z = 0; z <= digits(x); z++){
						if(x == recycle(y,z)) {pairs++; z = digits(x);}
						/*else if(y==recycle(x,z)){ pairs++; z= digits(y); }*/
					}
				}
			}
		}
		cout << " " << pairs << endl;
		outfile << " " << pairs << endl;
	}
	
	myfile.close();
	outfile.close();
	return 0;
}
