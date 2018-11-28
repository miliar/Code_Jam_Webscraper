#include <iostream>
#include <math.h>
#include <string>
using namespace std;


int main(int argc, char *argv){
	int numCases;
	cin>>numCases;
	for(int c=0;c<numCases;++c){
		int len;
		cin>>len;
		char prev=' ';
		int t=0;
		int posBlue=1;
		int posOrange=1;
		int orangeWaitTime=0;
		int blueWaitTime=0;
		int totalTime=0;
		for(int i=0;i<len;++i){
			string s;
			int button;
			cin>>s>>button;
			if(s[0]=='O'){
				int d=abs(posOrange-button);
				int extraTime=0;
				if(orangeWaitTime>=d){
					extraTime=1;
				}else{
					extraTime=d-orangeWaitTime+1;
				}
				orangeWaitTime=0;
				posOrange=button;
				totalTime+=extraTime;
				blueWaitTime+=extraTime;
			}else{
				int d=abs(posBlue-button);
				int extraTime=0;
				if(blueWaitTime>=d){
					extraTime=1;
				}else{
					extraTime=d-blueWaitTime+1;
				}
				blueWaitTime=0;
				posBlue=button;
				totalTime+=extraTime;
				orangeWaitTime+=extraTime;
			}
		}
		cout<<"Case #"<<c+1<<": "<<totalTime<<endl;
	}
	return 0;
}
