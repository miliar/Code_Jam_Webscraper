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

if(inputFile.is_open()){
    if(inputFile.good()){
        getline(inputFile, line);
        cases = atoi(line.c_str());
        for(int i=1;i<=cases;i++){
            getline(inputFile,line);
            outputFile<<"Case #"<<i<<": ";
            
	    int pos = line.find(" ");
	    int googlers =atoi(line.substr(0,pos).c_str());
	    line = line.substr((pos+1));
	    
	    pos = line.find(" ");
	    int surpriseTriplets = atoi(line.substr(0,pos).c_str());
	    line = line.substr((pos+1));
	    
	    pos = line.find(" ");
	    int minResult = atoi(line.substr(0,pos).c_str());
	    line = line.substr((pos+1));
	    
	    int sum=0;	
	    if(minResult == 0){
		sum = googlers;
	    }else{
	    while(line != ""){
		pos = line.find(" ");
		int num;
		if((pos == -1) && (line != "")){
		    num = atoi(line.c_str());
		    line = "";
		}else{    
		    num = atoi(line.substr(0,pos).c_str());
		    line = line.substr((pos+1));
		}
		int div = num/3;
		int reminder = num % 3;
		
		if(num == 0){
		
		}else if(num == 1){
		    if(minResult <= 1){
		    	sum++;
		    }
		}else if(num == 2){
		    if((minResult == 2) && (surpriseTriplets > 0)){
			sum++;
                        surpriseTriplets--;
		    }else if(minResult < 2){
			sum++;
		    }
		}else if(div >= minResult){
		    sum++;
		}else if( ((div+1) == minResult) && (reminder >= 1) ){
		    sum++;
		}else if( ((div+1) == minResult) && (reminder == 0) ){
		    if(surpriseTriplets > 0){
			sum++;
			surpriseTriplets--;
		    }
		}else{
		    if( ((div+reminder) >= minResult) && (surpriseTriplets > 0)){
			sum++;
			surpriseTriplets--;
		    }
		}
	    }
	    }
	    outputFile<<sum<<"\n";
	}
    }
}

inputFile.close();
outputFile.close();

return 0;
}
