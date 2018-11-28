#include <fstream>
#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(int argc, char *argv[]){

	//create input and output streams
	ifstream input("C-small.in");
	ofstream output("C-small.out");
	//create the holders for the ammount of cases and string counts
	int Cases, StringCount;

	string wtcj="welcome to code jam";
	string instance;
	stack<string::iterator> stk_instance, stk_wtcj;

	//if both are open correctly, proceeds to solve the problem
	if( input && output ){
		//read the data from the first line
		input >> Cases;
		//finishes reading the first line
		getline(input, instance);
		int counter; //counter for loops
		for(counter=1;counter<=Cases;counter++){
			getline(input, instance);
			StringCount=0; 
			output << "Case #" << counter << ": ";
			string::iterator inst=instance.begin();
			string::iterator wtcjit=wtcj.begin();
			while(inst!=instance.end()){
				if(*inst==*wtcjit){
					stk_wtcj.push(wtcjit);
					wtcjit++;
					stk_instance.push(inst);
					inst++;
					if(wtcjit==wtcj.end()){
						StringCount++;
						inst=stk_instance.top();
						inst++;
						stk_instance.pop();
						wtcjit=stk_wtcj.top();
						stk_wtcj.pop();
					}
				}
				while(*inst!=*wtcjit && inst!=instance.end()){
					inst++;
				}
				while(inst==instance.end() && !stk_wtcj.empty()){
						inst=stk_instance.top();
						inst++;
						stk_instance.pop();
						wtcjit=stk_wtcj.top();
						stk_wtcj.pop();
				}
			}
			if(StringCount<10){output << 0;}
			if(StringCount<100){output << 0;}
			if(StringCount<1000){output << 0;}
			output << StringCount << endl;
		}
	
	}
	input.close();
	output.close();
	return 0;
}

