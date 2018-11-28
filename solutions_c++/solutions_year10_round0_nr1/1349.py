#include <iostream>
#include <cmath>
#include <fstream>
#include <cstdlib>
using namespace std;

bool determine(int n,int k){
    int divider = int(pow(double(2),double(n)));
    int result = k%divider;
    if (result==(divider-1)){
        return true;    
    }
    else{
        return false;    
    }
}
int main(){
    char te[100];
    cin.getline(te, 99);
    ifstream fin(te);
    if(fin.fail()) {
        exit(1);
    }
    ofstream fout("tung.txt");
    if(fout.fail()) {
        exit(1);
    }
    int t;
	fin >> t;
    int n, k;
    for (int i=1; i<=t; i++){
        fin >> n >> k;
        if (determine(n,k)){
            fout << "Case #" << i << ": ON"<< "\n";    
        }    
        else{
            fout << "Case #" << i << ": OFF"<< "\n";         
        }
    } 
    return 0;    
}
