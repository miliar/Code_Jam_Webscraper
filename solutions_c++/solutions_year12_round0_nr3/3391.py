#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<cstdlib>
using namespace std;

int main(){

ifstream inputFile ("small.txt");
ofstream outputFile ("output.txt");

string line;
int cases=0;

if(inputFile.is_open()){
    if(inputFile.good()){
        getline(inputFile, line);
        cases = atoi(line.c_str());
        for(int i=1;i<=cases;i++){
            getline(inputFile,line);
            outputFile<<"Case #"<<i<<": ";
	    int pos = line.find(" ");
	    int min = atoi(line.substr(0,pos).c_str());
	    string str = line.substr(0,pos);
	    int max = atoi(line.substr((pos+1)).c_str());
	
	    int len = strlen(str.c_str());
	    int countPair = 0;
//	    cout<<"min max "<<min<<" "<<max<<endl;

	    while(min <= max){
		int j=1;
		if(len <=1){
		    break;
		}
		while(j < len){
		    string first,second;
		    first = str.substr(0,j);
		    second = str.substr(j);
		    if( (j == (len/2)) && ((strlen(first.c_str())) == (strlen(second.c_str()))) && (first == second)){
			break;
		    } 
		    string result = second;
		    result +=first;
		    int number2 = atoi(result.c_str());
//		    cout<<"number1 number2 "<<min<<" "<<number2<<endl;
		    if((min < number2) && (number2 <= max)){
			countPair++;
//			cout<<"countPair "<<countPair<<endl;
		    }
		    j++;
		}
		min++;
		sprintf((char *)str.c_str(),"%d", min);
		//cout<<"countPair "<<countPair<<endl;
		//cout<<"min str "<<min<<" "<<str<<endl;
	    }
	    outputFile<<countPair<<"\n";
	}
    }
}

inputFile.close();
outputFile.close();

return 0;
}


