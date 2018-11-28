#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include "parseFile.h"

using namespace std;


int main(int argc, char* argv[]) {
	int T=0, N=0, C=0;

	ofstream of("C-large.out");

	parseFile pa(argv[1]);//"input.txt");
	pa.nextLineSStream();
	pa.os>>T;

	int caseNum=1;
	while(caseNum<=T){
		pa.nextLineSStream();
		pa.os>>N;
		of<<"Case #"<<caseNum<<": ";

		pa.nextLineSStream();
		int min=2*pow(10,6), sum=0, wrongSum=0;

		while(pa.os>>C){
			wrongSum ^= C;
			sum+=C;
			if(min>C)min=C;
		}
		pa.os.clear();

		if(wrongSum!=0){
			of<<"NO"<<endl;
		}else{
			of<<sum-min<<endl;
		}

		caseNum++;
	}

	of.close();
	return 0;
}

