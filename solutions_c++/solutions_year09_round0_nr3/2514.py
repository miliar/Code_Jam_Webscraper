#include<iostream>
//#include<cstdlib>
//#include<cstdio>
#include<string>
//#include<cstring>
#include <sstream>
using namespace std;

int total=0;
string s="welcome to code jam";
int size = s.length()-1;
string word;
int wordsize;

void calc(int i, int p){
	for(int j=i; j<wordsize && (wordsize-1-j >= size-p); j++){
		if( word[j] == s[p] ){
			if( p == size ) {
				//cout << word[j] << "final " <<s[p] << endl;
				total++;
			}else{
				//cout << word[j] << " " <<s[p] << endl;
				calc(j+1, p+1);
			}
		}
	}
}


int main(){

	int N;
	cin >> N;
	getline(cin,word);
	
	for(int i=0; i<N;i++){
		getline(cin,word);
		//cout << word<< endl;
		total=0; 
		wordsize = word.length();
		calc(0,0);
		cout << "Case #" << i+1 << ": " ;
		//cout.width( 4 );
		//cout.fill( '0' );
		//total=123456789;
		string stotal;
        stringstream sout;
        sout.width( 4 );
		sout.fill( '0' );
        sout << total;
        stotal = sout.str();
		for(int j=stotal.length() -4; j<stotal.length(); j++){
                cout << stotal[j];
                
        }
		cout << endl; 
	}
}
