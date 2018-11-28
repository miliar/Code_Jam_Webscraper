#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <stdio.h>
#include <tr1/tuple>

#define ON true
#define OFF false

int main() {
	//typedef std::tr1::tuple<int,int> Intpl;

	std::ifstream in;
	in.open("A-small.in");
	std::fstream out;
	out.open("A-small.out", std::ios::out);
	if(!in.is_open() || !out.is_open()) {
		std::cout << "Lese-/Schreibfehler: Datei" << std::endl;
		return 0;
	}
	std::string line;
	std::getline(in, line);
	int T = atoi(line.c_str());
	std::vector<bool> snappers;
	//std::vector<Intpl> nk;
	for(int t = 0; t < T; t++) {
		snappers.push_back(ON);
		std::getline(in, line);
		int br = line.find(' ');
		int N = atoi(line.substr(0,br).c_str());
		int K = atoi(line.substr(br+1).c_str());
		//Intpl p = std::tr1::make_tuple(N,K);
		//nk.push_back(p);
		for(signed int i = 0; i < N; i++)
			snappers.push_back(OFF);
		for(int k = 0; k < K; k++) {
			/* snip */
			for(unsigned int i = snappers.size()-1; i > 0; i--) {
				bool strom = true;
				for(unsigned int j = 1; i-j > 0; j++)
					if(!snappers[i-j]) strom = false;
				if(strom) 
					snappers[i] = !snappers[i];
			}
		}
		bool strom = true;
		for(unsigned int j = 1; snappers.size()-j > 0; j++)
			if(!snappers[snappers.size()-j]) strom = false;
		std::string light;
		if(strom)
			light = "ON";
		else
			light = "OFF";

		out << "Case #" << t+1 << ": " << light << std::endl;
		std::cout << "Case #" << t+1 << ": " << light << std::endl;
		
		snappers.erase(snappers.begin(),snappers.end());
	}
	return 0;
}