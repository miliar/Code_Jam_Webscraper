#include <iostream>
#include <vector>
#include <stdlib.h>
using namespace std;

int main(){
	int caseNumber;
	cin >> caseNumber;
	for(int i=0;i<caseNumber;i++){
		int sNumber;
		cin >> sNumber;
		char color[sNumber];
		int bottom[sNumber];
		int step[sNumber];
		int preO=1,preB=1,stepO=0,stepB=0;
		for(int j=0;j<sNumber;j++){
			cin >> color[j] >> bottom[j];
			if(color[j]=='O'){
				step[j]=stepO+abs(bottom[j]-preO)+1;
				preO=bottom[j];
				stepO=step[j];
			}
			else{
				step[j]=stepB+abs(bottom[j]-preB)+1;
				preB=bottom[j];
				stepB=step[j];
			}
			//cout << step[j] << endl;
		}

		int addO=0,addB=0;
		for(int j=0;j<sNumber-1;j++){
			if(color[j]=='O'){
				if(color[j+1]=='B' && ((step[j+1]+addB)<=(step[j]+addO)) ){
					addB=step[j]+addO+1-step[j+1];
				}
				else continue;
			}
			else{
				if(color[j+1]=='O' && ((step[j+1]+addO)<=(step[j]+addB)) ){
					addO=step[j]+addB+1-step[j+1];
				}
				else continue;
			}
		}

		if(color[sNumber-1]=='O')
			cout << "Case #" << i+1 << ": " << step[sNumber-1]+addO << endl;
		else
			cout << "Case #" << i+1 << ": " << step[sNumber-1]+addB << endl;
		
	}
	return 0;
}
