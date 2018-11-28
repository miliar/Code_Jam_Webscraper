#include<iostream>
#include<string>
#include<cstdlib>
using namespace std;

char letters[] = {'y', //a
                  'h', //b
 		  'e', //c
                  's', //d
		  'o', //e
                  'c', //f
                  'v', //g
                  'x', //h
                  'd', //i
 		  'u', //j
                  'i', //k
	          'g', //l
		  'l', //m
                  'b', //n
                  'k', //o
		  'r', //p
                  'z', //q
                  't', //r
		  'n', //s
                  'w', //t
                  'j', //u
                  'p', //v
                  'f', //w
                  'm', //x                
		  'a', //y
                  'q'  //z
}; 

int main(){
	int T;
	string t;
	getline(cin, t, '\n');
	T = atoi(t.c_str());

	for(int i=0; i<T; i++){
		string input;
		getline(cin, input, '\n');
		
		string output;
		for(int j=0; j<input.length(); j++){
			char in = input[j];
			char out;
			if(in==' ') out = ' ';
			else out = letters[in-'a']; 			
			output += out;		
		}
		cout << "Case #" << i+1 <<": " << output << endl;				
	}	
}
