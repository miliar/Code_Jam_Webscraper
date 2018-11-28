//*******************************************
// Author: Samuel Jero
// Email: samuel.jero@gmail.com
// Date: 9/3/2009
//*******************************************
#include <string>
#include <vector>
#include <cstdlib>
#include <iostream>
using namespace std;


void load_dict();
int compute_case(string test);



int length;
int dict_num;
vector<string> dict;
vector<string> dict_cpy;



int main(){
	int testcases, result;
	string tmp; 

	cin >> length;
	cin >> dict_num;
	cin >> testcases;

	load_dict();

	for(int i=1; i <= testcases; i++){
		cin>> tmp;
		dict_cpy= dict;
		result=compute_case(tmp);
		cout<< "Case #"<<i<<": "<<result<<endl;
	}
return 0;
}



void load_dict(){
	string tmp;
	for(int i=0; i < dict_num; i++){
		cin >>tmp;
		if(cin.fail()){
			exit(1);
		}
		dict.push_back(tmp);
	}
return;
}



int compute_case(string test){
	int pos=0;
	string comp;
	bool in_paren=false;
	bool found;
	for(unsigned int i=0; i < test.length(); i++){
		if(test[i]=='('){
			in_paren=true;
			comp="";
			continue;
		}
		if(test[i]==')'){
			in_paren=false;
		}
		else{
			comp+= test[i];
		}
		if(in_paren==false){
			unsigned int j=0;
			while(j < dict_cpy.size()){
				found=false;
				for(unsigned int x=0; x < comp.length(); x++){
					if(dict_cpy[j][pos]==comp[x]){
						found=true;
					}
				}
				if(found==false){
					dict_cpy.erase(dict_cpy.begin()+j);
				}
				else{
					j++;
				}
			}
			comp="";
			pos++;
		}
	}
return dict_cpy.size();
}
