/*
 * SnapperChain.c
 *
 *  Created on: May 8, 2010
 *      Author: wen
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
#include "SnapperChain.h"

using namespace std;

int main()
{
	ifstream input("D:\\eclipseWorkspace\\SnapperChain\\A-large.in");
	ofstream output("D:\\eclipseWorkspace\\SnapperChain\\A-large.out");
	if (!input)
	{
		cout<<"cannot find file!";
	}

	int T;
	input>>T;//No. of test cases
	int N;//No. of Snappers
	int K;//No. of snaps

	int maxSnap;// maxSnap=2^N

	bool status;

	for(int i=1;i<=T;i++)
	{
		input>>N>>K;

		maxSnap=pow(2,N);

		status=((K%maxSnap)==(maxSnap-1));

		//cout<<maxSnap<<" "<<K<<endl;



		if (status)
			output<<"Case #"<<i<<": "<<"ON"<<endl;
		else
			output<<"Case #"<<i<<": "<<"OFF"<<endl;
	}
	input.close();
	output.close();

}
