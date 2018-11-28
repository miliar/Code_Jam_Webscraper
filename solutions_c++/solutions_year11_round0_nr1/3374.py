//
//  BotTrust.cpp
//  code jam 2011
//
//  Created by Yingzhi Gou on 7/05/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

const char infile[]="/Users/chairdog/Downloads/A-large.in.txt";
const char outfile[]="/Users/chairdog/Dropbox/2011Qualification/out.txt";


int botTrust(istream &in, ostream &out){
	int n;
	in>>n;
	int timeB=0, Bwait=0, timeO=0, Owait=0;
	char color;
	int button, lastOButton=1, lastBButton=1;
	for (int i=0; i<n; i++) {
		in>>color>>button;
		if (color=='O') {
			timeO+=(abs(lastOButton-button)>Owait?abs(lastOButton-button)-Owait:0)+1;
			Bwait+=(abs(lastOButton-button)>Owait?abs(lastOButton-button)-Owait:0)+1;
			lastOButton=button;
			Owait=0;
		}
		else{
			timeB+=(abs(lastBButton-button)>Bwait?abs(lastBButton-button)-Bwait:0)+1;
			Owait+=(abs(lastBButton-button)>Bwait?abs(lastBButton-button)-Bwait:0)+1;
			lastBButton=button;
			Bwait=0;
		}
	}
	return timeB+timeO;
}

void stuff(istream &in, ostream &out){
	int n;
	in>>n;
	for (int i=0; i<n; i++) {
		out << "Case #" << i+1 << ": " << botTrust(in, out) << endl;
	}
}

int main (int argc, const char * argv[])
{
	ifstream inf;
	ofstream outf;
	inf.open(infile);
	outf.open(outfile);
	stuff(inf, outf);
    return 0;
}

