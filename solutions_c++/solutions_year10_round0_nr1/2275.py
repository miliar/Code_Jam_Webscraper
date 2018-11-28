#include <iostream>
#include <fstream>
using namespace std;

int main(){
	int T, N, K;
	ifstream in("A-large.in");
	in >> T;
	ofstream out("out.txt");
	for(int i = 1; i <= T; i++){
		in >> N >> K;
		out << "Case #" << i << ": ";
		if((K&((1<<N)-1)) == ((1<<N)-1)) out << "ON" << endl;
		else out << "OFF" << endl;
	}
	return 0;
}