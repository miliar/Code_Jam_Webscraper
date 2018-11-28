#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ofstream fout ("g10qc.out");
	ifstream fin ("g10qc.in");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int numGroups, reached[1000], cur=0, loop=-1;
		long long numRuns, cap, groups[1000], riders[1001], total=0, initialRiders=0, initialRuns=0, loopRiders=0, loopRuns=0;
		fin>>numRuns>>cap>>numGroups;
		for(int n=0; n<numGroups; n++){
			fin>>groups[n];
			reached[n]=-1;
		}
		for(long long runs=0; runs<numRuns; runs++){
			if(reached[cur]!=-1){
				loop=cur;
				initialRuns=reached[cur];
				riders[runs]=-1;
				break;
			}
			reached[cur]=runs;
			riders[runs]=0;
			for(int n=0; n<numGroups; n++){
				if(riders[runs]+groups[cur]>cap)
					break;
				riders[runs]+=groups[cur];
				cur++;
				if(cur==numGroups)
					cur=0;
			}
			//cout<<runs<<" "<<cur<<" "<<riders[runs]<<endl;
			total+=riders[runs];
		}
		if(loop==-1){
			fout<<"Case #"<<caseNum+1<<": "<<total<<endl;
			continue;
		}
		for(int n=0; n<initialRuns; n++)
			initialRiders+=riders[n];
		for(int n=initialRuns; riders[n]!=-1; n++){
			loopRuns++;
			loopRiders+=riders[n];
		}
		//cout<<initialRuns<<" "<<initialRiders<<" "<<loopRuns<<" "<<loopRiders<<endl;
		total=initialRiders;
		numRuns-=initialRuns;
		total+=(numRuns/loopRuns)*loopRiders;
		numRuns%=loopRuns;
		for(int n=initialRuns; n<initialRuns+numRuns; n++)
			total+=riders[n];
		fout<<"Case #"<<caseNum+1<<": "<<total<<endl;
	}
	return 0;
}
