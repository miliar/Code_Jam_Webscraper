#include <iostream>
#include <fstream>
using namespace std;

long max (long a, long b) { return (a>b)?a:b; };
long min (long a, long b) { return (a>b)?b:a; };

// a >= b
long win (long x1, long x2) {
    long a=max(x1,x2);
    long b=min(x1,x2);
    if (a==b) return 0;
    if (a%b==0) return 1;

    if (a/b==1) return !win(a-b,b);

    return max(win(a%b,b),win(a%b+b,b));
}

int main (void) {
    ifstream myfile;
    myfile.open("C-small-attempt0.in", ios::in);
    int cases;
    myfile >> cases;

    for (int c=1; c<=cases; c++) {
        long al, ah, bl, bh;
        myfile >> al >> ah >> bl >> bh;
        long counter=0;
        for (int i=al; i<=ah; i++) {
            for (int j=bl; j<=bh; j++) {
                if (win(i,j)) counter++;
            }
        }
        cout << "Case #" << c << ": " << counter << '\n';
    }

    myfile.close();
    return 0;
};
