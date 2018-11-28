#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream input("/home/pabratte/Downloads/A-small-attempt3.in");
	if(!input){
		cerr<<"ERROR"<<endl;
	}
	
	int nTestCases;
	string line;
	input>>nTestCases;
  //char dic[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char dic[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	
	
	input.ignore();
	for(int i=0; i<nTestCases; i++){
		getline(input, line);
//		if(line.find("hello")!=string::npos || line.find("how")!=string::npos){
//			#cout<<"Case #"<<i+1<<": "<<line<<endl; 
//			continue;
//		}
		unsigned size=line.size();
		for(unsigned j=0; j<size; j++){
			if(line[j]!= ' ')
				line[j]=dic[line[j]-((int)'a')];
		}
		cout<<"Case #"<<i+1<<": "<<line<<endl; 
	}
	input.close();
	
	return 0;
}

