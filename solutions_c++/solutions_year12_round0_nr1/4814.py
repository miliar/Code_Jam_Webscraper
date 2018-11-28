#include <iostream>

#include <fstream>
#include <string>

using namespace std;

string Google = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
	
	ifstream in ("A-small-attempt2.in");
	ofstream ven ("ven.out");	
	int ponovi;
	in >> ponovi;
	string brez;
	getline(in, brez);
	
	
	for(int a(0);a<ponovi;a++){
		
		string temp;
		getline(in, temp);
		
		ven << "Case #" << a+1 << ": ";
		
		for(int b(0); b<temp.size();b++){
			int stevilo;
			if(temp[b]==' ')ven << " ";
			else{
				stevilo=temp[b]-'a';
				ven << Google[stevilo];
			}
		}
		
		ven << endl;
	}
	return 0;
}
