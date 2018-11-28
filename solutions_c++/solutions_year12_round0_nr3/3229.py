#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<string>

#include "RecycleNumbers.h"

using namespace std;

int main()
{
	ifstream infile;
	infile.open ("C-small-attempt0.in", ifstream::in);
	
	ofstream outfile;
	outfile.open("C-small-attempt0.out", ofstream::out);

    int nQuestion;
    vector<RecycleNumbers> vQuestions;

	infile >> nQuestion;
	infile.ignore();

    for( int i=0; i<nQuestion; i++ ){
		RecycleNumbers recycleNumbers;
		infile >> recycleNumbers.m_iMin;
		infile >> recycleNumbers.m_iMax;
		vQuestions.push_back( recycleNumbers );
    }

	for( int i=0; i<nQuestion; i++){
		outfile << "Case #" << i+1 << ": ";
		RecycleNumbers& recycleNumbers = vQuestions.at(i);
		outfile << recycleNumbers.getAnswer();
		outfile << endl;
	}

	infile.close();
	outfile.close();


}
