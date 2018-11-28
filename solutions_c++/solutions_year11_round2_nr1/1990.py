//
//  RPI.cpp
//  RPI
//
//  Created by Yingzhi Gou on 22/05/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

const char infile[]="/Users/chairdog/Dropbox/2011codeJam/code jam 2011/RPI/in.txt";
const char outfile[]="/Users/chairdog/Dropbox/2011codeJam/code jam 2011/RPI/out.txt";


void RPI(istream &in, ostream &out){
	int n;
	vector<string> raw;
	vector<long double> wp, owp, oowp;
	string tmp;
	in>>n;
	for	(int i=0; i<n; i++){
		in>>tmp;
		int win=0, loss=0;
		for (int j=0; j<n; j++){
			if (tmp[j]=='1'){
				win++;
			}
			else if(tmp[j]=='0'){
				loss++;
			}
		}
		wp.push_back((double)win/(win+loss));
		//debug
		cout << "wp "<< wp[i] << endl;
		raw.push_back(tmp);
	}
	
	for (int i=0; i<n; i++) {
		double tmpowp=0.0;
		int opps=0;
		for (int j=0; j<n; j++) {
			if (raw[i][j]!='.') {
				int win=0, loss=0;
				for (int k=0; k<n; k++){
					if (k!=i){
						if(raw[k][j]=='1'){
							win++;
						}
						else if(raw[k][j]=='0'){
							loss++;
						}
					}
				}
				opps++;
				tmpowp+=(double)loss/(double)(win+loss);
			}
		}
		tmpowp=tmpowp/opps;
		owp.push_back(tmpowp);
		//debug
		cout << "owp " <<owp[i] << endl;
	}
	for (int i=0; i<n; i++) {
		double tmpoowp=0.0;
		int opps=0;
		for (int j=0; j<n; j++) {
			if (raw[i][j]!='.') {
				tmpoowp+=owp[j];
				opps++;
			}
		}
		tmpoowp=tmpoowp/opps;
		oowp.push_back(tmpoowp);
	}

	
	for (int i=0; i<n; i++) {
		long double rpi=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
		out << rpi << endl;
		//debug
		cout << rpi << endl;
	}
	
}

void stuff(istream &in, ostream &out){
	int T;
	in>>T;
	for (int i=0; i<T; i++){
		out << "Case #" << i+1 << ": " << endl;
		RPI(in, out);
		//out << endl;
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
