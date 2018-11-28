#include <iostream>
#include <fstream>
using namespace std;

int n,k;
int divor[31];
int main(){
	int countx = 1;
	int t;
	divor[0] = 0;
	divor[1] = 2;
	for(int i = 2; i != 31; ++i)
		divor[i] = 2 * divor[i-1];
	ifstream ifs("in.txt");
	ofstream ofs("out.txt");
	ifs>>t;
	while(t--){
		ifs>>n>>k;
		ofs<<"Case #"<<countx<<": ";
		int left = k % divor[n];
		if(left == (divor[n] - 1)){
			ofs<<"ON"<<endl;
		}else{
			ofs<<"OFF"<<endl;
		}
		++countx;
	}
	ofs.close();
	ifs.close();
	return 0;
}