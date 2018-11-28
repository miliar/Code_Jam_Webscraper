/*
 * B.cpp
 *
 *  Created on: 22 mai 2010
 *      Author: Rafael
 */

#include<iostream>
#include<fstream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include <set>
#define DEBUG(x) cout << #x" = " << x << "\n"

using namespace std;

int main(){
	int C;
	cin>>C;
	for(int c = 1;c<=C;c++){
		cout<<"Case #"<<c<<": ";
		double P,L,r,f,a;
		cin>>L>>P>>f;
		r=P/L;
		int ret=0;
		while(r>f+1e-7)
		{
			r=sqrt(r);
			ret++;
		}
		cout<<ret<<"\n";

	}

	return 0;
}
