#include <iostream>
#include <fstream>
using namespace std;
bool check(long long k,int n){
    for(int i = 0; i < n; i++){
        if(k % 2 == 0) return false;
        k = (k >> 1);
    }
    return true;
}
int main(){
	ifstream in("input.txt");
	ofstream out("out.txt");
	int cases = 0;
	in >> cases;
	long long  n = 0;
	long long  k = 0;
	int no = 1;
	for(;no<= cases;no++){
	    //cout << no << endl;
		in >> n >> k;
		//cout << k << endl;
		out << "Case #" << no << ": ";
		if(check(k,n)) out << "ON";
		else out << "OFF";
		out << endl;
	}
	return 0;
}
