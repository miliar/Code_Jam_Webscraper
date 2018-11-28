#include <iostream>
#include <fstream>
#include <conio.h>
#include <string>

using namespace std;

int main(){
	fstream fin, fout;
	fin.open("C-large.in", fstream::in); 
	fout.open ("out.txt", fstream::out);
	
	int ntest;
	int a, b;
	
	fin >> ntest;
	
	for(int t = 1; t <= ntest; t++){
		int number = 0;
		fin >> a >> b;
		for(int i = a; i <= b; i++){
			int sodung =0;
			int m[10];
			int mang[10], mang2[10];
			int len = 0;
			int n = i;
			while(n){
				mang[len] = n%10;
				n = n/10;
				len++;
			}
			for(int j = len -1; j >=0; j--)
				mang2[j] = mang[len -1 - j];
			
			for(int j = 1; j <= len -1; j++){
				int flag = 0;
				int rec = 0;
				
				for(int k = 0; k < len; k++){
					rec = rec*10 + mang2[(k+ j)%len];
				}
				
				for(int l = 1; l <= sodung; l++){
					if(rec == m[l])
						flag = 1;	
				}
				 
				if( rec > i && rec <= b && rec >= a && flag == 0){
					number++;
					sodung++;
					m[sodung] = rec;
				}
			}
		}
		
		fout << "Case #" << t << ": " << number << endl;
	}
	getch();
	return 0;
}
