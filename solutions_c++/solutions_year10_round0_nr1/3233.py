/* 
 * File:   newmain.cpp
 * Author: srikanth1
 *
 * Created on 4 May, 2010, 11:23 AM
 */
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <math.h>
#include <stdlib.h>
using namespace std;
/*
 * 
 */


int main(int argc, char** argv) {

    ifstream in;
    in.open(argv[1]);
    if(!in) {
        cout <<"Error opening file!";
        exit(1);
    }

    int ntestcases;

    in >> ntestcases;
    for(int i=0; i<ntestcases; i++) {
      int N,K,j,rem;
	in >> N >> K;
	j = (int) pow(2,N);
	rem = K%j;
	if(rem == j-1) cout << "Case #"<<i+1<<": "<<"ON\n";
	else cout << "Case #"<<i+1<<": "<<"OFF\n";    
     }

    return (EXIT_SUCCESS);
}

