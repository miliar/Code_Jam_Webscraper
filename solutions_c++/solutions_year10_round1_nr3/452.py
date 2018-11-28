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

using namespace std;

class p3{
public:

	void swap(int& i, int& j){
		if(i<j)
			return;

		int tmp=i;
		i=j;
		j=tmp;
	}

	bool test(int i, int j){
		//cout<<"enter test("<<i<<","<<j<<")\n";
		if(i==j){
			//cout<<"fasle\n";
			return false;
		}
		swap(i, j);
		cout<<"test(): " <<i<<" "<<j<<" eee\n";

		if(i==1){
			//cout<<"i==1\n";
			return true;
		}
		if(j%i==0){
			//cout<<"j%i==0\n";
			return true;
		}
		if(j>i*2){
			//cout<<"j>i*2\n";
			return true;
		}

		cout<<"555\n";
		return !test(i, j-i);
	}

	int run(int A1, int A2, int B1, int B2){
		cout<<"entering run(): "<<A1<<" "<<A2<<" "<<B1<<" "<<B2<<endl;

		int count=0;
		for(int i=A1; i<=A2; i++)
			for(int j=B1; j<=B2; j++)
				if (true==test(i,j)){
					cout<<"	run():"<<i<<" "<<j<<endl;
					count++;
				}

		return count;
	}

};

int main(){
	parseFile pf("C-small-attempt0.in");
	ofstream ofile("C-small-attempt1.out");

	int T=0, caseNum=0;
	int A1=0, A2=0, B1=0, B2=0;
	p3 pp3;

	pf.nextLineSStream();
	pf.os>>T;
	cout<<T<<endl;

//	while(caseNum<T){
//		pf.nextLineSStream();
	while(pf.nextLineSStream()){
		caseNum++;
		pf.os>>A1>>A2>>B1>>B2;
		cout<<A1<<" "<<A2<<" "<<B1<<" "<<B2<<endl;

		int count=pp3.run(A1, A2, B1, B2);
		cout<<"Case #"<<caseNum<<": "<<count<<endl;
		ofile<<"Case #"<<caseNum<<": "<<count<<endl;
	}

	ofile.close();
	return 0;
}
