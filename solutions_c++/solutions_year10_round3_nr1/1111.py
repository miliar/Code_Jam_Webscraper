/*
 * prob2.cpp
 *
 *  Created on: 2010-5-7
 *      Author: xhd
 */
#include <iostream>
#include <vector>
#include <fstream>
#include "parseFile.h"

using namespace std;

class prob1{
public:
	int run(int N, int*A, int*B){
		int count=0;

		for(int i=0; i<N; i++)
			for(int j=i+1; j<N; j++){
				if( (A[i]-A[j])*(B[i]-B[j])<0 )
					count++;
			}

		return count;
	}

private:
	int Measure;
	int Del;
	int Ins;
};

int main(){
	parseFile pf("A-large.in");
	ofstream ofile("A-large.out");

	int T=0, caseNum=0, tmp;
	int N=0;
	prob1 p1;

	pf.nextLineSStream();
	pf.os>>T;
	cout<<T<<endl;

//	while(caseNum<T){
//		pf.nextLineSStream();
	while(pf.nextLineSStream()){
		caseNum++;
		pf.os>>N;
		cout<<N<<endl;

		int *A=new int[N];
		int *B=new int[N];
		for(int i=0; i<N; i++){
			pf.nextLineSStream();
			pf.os>>A[i]>>B[i];
			cout<<A[i]<<" "<<B[i]<<endl;
		}

		int cost=p1.run(N, A, B);

		cout<<"Case #"<<caseNum<<": "<<cost<<endl;
		ofile<<"Case #"<<caseNum<<": "<<cost<<endl;
	}

	ofile.close();
	return 0;
}
