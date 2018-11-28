//*******************************************
// Author: Samuel Jero
// Email: samuel.jero@gmail.com
// Date: 9/3/2009
//*******************************************
#include <string>
#include <vector>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <iomanip>
using namespace std;


void find(string what, string in, int pos);


int count;


int main(){
	int testcases;
	string tmp;

	cin>>testcases;
	getline(cin,tmp);
	for(int i=1; i <=testcases; i++){
		count=0;
		getline(cin, tmp);
		find("welcome to code jam", tmp, 0);
		cout<<"Case #"<<i<<": "<<setw(4)<<setfill('0')<<count<<endl;
	}

return 0;
}


void find(string what, string in, int pos){
	string tmp;
	if(what!=""){
		for(unsigned int i=pos; i < in.length(); i++){
			if(what[0]==in[i]){
				tmp=what;
				tmp.erase(tmp.begin());
				find(tmp, in, i+1);
				if(tmp==""){
					count++;
				}
				if(count == 10000){
					count=0;
				}
			}
		}
	}
return;
}
