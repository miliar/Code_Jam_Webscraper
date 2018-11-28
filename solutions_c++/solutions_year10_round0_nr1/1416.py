// qualification_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <bitset>
#include <fstream>
#include <vector>
using namespace std;

int main(int argc, char* argv[])
{
	int state;
	bitset<32> b;
	int n,k,t=0;
	vector<int> n_vec;
	vector<int> k_vec;
    fstream frw("A-large.in",ios::in);
	frw>>t;

	for(int i=0;i<t;i++)
	{
		frw>>n>>k;
		n_vec.push_back(n);
		k_vec.push_back(k);
	}
	frw.close();
	fstream fw;
	fw.open("output.txt",ios::out);
	for(int j=0;j<t;j++)
	{
		state=1;		
	    bitset<32> b(k_vec[j]);
		for(int p=0;p<n_vec[j];p++)
		{
			if(!b.test(p)) {state=0;break;}
				
		}
		fw<<"Case #"<<j+1<<": ";
		if(state==0) fw<<"OFF"<<endl;
		else 		fw<<"ON"<<endl;
	}
	fw.close();
	
	return 0;
}
