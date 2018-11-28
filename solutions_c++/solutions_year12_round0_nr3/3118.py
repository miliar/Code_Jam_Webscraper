#include <iostream>
#include <string>
#include <cctype>
#include <fstream>
#include <cmath>

using namespace std;

int main(){
	int T;
	ifstream ifs; 
	ifs.open("C-small-attempt0.in");
	ofstream ofs;
	ofs.open("solution.out");;
	int cas = 1;
	ifs>>T;
	while(cas <= T){
		int A, B;
		ifs>>A>>B;
		int count = 0;
		ofs<<"Case #"<<cas++<<": ";
		for(int i=A; i<B;i++){
			int digitcount =0;
			if(i<=99)
				digitcount = 2;
			else if(i<=999)
				digitcount = 3;
			else if(i<=9999)
				digitcount = 4;
			else if(i<=99999)
				digitcount = 5;
			else if(i<=999999)
				digitcount = 6;
			else if(i<=2000000)
				digitcount = 7;
				
			int attemp = 1;
			int divFactor = 10;
			int mulFactor = (int)pow((int)10,digitcount-1);
			int c = i;
			//ofs<<i<<"  ";
			while(attemp<digitcount){
				int rem = c%divFactor;
				int d = c /divFactor;
				d = rem * mulFactor + d;
				//cout<<"Attemp = "<<attemp<<" Digcount = "<<digitcount<<" rem "<<rem<<"  d "<<d<<endl; 
				if(d>i && d<= B){
					count++;
					//ofs<<d<<"  ";
				}
				attemp++;
				divFactor *= 10;
				mulFactor /= 10;
			}
			//ofs<<endl;
		}
		ofs<<count<<endl;
	}
	return 0;
}

	