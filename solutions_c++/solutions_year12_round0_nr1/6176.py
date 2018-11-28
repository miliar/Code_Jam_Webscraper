#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
using namespace std;

string kerja(string a){	
	int sizestr = a.length();
	int i=0;
	string s = "";
	for (i=0; i<sizestr; i++){
		if (a[i]=='y' || a[i]=='Y') { s = s + "a";}
        else if (a[i]=='n' || a[i]=='N') { s = s + "b";}
        else if (a[i]=='f' || a[i]=='F') { s = s + "c";}
        else if (a[i]=='i' || a[i]=='I') { s = s + "d";}
        else if (a[i]=='c' || a[i]=='C') { s = s + "e";}
        else if (a[i]=='w' || a[i]=='W') { s = s + "f";}
        else if (a[i]=='l' || a[i]=='L') { s = s + "g";}
        else if (a[i]=='b' || a[i]=='B') { s = s + "h";}
        else if (a[i]=='k' || a[i]=='K') { s = s + "i";}
		else if (a[i]=='u' || a[i]=='U') { s = s + "j";}
        else if (a[i]=='o' || a[i]=='O') { s = s + "k";}
        else if (a[i]=='m' || a[i]=='M') { s = s + "l";}
        else if (a[i]=='x' || a[i]=='X') { s = s + "m";}
        else if (a[i]=='s' || a[i]=='S') { s = s + "n";}
        else if (a[i]=='e' || a[i]=='E') { s = s + "o";}
        else if (a[i]=='v' || a[i]=='V') { s = s + "p";}
        else if (a[i]=='z' || a[i]=='Z') { s = s + "q";}
        else if (a[i]=='p' || a[i]=='P') { s = s + "r";}
        else if (a[i]=='d' || a[i]=='D') { s = s + "s";}
        else if (a[i]=='r' || a[i]=='R') { s = s + "t";}
        else if (a[i]=='j' || a[i]=='J') { s = s + "u";}
        else if (a[i]=='g' || a[i]=='G') { s = s + "v";}
        else if (a[i]=='t' || a[i]=='T') { s = s + "w";}
        else if (a[i]=='h' || a[i]=='H') { s = s + "x";}
        else if (a[i]=='a' || a[i]=='A') { s = s + "y";}
        else if (a[i]=='q' || a[i]=='Q') { s = s + "z";}
		else if (a[i]==' ') { s = s + " ";}
	}
	return s;
}

void prosesfile(){
	ifstream input("input.in");
	
	if (!input) {
			cout<< "File not opened." << endl;
	}

	string str;
	getline(input,str);
	int counter = 0;
	int T = atoi (str.c_str());
	//cout<<T<<endl;
	ofstream myfile ("output.txt");
	if (T>30 || T<1){
		cout<<"Error, T is limited."<<endl;
	}
	else{
		while (!input.eof()){
			++counter;
			getline(input,str);
			if (counter>0 && counter <=30){
				myfile<<"Case #"<<counter<<": ";
				myfile << kerja(str);
				myfile<<endl;
			}
		}
	}
}



int main () {
	prosesfile();
}

