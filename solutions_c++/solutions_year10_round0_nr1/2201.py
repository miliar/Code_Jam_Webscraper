/*
 * prob3.cpp
 *
 *  Created on: 2010-5-7
 *      Author: xhd
 */
#include <iostream>
#include <vector>
#include <fstream>
#include "parseFile.h"
#include "calSnapperChain.h"

using namespace std;

int main(){
	parseFile pf("A-large.in");
	ofstream ofile("A-large.out");

	int T=0, caseNum=0;
	int N=0, K=0;
	vector<int> tVec();

	pf.nextLineSStream();
	pf.os>>T;
	//cout<<T<<endl;

	//process the vector and calculate the case:
	calSnapperChain CSC;
	CSC.run();

	//while(caseNum<T){ pf.nextLineSStream();
	while(pf.nextLineSStream()){
		caseNum++;
		pf.os>>N>>K;
		//cout<<N<<" "<<K<<endl;
		//cout<<"Case #"<<caseNum<<": ";
		ofile<<"Case #"<<caseNum<<": ";
		if(calSnapperChain::ON == CSC.calStat(N, K)){
			//cout<<"ON"<<endl;
			ofile<<"ON"<<endl;
		}else{
			//cout<<"OFF"<<endl;
			ofile<<"OFF"<<endl;
		}
	}
	ofile.close();

	return 0;
}
