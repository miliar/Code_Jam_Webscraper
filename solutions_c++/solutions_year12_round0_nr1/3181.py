#include<iostream>
#include<string>
#include<vector>
#include<fstream>
using namespace std;

int main(){

ifstream inputFile ("small.txt");
ofstream outputFile ("output.txt");

string line;
int cases=0;
char ch;
if(inputFile.is_open()){
    if(inputFile.good()){
	getline(inputFile, line);
	cases = atoi(line.c_str());
	for(int i=1;i<=cases;i++){
	    getline(inputFile,line);
	    outputFile<<"Case #"<<i<<": ";
	    while(line != ""){
		ch = * (line.substr(0,1)).c_str();
		line = line.substr(1);
		switch(ch){
		    case ' ': outputFile<<" "; break;
		    case 'y': outputFile<<"a"; break;
		    case 'n': outputFile<<"b"; break;
		    case 'f': outputFile<<"c"; break;
		    case 'i': outputFile<<"d"; break;
		    case 'c': outputFile<<"e"; break;
		    case 'w': outputFile<<"f"; break;
		    case 'l': outputFile<<"g"; break;
		    case 'b': outputFile<<"h"; break;
		    case 'k': outputFile<<"i"; break;
		    case 'u': outputFile<<"j"; break;
		    case 'o': outputFile<<"k"; break;
		    case 'm': outputFile<<"l"; break;
		    case 'x': outputFile<<"m"; break;
		    case 's': outputFile<<"n"; break;
		    case 'e': outputFile<<"o"; break;
		    case 'v': outputFile<<"p"; break;
		    case 'z': outputFile<<"q"; break;
		    case 'p': outputFile<<"r"; break;
		    case 'd': outputFile<<"s"; break;
		    case 'r': outputFile<<"t"; break;
		    case 'j': outputFile<<"u"; break;
		    case 'g': outputFile<<"v"; break;
		    case 't': outputFile<<"w"; break;
		    case 'h': outputFile<<"x"; break;
		    case 'a': outputFile<<"y"; break;
		    case 'q': outputFile<<"z"; break;
		}
	    }
	    outputFile<<"\n";
	}
    }
}

outputFile.close();
inputFile.close();

return 0;
}
