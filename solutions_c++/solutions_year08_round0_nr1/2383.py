#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <set>

int main() {
	int N,Q,S;
	std::cin>>N;
	std::string szEnd;
	std::getline(std::cin,szEnd);
	for (int nCase=1; nCase<=N; nCase++) {
		std::cin>>S;
		std::getline(std::cin,szEnd);
		std::set<std::string> sEngines;
		for (int i=0; i<S; i++) {
			std::string szLine;
			std::getline(std::cin,szLine);
			sEngines.insert(szLine);
		}
		int nSwitches=0;
		std::set<std::string> sHad;
		std::cin>>Q;
		std::getline(std::cin,szEnd);
		for (int i=0; i<Q; i++) {
			std::string szLine;
			std::getline(std::cin,szLine);
			std::pair<std::set<std::string>::iterator,bool> res=sHad.insert(szLine);
			if (res.second && sHad.size() >= sEngines.size()) {
				sHad.clear();
				sHad.insert(szLine);
				nSwitches++;
			}
		}
		std::cout<<"Case #"<<nCase<<": "<<nSwitches<<std::endl;
	}
	return 0;
}