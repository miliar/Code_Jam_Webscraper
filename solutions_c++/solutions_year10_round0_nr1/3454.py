#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("1.out");

long long int power(int a, int b)
{
     long long int c=a;
     for (int n=b; n>1; n--) c*=a;
     return c;
}

bool problem1(int c, long long int s) {
     
     if(s==0) return false;
     long long M=power(2,c);
     
     s=s%M;
     
     if(s==M-1) return true;
     else return false;
     
}


int main() {
    
    int C;
    fin >> C;
    
    for(int i=0;i<C;i++) {
    
        int cSnappers;
        fin >> cSnappers;
        long long int snaps;
        fin >> snaps;
        
        
        fout << "Case #"<<i+1<<": "; 
        if( problem1(cSnappers,snaps) ) fout << "ON" << endl;
            else fout << "OFF" << endl;
    }
    
    system("pause");
}
