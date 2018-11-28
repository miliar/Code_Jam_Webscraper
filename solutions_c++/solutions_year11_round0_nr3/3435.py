//
//  Candy_Splitting.cpp
//  Candy_Splitting
//
//  Created by Yingzhi Gou on 7/05/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


const char infile[]="/Users/chairdog/Dropbox/2011Qualification/in.txt";
const char outfile[]="/Users/chairdog/Dropbox/2011Qualification/out.txt";

long candySplitting(istream &in){
	long pile1=0, pile2=0, XorP=0, XorAll=0;
	int T;
	vector<long> candy;
	in >> T;
	for (int i=0; i<T; i++) {
		long tmp;
		in>>tmp;
		candy.push_back(tmp);
		XorAll^=tmp;
	}
	sort(candy.begin(), candy.end());
	for (int i=T-1; i>=0; i--) {
		XorAll^=candy[i];
		XorP^=candy[i];
		pile1+=candy[i];
		if (XorAll==XorP) {
			pile2+=candy[i];
			pile1-=candy[i];
		}
		else{
			XorAll^=candy[i];
			XorP^=candy[i];
		}
	}
	if (XorAll==0) {
		pile2-=candy[0];
	}
	return pile2;
}

void stuff(istream &in, ostream &out){
	int n;
	in>>n;
	for (int i=0; i<n; i++){
		long result=candySplitting(in);
		out << "Case #" << i+1 << ": ";
		if (result>0) {
			out << result;
		}
		else{
			out << "NO";
		}
		out << endl;
	}
}

int main (int argc, const char * argv[])
{
	ifstream inf;
	ofstream outf;
	inf.open(infile);
	outf.open(outfile);
	stuff(inf, outf);
	inf.close();
	outf.close();
    return 0;
}



