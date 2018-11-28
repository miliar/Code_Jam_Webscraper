#include <iostream>
#include <string>
#include <cmath>
using namespace std;

struct State{
	int location;
	int time;
};

int main() {
	int numTests;
	cin>>numTests;
	string ignore;
	getline(cin,ignore);
	for(int test=0;test<numTests;test++){
		cout<<"Case #"<<(test+1)<<": ";
		int totalTime=0;
		State orange;
		orange.location=1;
		orange.time=0;
		State blue;
		blue.location=1;
		blue.time=0;
		int numButtons;
		cin>>numButtons;
		for(int i=0;i<numButtons;i++){
			int loc;
			char bot;
			cin>>bot;
			cin>>loc;
			if(bot=='O'){
				int dist = abs(orange.location - loc);
				if(dist>orange.time){
					totalTime+=dist-orange.time;
					blue.time+=dist-orange.time;	
				}
				totalTime++;
				orange.time=0;
				orange.location=loc;
				blue.time++;
			}
			else{
				int dist = abs(blue.location - loc);
				if(dist>blue.time){
					totalTime+=dist-blue.time;
					orange.time+=dist-blue.time;			
				}
				totalTime++;
				blue.time=0;
				blue.location=loc;
				orange.time++;				
			}
		}
		cout<<totalTime<<endl;
	}
}
