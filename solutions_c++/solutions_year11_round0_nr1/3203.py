#include <iostream>
#include <vector>
#include <algorithm>
#include "parseFile.h"

using namespace std;


int main(int argc, char* argv[]) {
	int T=0, N=0;
	int Pi, Pi0, PO=1, PB=1;
	char Ri, R0;
	int duration=0;

	ofstream of("A-large.out");

	parseFile pa(argv[1]);//"input.txt");
	pa.nextLineSStream();
	pa.os>>T;

	int caseNum=1;
	while(caseNum<=T){
		PO=PB=1;
		duration=0;
		int subDur=0;
		pa.nextLineSStream();
		pa.os>>N;
		while(pa.os>>Ri){
			pa.os>>Pi;
			if(Ri=='O'){
				Pi0=PO;
				PO=Pi;
			}
			else{
				Pi0=PB;
				PB=Pi;
			}

			int step=abs(Pi-Pi0)+1;
			if(duration==0)
				R0=Ri;
			if(R0==Ri){
				duration+=step;
				subDur+=step;
			}
			else{//switch to another robot:
				if(subDur>step-1)
					subDur=1;
				else
					subDur=step-subDur;

				duration+=subDur;
			}
			R0=Ri;
		}
		of<<"Case #"<<caseNum<<": "<<duration<<endl;
		caseNum++;
		pa.os.clear();
	}

	of.close();

}

