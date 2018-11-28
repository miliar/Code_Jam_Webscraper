#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<string>

#include "GoogleDancers.h"
using namespace std;

int main()
{
	ifstream infile;
	infile.open ("B-large.in", ifstream::in);
	
	ofstream outfile;
	outfile.open("B-large.out", ofstream::out);

    int nQuestion;
    vector<GoogleDancers> vQuestions;

	infile >> nQuestion;
	infile.ignore();

    for( int i=0; i<nQuestion; i++ ){
		GoogleDancers googleDancers;
		infile >> googleDancers.m_nTestData;
		infile >> googleDancers.m_nSurprising;
		infile >> googleDancers.m_iBestResult;
		for( int j=0; j<googleDancers.m_nTestData; j++){
			int iTestData;
			infile >> iTestData;
			googleDancers.m_vDancerScores.push_back( iTestData );
		}

		vQuestions.push_back( googleDancers );
    }

	for( int i=0; i<nQuestion; i++){
		outfile << "Case #" << i+1 << ": ";
		GoogleDancers& googleDancers = vQuestions.at(i);
		outfile << googleDancers.getAnswer();
		outfile << endl;
	}

	infile.close();
	outfile.close();


}
