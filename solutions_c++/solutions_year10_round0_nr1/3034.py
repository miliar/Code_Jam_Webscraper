#include <math.h>
#include <fstream>

using namespace std;

int main(){
	ifstream file;
	ofstream output;
	file.open("A-large.in");
	output.open("A-large.out");

	int i,cases, snappers,snaps,needed;
	file >> cases;
	for(i=1;i<=cases;i++){
		file >> snappers;
		file >> snaps;
		needed = pow(2,snappers);
		output << "Case #" << i << ": " << (((snaps % needed)==(needed-1)) ? "ON" : "OFF") << endl;
	}
	file.close();
	output.close();

	return 0;
}

