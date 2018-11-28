/*
 * p1.cpp
 *
 *  Created on: 2012-4-14
 *      Author: xhd
 */

#include <iostream>
#include "parseFile.h"

using namespace std;

bool bGoodResult(int& S, int& p, int& scoreSum, bool& bsurprise){
	int average=scoreSum/3;
	int remainder=scoreSum%3;

	bsurprise=false;
	if(average>=p)
		return true;
	if(remainder==1){
		return (average+1>=p);
	}
	if(remainder==2 && average+1>=p)
		return true;

	bsurprise=true;
	if(remainder==0){
		if(average==0)
			return average>=p;
		else
			return (average+1>=p);

	}else //remainder==2
		return (average+2>=p);
}

int main(int argc, char** argv){
	if(argc<2){
		cout<<"Please input data: "<<endl;
	}

	int T, N, S, p;
	int i=0,j=0,k=0;
	int count=0, t;
	bool bSurprise=false;

	parseFile pf(argv[1]);
	pf.nextLineSStream();
	pf.os>>T;
	while(i++<T){
		pf.nextLineSStream();
		pf.os>>N>>S>>p;
		for(j=0; j<N; j++){
			pf.os>>t;
			if(bGoodResult(S,p,t, bSurprise)){
				if(bSurprise){
					S--;
					if(S<0)continue;
				}
				count++;
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
		count=0;
	}

	return 0;
}
