#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;


int main(int argc, char **argv){
	ifstream ifs(argv[1]);
	
	int T;
	ifs>>T;

	int times=0;
	while(T--){
		++times;
		int N;
		ifs>>N;
		
		int blue=1, orange=1;
		int blueTime=0, orangeTime=0;
		while(N--){
			char c;
			int pos;
			ifs>>c>>pos;
			if(c=='O'){
				orangeTime+= abs(pos-orange);
				orange=pos;
				orangeTime = max( blueTime, orangeTime)+1;
			}
			else if(c=='B'){
				blueTime+= abs(pos-blue);
				blue=pos;
				blueTime = max( blueTime, orangeTime)+1;
			}
		}
		cout<<"Case #"<<times<<": "<<max(orangeTime, blueTime)<<endl;
	}
	return 0;
}
