#include <iostream>
#include <fstream>
using namespace std;
struct twi{
	int x;
	int y;
};
int main(){
	ifstream dataInput("A-large.in");		//input data stream
	ofstream dataOutput("try.out");		//output data stream

	int T = 0;		//the number of test cases
	dataInput>>T;
	for(int i=1;i<=T;i++){
		int N = 0;
		dataInput>>N;

		twi * data ;
	  	data = new twi[N];
		for(int j=0;j<N;j++){
			dataInput>>data[j].x>>data[j].y;
		}
	
		int times = 0;
		for(int m=0;m<N-1;m++){
			for(int n=m+1;n<N;n++){
				if((data[m].x-data[n].x)*(data[m].y-data[n].y)<0)
					times++;
			}
		}

		dataOutput<<"Case #"<<i<<": "<<times<<endl;

		delete data;
	}		
}
