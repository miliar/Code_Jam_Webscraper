#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <stack>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#define INF 1000000
typedef long long ll;
typedef unsigned long long llu;
using namespace std;

int main(void) {
    char m[] = {
        'y', 'h', 'e', 's', 'o', 'c',
        'v', 'x', 'd', 'u', 'i', 'g',
        'l', 'b', 'k', 'r', 'z', 't',
        'n', 'w', 'j', 'p', 'f', 'm',
        'a', 'q'
    };

    string in;
    getline(cin, in);

    int i = 1;
    while(getline(cin, in)) {
        cout << "Case #" << i << ": ";
        for(unsigned int j = 0; j < in.length(); ++j) {
            if(in[j] == ' ') cout << ' ';
            else {
                cout << m[in[j]-'a'];
            }
        }
        cout << endl;
        ++i;
    }
    return 0;
}
