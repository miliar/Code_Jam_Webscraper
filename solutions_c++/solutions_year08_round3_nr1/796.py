#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;



int main() {
    ifstream in;
    in.open("A-small.in");
    ofstream out;
    out.open("A-small.out");
    int c = 1;
    int cases;
    int P, K, L;
    int p, k, l;
    int x = 0;
    int freq[1000];
    int high = 0;
    int min = 0;
    
    in >> cases;
    
    

    while (c <= cases) {
        in >> P;
        in >> K;
        in >> L;
        x = 0;
        high = 0;
        l = 0;
        p = 1;
        k = 0;
        min = 0;
        
        while (x < L) {
            in >> freq[x];
            x++;
        }
        x = 0;
        
        while (l < L) {
            x = 0;
            while (x < L) {
                if (freq[x] > freq[high])
                    high = x;
                x++;
            }
            min = min + freq[high] * p;
            freq[high] = 0;
            l++;
            k++;
            if (k == K) {
                p++;
                k = 0;
            }
        }
        
        out << "Case #" << c << ": " << min;
        if (c != cases)
            out << endl;
        
        
        
        
        
        c++;
    }
    
    return 0;
    
    
    
}
