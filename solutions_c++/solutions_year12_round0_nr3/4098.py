#include<iostream>
#include<fstream>
using namespace std;

bool es ( int a, int b) {
    if(a < 10) return false;
    else if(a < 100) {
            int a1, a2, b1, b2;
            a1 = a%10; a/=10;
            a2 = a%10; a/=10;
            
            b1 = b%10; b/=10;
            b2 = b%10; b/=10;
            if(a1%10 == b2%10 && a2%10 == b1%10) return true;
            else return false;
        }else{
            int a1, a2, a3, b1, b2, b3;
            a1 = a%10; a/=10;
            a2 = a%10; a/=10;
            a3 = a%10; a/=10;
            
            b1 = b%10; b/=10;
            b2 = b%10; b/=10;
            b3 = b%10; b/=10;
            
            if(a1 == b3 && a2 == b1 && a3 == b2) return true;
            if(a1 == b2 && a2 == b3 && a3 == b1) return true;
            return false;
        }
}

int main() {
    ifstream fin ("a.in");
    ofstream fout ("a.out");    
    int n;
    fin >> n;
    for(int i = 0; i < n; ++i) {
        int a,b;
        fin >> a >> b;
        int per = 0;
        for(int ii = a; ii <= b; ++ii) {
            for(int k = ii+1; k <= b; ++k) {
                if(es(ii,k)) ++per;
            }
        }
        fout << "Case #" << i+1 << ": " << per << endl;
    }
}
