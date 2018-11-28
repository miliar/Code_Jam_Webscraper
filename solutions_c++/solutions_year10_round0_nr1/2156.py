#include <fstream>
#include <iostream>
#include <windows.h>
#include <time.h>
#include <string>
#include <math.h> //Because MSVC++ hates the left shift operand >.<
using namespace std;
int main(){
	string inname;
	string outname;
	cout << "Enter file name to read: ";
	getline(cin,inname);
	cout << "\nEnter file name to save: ";
	getline(cin,outname);
	ifstream in(inname.data());
	ofstream out(outname.data(),ios::trunc);
	bool good = true;
	if(!in.is_open()){
		good = false;
		cout << "Could not open file " << inname << " for reading";
	}
	if(!out.is_open()){
		good = false;
		cout << "Could not open file " << outname << " for reading";
	}
	if(!good)
		Sleep(10000000000);
	clock_t st = clock();
	int cases = 0;
	in >> cases;
	for(int casen = 1;casen <= cases;casen++){
		int N,K;
		string answer;
		in >> N;
		in >> K;
		int a = (int)pow(2.0,N);
		int b = K % a;
		if(b == a-1){
			answer = "ON";
		}else{
			answer = "OFF";
		}
		std::cout << "DONE CASE: " << casen << "\n";
		std::cout << "Case #" << casen << ": " << answer << "\n";
		out << "Case #" << casen << ": " << answer << "\n";
	}
	in.close();
	out.close();
	clock_t en = clock();
	cout << "Time: " << ((en-st)/CLOCKS_PER_SEC);
	Sleep(1000000000);
}
