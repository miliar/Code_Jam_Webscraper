#include <fstream>
#include <iostream>
#include <windows.h>
#include <time.h>
#include <string>
#include <math.h> //Because MSVC++ hates the left shift operand >.<
using namespace std;
long main(){
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
	long cases = 0;
	in >> cases;
	for(long casen = 1;casen <= cases;casen++){
		long N,answer;
		in >> N;
		long* data = new long[N];
		for(long i = 0;i < N;i++){
			in >> data[i];
		}
		long* numbs = new long[N-1];
		for(long ii = 0;ii < N-1;ii++){
			numbs[ii] = abs(data[ii]-data[ii+1]);
		}
		long GCF = numbs[0];
		for(long iii = 0;iii < N-2;iii++){
			long dive = GCF;
			long divi = numbs[iii+1];
			if(divi == 0) //WTF? It happens D:
				continue;
			long r = dive%divi;
			while(r != 0){
				dive = divi;
				divi = r;
				r = dive%divi;
			}
			GCF = divi;
		}
		answer = GCF - (data[0] % GCF);
		if(answer == GCF){
			answer = 0;
		}
		std::cout << "Completed " << casen << "\n";
		out << "Case #" << casen << ": " << answer << "\n";
	}
	in.close();
	out.close();
	clock_t en = clock();
	cout << "Time: " << ((en-st)/CLOCKS_PER_SEC);
	Sleep(1000000000);
}
