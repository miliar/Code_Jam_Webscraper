#include <iostream>
#include <fstream>
#include <conio.h>
#include <cmath>
#include <string>

using namespace std;

int main(){
	fstream fin, fout;
	fin.open("B-large.in", fstream::in); 
	fout.open ("out.txt", fstream::out);
	
	int ntest;
	int n, s, p;
	
	fin >> ntest;
	
	for(int k = 1; k <= ntest; k++){
		int snumber = 0;
		int accepted = 0;
		int total;
		fin >> n >> s >> p;
		for(int i = 0; i < n; i++){
			fin >> total;
			
			if(ceil(total/3.0) >= p)
				accepted++;
			else{
				if(total%3 !=2){
					if(total/3 + 1 >= p && total/3 -1 >= 0)
						snumber++;
				}
				else{
					if(total/3 + 2 >= p)
						snumber++;
				}
			}
		}	
		int result = min(snumber, s) + accepted;
		fout << "Case #" << k << ": " << result << endl;
	}
	getch();
	return 0;
}
