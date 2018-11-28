#include <fstream>
#include <iostream>
#include <windows.h>
#include <time.h>
#include <string>
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
		int R,k,N,answer;
		in >> R;
		in >> k;
		in >> N;
		int* riders = new int[N];
		int sum = 0;
		for(int i = 0;i < N;i++){
			in >> riders[i];
			sum += riders[i];
		}
		if(sum < k){
			answer = sum * R;
		}else{
			answer = 0;
			int ptr = 0;
			for(int ride = 0;ride < R;ride++){
				int cap = k;
				int next = riders[ptr];
				while(cap >= next){
					cap = cap - next;
					ptr = (ptr + 1) % N;
					next = riders[ptr];
				}
				answer += (k-cap);
			}
		}
		std::cout << "DONE CASE: " << casen << "\n";
		std::cout << "Case #" << casen << ": " << answer << "\n";
		out << "Case #" << casen << ": " << answer << "\n";
	}
	clock_t en = clock();
	cout << "Time: " << ((en-st)/CLOCKS_PER_SEC);
	Sleep(1000000000);
}
