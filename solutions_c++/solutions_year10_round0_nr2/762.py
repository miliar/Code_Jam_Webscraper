#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#define _INPUT_FILE_PATH "G:\\B-small-attempt3.in"
#define _OUTUT_FILE_PATH "G:\\B-small-attempt3.out"
//#define _INPUT_FILE_PATH "G:\\B-tiny.in"
//#define _OUTUT_FILE_PATH "G:\\B-tiny.out"

// compiled on visual studio 2010

using namespace std;

unsigned int cases;
unsigned int pow10[9] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000 };
unsigned int pow2[32] = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648};

void readinputfile();
unsigned int str2int(string s) { unsigned int i=0,C=s.length(); for (unsigned int c=0;c<C;c++) i += (s[C-c-1]-'0')*pow10[c]; return (i); }
unsigned int gcd(unsigned int m,unsigned int M) { 
	unsigned int k;
	for(k=0; M>m; M-=m, k++);
		if(m>M) return(gcd(M,m));
		else return(m);
};

void main() {
	ifstream inputfile; ofstream outputfile;
	inputfile.open(_INPUT_FILE_PATH); outputfile.open(_OUTUT_FILE_PATH);
	if (inputfile.is_open() && outputfile.is_open())
	{
		string inputline;
		getline(inputfile,inputline,'\n'); cases = str2int(inputline);
		for (unsigned int c=1; c<=cases; c++) {
			unsigned int *ge = new unsigned int[1000];
			getline(inputfile,inputline,' '); unsigned int n = str2int(inputline);
			for (unsigned int ni=0; ni<n; ni++) {
				if (ni+1<n) getline(inputfile,inputline,' ');
				if (ni+1==n) getline(inputfile,inputline,'\n');
				ge[ni] = str2int(inputline);
			}

			// arraysort&cleanup
			for (unsigned int ni=0; ni+1<n; ni++) {
				for (unsigned int nii=0; nii+ni+1<n; nii++) {
					if (ge[nii]>ge[nii+1]) {
						unsigned int getemp=ge[nii]; ge[nii]=ge[nii+1]; ge[nii+1]=getemp;
					}
				}
			}

			unsigned int *ged = new unsigned int[999];
			for (unsigned int ni=0; ni+1<n; ni++) { ged[ni]=ge[ni+1]-ge[ni]; }

			// arraysort
			for (unsigned int ni=0; ni+2<n; ni++) {
				for (unsigned int nii=0; nii+ni+2<n; nii++) {
					if(ged[nii]>=ged[nii+1]) {
						unsigned int gedtemp=ged[nii]; ged[nii]=ged[nii+1]; ged[nii+1]=gedtemp;
					}
				}
			}

			//for (unsigned int ni=0; ni+1<n; ni++) { cout << " " << ged[ni]; } cout << endl;

			// greatest common divisor
			unsigned int ni0=0; unsigned int pairgcd=ged[ni0];
			while(pairgcd==0) { ni0++; pairgcd=ged[ni0]; }
			for (unsigned int ni=ni0; ni+2<n; ni++)
				pairgcd = gcd(pairgcd,ged[ni+1]);

			outputfile << "Case #" << c << ": " << (ge[0]%pairgcd>0?pairgcd-ge[0]%pairgcd:0) << endl;
		}
		inputfile.close(); outputfile.close();
	}
	else cout << "couldn't open file" << endl;
}


