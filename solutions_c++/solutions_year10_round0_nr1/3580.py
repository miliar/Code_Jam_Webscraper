#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;


int main()
{
	ifstream fi("credit.in");
	ofstream fo("credit.out");
	int t, n, k;
	fi>>t;
	for(int m=1; m<=t; m++)
	{
		fo<<"Case #"<<m<<": ";
		fi>>n>>k;
		int period=(int)pow(2.0,n);
		k=k%period;
		if(k==period-1)	fo<<"ON"<<endl;
		else fo<<"OFF"<<endl;
	}
}



