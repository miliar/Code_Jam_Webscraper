#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    const char alpha[26] = {
        'y', // a
        'h', // b 
        'e', // c
        's', // d 
        'o', // e
        'c', // f 
        'v', // g
        'x', // h 
        'd', // i
        'u', // j 
        'i', // k
        'g', // l 
        'l', // m
        'b', // n 
        'k', // o
        'r', // p 
        'z', // q
        't', // r 
        'n', // s
        'w', // t 
        'j', // u
        'p', // v 
        'f', // w
        'm', // x 
        'a', // y
        'q'  // z 
    };

    unsigned int T;
    char c;
    scanf("%u\n", &T);
    for (unsigned int i = 1; i < T + 1; ++i) {
        cout << "Case #" << i << ": ";
        do {
            scanf("%c", &c);
            if (c == '\n') {
                break;
            }
            cout << (c == ' ' ? ' ' : alpha[c - 'a']);
        } while (true);
        cout << endl;
    }
}
