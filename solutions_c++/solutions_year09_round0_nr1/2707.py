#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>
using namespace std;
int main (int argc, char * const argv[]) {
	ofstream outFile;
	ifstream inFile;
	outFile.open("A-small.out");
	inFile.open("A-small-attempt0.in.txt");
	string parsedString;
	int L,d,n;
	inFile>>L>>d>>n;
	char charSearch;
	string stringSearch;
	vector<string> dictionary(d);
	vector<string> possibilities;
	for(int c=0;c<d;c++){
		inFile>>dictionary[c];
	}
	
	for(int c=0; c<n; c++){
		possibilities=vector<string>(0);
		for(int i=0; i<d;i++){
			possibilities.push_back(dictionary[i]);
		}
		
		for(int i=0; i<L;i++){
			inFile>>charSearch;
			if(charSearch=='('){
				inFile>>charSearch;
				stringSearch="";
				while(charSearch!=')'){
					stringSearch.append(1,charSearch);
					inFile>>charSearch;
				}
				vector<string>::iterator it=possibilities.begin();
				while(it!=possibilities.end()){
					if(stringSearch.find((*it)[i])==-1)
						it=possibilities.erase(it);
					else
						++it;
				}
			}
			else{
				vector<string>::iterator it=possibilities.begin();
				while(it!=possibilities.end()){
					if((*it)[i]!=charSearch)
						it=possibilities.erase(it);
					else
						++it;
				}
			}
		}
		outFile<<"Case #"<<c+1<<": "<<possibilities.size()<<endl;
	}
	outFile.close();
	inFile.close();
    return 0;
}
