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

	int n, g, s, p, t;
	fin >> n;
	for(int i = 1; i<=n; i++){

		int res = 0;

		fin >> g >> s >> p;
		
		for(int j = 1; j<=g; j++){
			fin >> t;
			if(p==0) res++;
			else{
			if(t>0){

				if(t/p >= 3) res++;
				else{
					int pt = p - ((t-p)/2);
						if(pt==2 && s>0){
							res++;
							s--;
						}
						else if(pt==1) res++;
				}
			}
			}

		}

		fout << "Case #" << i << ": " << res << endl;
	}

    
}