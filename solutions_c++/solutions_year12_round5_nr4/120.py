#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

const char special[8]={'o', 'i', 'e', 'a', 's', 't', 'b', 'g'};
long long powers[61];

int main(){
	ifstream fin ("g123d.in");
	ofstream fout ("g123d.out");
	powers[0]=1;
	for(int n=1; n<=60; n++)
		powers[n]=powers[n-1]*2;
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int subLength;
		fin>>subLength;
		string str;
		fin>>str;
		int length=str.size();
		vector<int> ins[5000], outs[5000];
		int numSpecial[5000];
		int current=0;
		for(int n=0; n<length-subLength+1; n++){
			int next=n+1;
			for(int i=0; i<=n; i++){
				if(str.compare(n+1, subLength-1, str, i, subLength-1)==0){
					next=i;
					break;
				}
			}
			bool found=false;
			for(unsigned int i=0; i<outs[current].size(); i++)
				if(outs[current][i]==next){
					found=true;
					break;
				}
			if(!found){
				outs[current].push_back(next);
				ins[next].push_back(current);
			}
			current=next;
		}
		for(int n=0; n<length-subLength+2; n++){
			if(ins[n].size()==0 && outs[n].size()==0)
				continue;
			numSpecial[n]=0;
			for(int i=0; i<subLength-1; i++)
				for(int j=0; j<8; j++){
					if(str[n+i]==special[j])
						numSpecial[n]++;
				}
			//cout<<str.substr(n, subLength-1)<<" "<<ins[n].size()<<" "<<outs[n].size()<<" "<<numSpecial[n]<<endl;
		}
		long long numEdges=0, numPaths=0;
		for(int n=0; n<length-subLength+2; n++){
			if(ins[n].size()==0 && outs[n].size()==0)
				continue;
			long long numIn=0, numOut=0;
			for(unsigned int i=0; i<ins[n].size(); i++)
				numIn+=powers[numSpecial[ins[n][i]]];
			for(unsigned int i=0; i<outs[n].size(); i++)
				numOut+=powers[numSpecial[outs[n][i]]];
			numEdges+=numOut*powers[numSpecial[n]];
			if(numOut>numIn)
				numPaths+=(numOut-numIn)*powers[numSpecial[n]];
		}
		//cout<<numEdges<<" "<<numPaths<<endl;
		if(numPaths==0)
			numPaths=1;
		fout<<"Case #"<<caseNum+1<<": "<<numPaths*(subLength-1)+numEdges<<endl;
	}
	return 0;
}
