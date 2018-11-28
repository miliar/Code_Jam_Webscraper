#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;
typedef vector<int> VI;


int calc(VI& a, VI& b){
    int aSize=a.size();
    int bSize=b.size();
    if(!aSize){
        return 0;
    }     
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    int i=0;
    int j=0;
    int count = 0; 
    while(i<aSize && j<bSize){
        while(i<aSize && a[i]<b[j]) {
            count++;
            i++;
        }
        i++;
        j++;    
    }
    count+=i<aSize?aSize-i:0;
    return count;
}


void process(ifstream& input, ofstream& output){

    string line;
    getline(input, line);
    VI a1,a2,b1,b2;
    int N = atoi(line.c_str());
    for(int i=1; i<=N;++i){
        a1.clear();
        a2.clear();
        b1.clear();
        b2.clear();
        getline(input,line);
        int offset = atoi(line.c_str());
        getline(input,line);
        int A,B=0;
        sscanf(line.c_str(), "%d %d",&A,&B);
        int io,ip,eo,ep=0;
        while(A--){
            getline(input,line);
            sscanf(line.c_str(),"%d:%d %d:%d",&io,&ip,&eo,&ep);
            a1.push_back(60*io+ip);
            a2.push_back(60*eo+ep+offset);
        }
        while(B--){
           getline(input,line);
           sscanf(line.c_str(),"%d:%d %d:%d",&io,&ip,&eo,&ep);
           b1.push_back(60*io+ip);
           b2.push_back(60*eo+ep+offset); 
        }
        output << "Case #" << i << ": " << calc(a1,b2) << " " << calc(b1,a2) << endl;
    }

}



int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr,"usage: %s inputFile outputFile\n", argv[0]);
        return 1;
    }
    ifstream input(argv[1]);
    ofstream output(argv[2]);
    process(input, output);
    return 0;
}

