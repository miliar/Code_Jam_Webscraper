//
//  main.cpp
//  FreeCell Statistics
//
//  Created by Yingzhi Gou on 21/05/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const char infile[]="/Users/chairdog/Dropbox/2011codeJam/code jam 2011/FreeCell Statistics/in.txt";
const char outfile[]="/Users/chairdog/Dropbox/2011codeJam/code jam 2011/FreeCell Statistics/out.txt";


string freeCell(istream &in){
	int pd, pg;
	long n;
	in >> n >> pd >> pg;
	//cout << n << " "  << pd << " " << pg << endl;
	if ((pg==100&&pd!=100)||(pg==0&&pd>0)||(n==1&&(pd!=0&&pd!=100))) {
		return "Broken";
	}
	if ((pd==0)) {
		return "Possible";
	}
	for (long i=1; i<=n; i++){
		for (long j=1; j<=i; j++){
			if (i*pd%100==0&&i*pd/100==j) {
				return "Possible";
			}
		}
	}
	return "Broken";
}


void stuff(istream &in, ostream &out){
	int T;
	in>>T;
	for (int i=0; i<T; i++){
		out << "Case #" << i+1 << ": " << freeCell(in)<< endl;
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

