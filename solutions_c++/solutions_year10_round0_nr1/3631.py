#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

using namespace std;

bool process(int n,int k){
    int c = int(pow(double(2),double(n)));
    int r = k%c;
    if (r==(c-1)){
        return true;    
    }
    else{
        return false;    
    }
}
int main(){
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("tung.txt");
    int t;
	fin >> t;
    int n, k;
    for (int i=1; i<=t; i++){
        fin >> n >> k;
        if (process(n,k)){
            fout << "Case #" << i << ": ON"<<endl;    
        }    
        else{
            fout << "Case #" << i << ": OFF"<<endl;         
        }
    } 
    return 0;    
}
