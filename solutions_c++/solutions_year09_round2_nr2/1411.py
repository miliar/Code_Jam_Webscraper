#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>

#include <algorithm>
#include <vector>
#include <string>
#define fori(N) for(int i=0; i<N; i++)
#define forj(N) for(int j=0; j<N; j++)

using namespace std;

int pow10(int n){
    int a = 1;
    fori(n) a *= 10;
    return a;
}

int main(){
    ifstream fin("B-small-attempt.in");
    ofstream fout("B-small.out");
    int n,i,a;
    int curr;
    
    fin >> n;
    
    for(int Z=0; Z<n; Z++){
        char digits[20];
        fin >> curr;
        int k = curr;
        for(i=0; k>0; i++){
            digits[i] = '0' + k%10;
            k /= 10;
        }
        digits[i] = '\0';
        reverse(digits, digits+i);
        //cout << i << endl;
        //cout << digits << " ->";
        //cout << "---" << endl;
        if(next_permutation(digits, digits + i)){
            //reverse(digits, digits + i);
            //cout << digits << endl;
            a = atoi(digits);
        }
        else{
            digits[i] = '0';
            digits[++i] = '\0';
            sort(digits, digits+i);
            //reverse(digits, digits+i);
            while(next_permutation(digits, digits+i)){
                a = atoi(digits);
                cout << a << endl;
                if(a > pow10(i-1)) break;
            }
        }
        fout << "Case #" << Z+1 << ": " << a << endl;
        
    }
          
    cin.get();
    return 0;   
}
