#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>


using namespace std;
typedef map< string, set<int> > Data;

bool hasEmpty(Data& data){

   for(Data::iterator iter=data.begin(); iter!=data.end(); ++iter){
        if(iter->second.empty()){
            return true;
        }
    } 
    return false;    

}

void calc(Data& data, int N, ofstream& output){

    int result = 0;
    if(!hasEmpty(data)){
        
        do{
            int max=0;
            for(Data::iterator iter=data.begin(); iter!=data.end(); ++iter){
                int x = *(iter->second.begin());
                max=max<x?x:max;
            }
            for(Data::iterator iter=data.begin(); iter!=data.end(); ++iter){
                set<int>::iterator start = iter->second.begin();
                set<int>::iterator setIter=iter->second.begin();
                for(;*setIter<max && setIter!=iter->second.end(); ++setIter);
                iter->second.erase(start, setIter);
            }
            result++;
            }while(!hasEmpty(data));
    }
    output << "Case #" << N << ": " << result << endl;
}

void clearData(Data& data){

    for(Data::iterator iter=data.begin(); iter!=data.end(); ++iter){
       iter->second.clear(); 
    }
}

void process(ifstream& input, ofstream& output){

    Data  data;
    string line;
    getline(input,line);
    int N = atoi(line.c_str());
    for(int i=1; i<=N; ++i){
        getline(input,line);
        int S = atoi(line.c_str());
        while(S--){
            set<int> row;    
            getline(input,line);
            data.insert(make_pair(line, row));
        }
        getline(input,line);
        int Q = atoi(line.c_str());
        int idx = 0;
        while(Q--){
            getline(input,line);
            data[line].insert(idx++);
        }  
        calc(data, i, output);
        data.clear();
    }
}



int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr,"usage: %s inputFile outputFile\n", argv[0]);
        return 1;
    }
    ifstream input(argv[1]);
    ofstream output(argv[2]);
    process(input,output);
    return 0;
}

