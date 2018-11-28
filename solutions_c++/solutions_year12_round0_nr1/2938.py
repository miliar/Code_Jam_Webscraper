
#include <iostream>
#include <string>
#include <cctype>
#include <fstream>

using namespace std;

string STR = "yhesocvxduiglbkrztnwjpfmaq ";

int main(){
	int T;
	ifstream ifs; 
	ifs.open("A-small-attempt1.in");
	ofstream ofs;
	ofs.open("solution.out");;
	int cas = 1;
	ifs>>T;
	string sample;
	getline(ifs, sample);
	while(cas <= T){
		string ipstr;
		getline(ifs, ipstr);
		int len = ipstr.length();
		ofs<<"Case #"<<cas++<<": ";
		for(int i=0; i<len; i++){
			if(isalpha(ipstr[i]))
				ofs<<STR[ipstr[i]-'a'];
			else if(ipstr[i]=' ')
				ofs<<" ";
		}
		ofs<<endl;
	}
	ifs.close();ofs.close();
	return 0;
}
	
		
