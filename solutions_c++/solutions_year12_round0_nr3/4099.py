#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <stdio.h>
#include <algorithm>
using namespace std;


void main(){
    ifstream fin("input.txt");
    ofstream fout("output.txt");

	
	int n, a, b;
	fin >> n;
	for(int i = 1; i <= n; i++){
		fin >> a >> b;
		int count = 0;


		for(int k = a; k<=b; k++){






			int ct[10], c[10];
			int t = k;
			int z = 0;
			while(t>0){
				ct[z++] = t%10;
				t /= 10;
			}
			int ll = z-1;
			for(int l = 0; l<z; l++) c[l]=ct[ll--];

			for(int l = 1; l < z; l++){
				copy(c, c+z, ct);
				c[0]=ct[z-1];
				for(int p =1; p<z; p++) c[p] = ct[p-1];

				int d= 0;
				int m=1;
				for(int p = z-1; p>=0; p--){
					d += c[p]*m;
					m *= 10;
				}
				if(d>k && d<=b) count++;

			}
			
			


		}

		fout << "Case #" << i << ": " << count << endl;




	}
	
	
    
}