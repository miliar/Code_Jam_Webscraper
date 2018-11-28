#include <vector>
#include <map>
#include <cstdlib>
#include <iostream>
#include <fstream>
using namespace std;

int adjust(int lstart,int lend){
    int a = 0;
    int r = 0;
    int cnt = 0;
    int m = 0;

    int len = 1;
    int d = 10;
    int n2 ;

    map<int,int>::const_iterator iter;

    for(int n = lstart; n < lend ; n++){
        map<int,int> dict;
        n2 = n;
        d = 10;
        len = 1;
        while(1){
            n2 = n2/d;
            if(n2==0)
                break;
            else
                len = len * 10;
        }
        len = len * 10;
        d = 10;
        while(1){
            a = n/d;
            r = n%d;
            if(a == 0)
                break;
            m = a + r * (len/d) ;
            
            if(m > n && m <= lend){
                dict[m] = m;
            }
            d = d * 10;
        }
        cnt = cnt + dict.size();
    }

    return cnt;
}

int range(int lstart, int lend){
    int cnt = 0;
    for(int i = lstart; i < lend;i++){
        cnt = cnt + adjust(i,lend);
    }
    return cnt;
}

void read_file(string fileName){
    ifstream inFile(fileName.c_str());
    ofstream outFile("c_out.txt");
    if(!inFile.good()){
        cout << "Error when opening file" << endl;
        return;
    }
    int cline = 0;
    int lstart = 0;
    int lend = 0;
    int ret = 0;
    inFile >> cline ;
    for(int i = 1 ; i <= cline; i++){
        inFile >> lstart;
        inFile >> lend;
        cout << "range(" << lstart << "," << lend << ");" << endl;
        ret = adjust(lstart,lend);
        outFile << "Case #" << i << ": " << ret << "\n";
    }
    inFile.close();
    outFile.close();
}

int main(){
    string fileName = "C-large.in";
    read_file(fileName);
    return 0;
}
