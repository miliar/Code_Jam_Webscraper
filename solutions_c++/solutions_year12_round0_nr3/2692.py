#include <iostream>
#include <sstream>
#include <cmath>
#include <set>
#include <fstream>
using namespace std;
set<int> pairs;
set<int> numbers;
set<int>::iterator it;

bool rotate(int number, int minimum, int maximum, int base, int digits) { 
    int new_number = number;
    pairs.clear();
    pairs.insert(number);
    for (int i=0; i<digits; i++) { 
        int div = new_number / base;
        int rem = new_number % base;
        new_number = rem*10 + div;
        if ( new_number<minimum || new_number > maximum) continue;
        pairs.insert(new_number);
    }
}



int main(int argc, char** argv) {
    if (argc < 2) { 
        cout << "Usage " << argv[0] << " <input file>" << endl;
        return 1;
    }

    int maximum, minimum;
    int count;
    int cases;
    int base, digits;
    
    ifstream in(argv[1]);
    in >> cases;
    
    for (int c=1; c<=cases; c++) { 
        cout << "Case #" << c << ": ";
        in >> minimum; in >> maximum;
        digits = log10(minimum);
        base = pow(10, digits);
        count = 0;
        numbers.clear();
        for (int i=minimum; i<=maximum; i++) {
            if (numbers.count(i) == 1) continue; 
            rotate(i, minimum, maximum, base, digits);
            if (pairs.size() > 1) { 
                for (it=pairs.begin(); it!=pairs.end(); it++){
                    numbers.insert(*it);
                }
                count += pairs.size() * (pairs.size()-1) / 2;
            }
        }
        cout << count << endl;
    }

    return 0;
}
