#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char** argv) {

    int count, a, b;
    int i;
    int order, temp, current;
    int found, result;
    
    cin >> count;
    
    for (i=0; i<count; i++) {
        cin >> a >> b;

       // najdi najvyssi rad
        temp  = a;
        order = 1;
        while (temp > 9) {
            temp  /= 10;
            order *= 10;
        }
        
        result = 0;
       // najdi vsetky recycled numbers
        for (current = a; current<=b; current++) {
            found = 0;
            
            temp = current;
            do {
                temp = (temp%10)*order+(temp/10);
                
                if (temp == current) {break;}
                if (temp > current && temp <= b) {found++;}
            } while (temp != current);
            result += found;
        }
        
        cout << "Case #" << (i+1) << ": " << result << endl;
    }
    
    return 0;
}

