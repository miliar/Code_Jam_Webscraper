//============================================================================
// Name        : FileFix-it.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int ntc;
	cin >> ntc;

	for(int ci=0;ci<ntc;ci++){
		int N,M;
		int res=0;
		cin >> N >> M;
		vector <string> ex_s;
		string tmp;
		for(int i=0;i<N;i++){
			cin >> tmp;
			ex_s.push_back(tmp);
		}
		for(int i=0;i<M;i++){
			cin >> tmp;
			unsigned int pos=tmp.find('/');;
			while(pos!=string::npos){
				pos=tmp.find('/',pos+1);
				string tmp2=tmp.substr(0,pos);
//				cout << tmp2 << endl;
				bool is_ex=false;
				for(unsigned int j=0;j<ex_s.size();j++){
					if(tmp2.compare(ex_s[j])==0){
						is_ex=true;
						break;
					}
				}
				if(!is_ex){
					ex_s.push_back(tmp2);
					res++;
				}
			}
		}

		cout << "Case #" << ci+1 << ": " << res << endl;
	}
	return 0;
}
