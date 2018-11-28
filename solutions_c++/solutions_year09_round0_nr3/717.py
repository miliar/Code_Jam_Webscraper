#include <iostream>
#include <string>

using namespace std; 

int main() {
    char str[] = "welcome to code jam" ;
    int table[20] ; 
    int n,i; 
    string instr;


    cin >> n  ;
    getline(cin,instr);
    for(i=0;i<n; i++) {
        getline(cin,instr);
        int j,k; 
        for(j=0;j<20;j++) { table[j] =0 ; }
        table[0] = 1; 
        for(j=0;j<instr.length();j++) {
            for(k=0;k<19;k++) {
                if (instr[j]==str[k]) {
                    table[k+1] += table[k] ;
                    table[k+1] %= 10000;
                }
            }
        }
        //cout << instr[j-1] ;
        cout << "Case #" << i+1 << ": " ; 
        if (table[19]<10) { cout << "000" << table[19] << endl; }
        else if (table[19]<100) { cout << "00" << table[19] << endl; }
        else if (table[19]<1000) { cout << "0" << table[19] << endl; }
        else { cout << table[19] << endl; }

    }
    cout.flush();

    return 0 ;
}
