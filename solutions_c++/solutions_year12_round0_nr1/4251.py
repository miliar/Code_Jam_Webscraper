#include <string>
#include <fstream>
#include <iostream>
using namespace std;

char array[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main(){
	int n;
	string trans;
	ifstream derp ("input.txt");
	ofstream out ("output.txt");
	derp >> n;
	getline(derp, trans);
	for(int i = 1; i <= n; i++){
		getline(derp, trans);
		//cout << trans << endl;
		for(int j = 0; j < trans.size(); j++){
			int x = trans[j];
			if(x >= 97 && x <= 122){
				trans[j] = array[x-97];
			}
		}
		out << "Case #" << i << ": " << trans << endl;
	}
	derp.close();
	out.close();
	return 0;
}