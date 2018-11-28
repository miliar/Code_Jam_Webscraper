#include <cstdlib>
#include <cstring>
#include <vector>
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
        if(tmp >= a && tmp < b)
            cnta++;
    }
    int ret = 0;

    if(cnta <= S)
        ret = cntb + cnta;
    else
        ret = cntb + S;
/*
    if(cntb + cnta < S)
        ret = 0;
*/
    cout << "cntb=" << cntb << " cnta="<< cnta ;
    cout << " S=" << S << " p=" << p;
    cout << " ret=" << ret << " small=" << a << " large=" << b << endl;
    return ret;
}

void read_file(string fileName){
    ifstream inFile(fileName.c_str());
    ofstream outFile("b_out.txt");
    char* token = NULL;
    string line;
    int ti = 1;
    int cnt = 0;
    int tests = 0;
    int N = 0;
    int S = 0;
    int p = 0;

    while(getline(inFile,line)){
        if (cnt == 0){
            tests = atoi(line.c_str());
            cnt++;
            continue;
        }
        
        token = strtok(const_cast<char*>(line.c_str())," ");
        N = atoi(token);
        token = strtok(NULL," ");
        S = atoi(token);
        token = strtok(NULL," ");
        p = atoi(token);
        int* iptr = new int[N];
        int icnt = 0;
        token = strtok(NULL," ");
        while(token!= NULL && strcmp(token,"")!=0 ){
            *(iptr+icnt) = atoi(token);
            token = strtok(NULL," ");
            icnt++;
        }
//        cout << N << " " << S << " " << p << ":";
        cout << "Case #"<< ti << ": " <<  do_it(N,S,p,iptr) << endl;
        outFile << "Case #"<< ti << ": " <<  do_it(N,S,p,iptr) << "\n";
        ti++;
//        if(ti == 440)
//            break;
        delete [] iptr;
    }
    inFile.close();
    outFile.close();
    
}


int main(){
  /*  
    int* iptr = new int[1];
    *(iptr) = 21;
    cout << do_it(1,0,8,iptr) << endl;
    cout << "guess_score(): ";
    cout << guess_score(29,0,1) << endl;
    cout << guess_score(14,0,1) << endl;
    cout << "before read_line" << endl;
*/    
    read_file("B-large.in");
    return 0;
}
