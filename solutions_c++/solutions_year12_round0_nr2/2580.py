//#include <cstdlib>
//#include <cstring>
#include <fstream>
#include <iostream>
using namespace std;

int do_it(int N,int S,int p,int* &iptr){
    int a = 3 * p - 4;
    int b = 3 * p - 2;
    int cnta = 0;
    int cntb = 0;
    int tmp = -1;

    if(a < 0)
        a = p;
    if(b < 0)
        b = p;

    for(int i = 0 ; i < N; i++){
        tmp = *(iptr+i);
        if(tmp >= b)
            cntb++;
        else
            if(tmp >=a)
                cnta++;
    }
    int ret = 0;

    if(cnta <= S)
        ret = cntb + cnta;
    else
        ret = cntb + S;
    return ret;
}

void read_file(string fileName){
    ifstream inFile(fileName.c_str());
    if(!inFile.good()){
        cout << "error when open file" << endl;
        return;
    }
    ofstream outFile("bb_out.txt");
    char* token = NULL;
    string line;
    int ti = 1;
    int cnt = 0;
    int N = 0;
    int S = 0;
    int p = 0;
    int tests = 0;

    inFile >> tests;
    for(int ti = 1; ti <= tests; ti++){ 
        inFile >> N;
        inFile >> S;
        inFile >> p;
        
        int* iptr = new int[N];
        for(int i = 0 ; i < N; i++){
            inFile >> *(iptr+i) ;
        }
        cout << "Case #"<< ti << ": " <<  do_it(N,S,p,iptr) << endl;
        outFile << "Case #"<< ti << ": " <<  do_it(N,S,p,iptr) << "\n";
        delete [] iptr;
    }
    inFile.close();
    outFile.close();
}


int main(){
    read_file("B-large.in");
    return 0;
}
