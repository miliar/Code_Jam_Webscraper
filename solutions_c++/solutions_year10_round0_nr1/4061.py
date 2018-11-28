/*
 * A.cpp
 *
 *  Created on: May 8, 2010
 *      Author: amr
 */
#include <iostream>
#include <fstream>
#include <iomanip>


using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("large.out");

	int t;
	fin>>t;

	int n,k,count,power;
	int case_num = 0;


	while(t--){

		case_num++;
		fin>>n>>k;
		power =(1<<n);
		count = power -1;
		if((k%power)==(count%power))fout<<"Case #"<<case_num<<": ON"<<endl;
		else fout<<"Case #"<<case_num<<": OFF"<<endl;

	}
	fout.close();

	return 0;
}
