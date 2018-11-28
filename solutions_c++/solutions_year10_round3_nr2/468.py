//============================================================================
// Name        : LoadTesting.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;

int main() {
	int ntc;
	cin >> ntc;
	for(int ci=0;ci<ntc;ci++){
		long long L,P,C;
		cin >> L >> P >> C;
		int res=0;
		while(1){
			if (L*C>=P){
				break;
			}
			else{
				long long tmp;
				tmp=sqrt(L)*sqrt(P);
				if(tmp*tmp==L*P)
					P=tmp;
				else
					P=tmp+1;
				res++;
			}
		}
		cout << "Case #"<< ci+1<<": "<< res<<endl;
	}
	return 0;
}
