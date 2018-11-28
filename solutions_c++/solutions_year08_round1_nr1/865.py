#ifndef __IOSTREAM__ 
#define __IOSTREAM__
#include <iostream>
#include <fstream>
#include <Vector>
#include <List>
#endif

using namespace std;

#define FILENAME  "A-small-attempt1.in"

void sort( vector<int>* a ) {

	int n;
	int k=1;
	for ( int i=(*a).size()-1; i > 0; i-- ) {
		for ( int j=(*a).size()-1; j >= (*a).size()-i; j-- ) {
			if( (*a)[j] > (*a)[j-1] ) {
				n = (*a)[j-1];
				(*a)[j-1] = (*a)[j];
				(*a)[j] = n;
			}
		}
	}
}

void sortf( vector<int>* a ) {

	int n;
	int k=1;
	for ( int i=(*a).size()-1; i > 0; i-- ) {
		for ( int j=(*a).size()-1; j >= (*a).size()-i; j-- ) {
			if( (*a)[j] < (*a)[j-1] ) {
				n = (*a)[j-1];
				(*a)[j-1] = (*a)[j];
				(*a)[j] = n;
			}
		}
	}
}

void main(){

	int n,i,j,k;
	vector<int> a;
	vector<int> b;
	int result;

	ifstream file(FILENAME,ios::in);
	if(file.fail()){
		file.close();
		system("pause");
		exit(0);
	} 
	ofstream ouputfile("output.txt",ios::out);


	file>>n;
	for ( int casenum = 0; casenum < n; casenum++ ) {
		
		a.clear();
		b.clear();
		file>>i;
		for ( j = 0; j < i; j++ ) {
			file>>k;
			a.push_back( k );
		}
		for ( j = 0; j < i; j++ ) {
			file>>k;
			b.push_back( k );
		}
		
		sort(&a);
		sortf(&b);

		result = 0;
		for ( j = 0; j < i; j++ ) {
			result = result + a[j]*b[j];
		}

		ouputfile<<"Case #"<<casenum+1<<": "<<result<<endl;
	}

	ouputfile.close();
	file.close();
}
