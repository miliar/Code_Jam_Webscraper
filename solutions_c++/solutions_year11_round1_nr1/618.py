#include <algorithm>
#include <sstream>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

long long gcd(long long a, long long b) {
    return (b == 0 ? a : gcd(b, a%b));
}

int main(int argc,char *argv[]) {
	ifstream in;
    in.open(argv[1]);
    
    ofstream out;
    out.open("freecell_statistics.txt");

    int t;
    long long n, d, g;
    in >> t;
    cout << t << endl;
    for(int i = 0; i < t; i++) {
        in >> n;
        in >> d;
        in >> g;
        bool possible = false;
        long long gc = gcd(d, 100);
        if (100/gc <= n)
            possible = true;
        if(d == 0)
            possible = true;
        if(d != 100 && g == 100)
            possible = false;
        if(d != 0 && g == 0)
            possible = false;     
        ostringstream oss;
        oss << "Case #" << i+1 << ": ";
        if(possible)
            oss << "Possible" << endl;
        else 
            oss << "Broken" << endl;

        out << oss.str();
    }

    in.close();
    out.close();
	return 0;
}
