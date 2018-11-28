#include <functional>
#include <algorithm>
#include <utility>
#include <cassert>
#include <cmath>
#include <ctime>

#include <numeric>
#include <iomanip>
#include <complex>
#include <float.h>
#include <cfloat>

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <cstdio>

#include <cstring>
#include <string>

#include <iterator>
#include <vector>
#include <bitset>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

const char MAP[26][2] = {
    {'a', 'y'}, {'b', 'h'}, {'c', 'e'}, {'d', 's'}, {'e', 'o'}, {'f', 'c'}, {'g', 'v'}, {'h', 'x'}, 
    {'i', 'd'}, {'j', 'u'}, {'k', 'i'}, {'l', 'g'}, {'m', 'l'}, {'n', 'b'}, {'o', 'k'}, 
    {'p', 'r'}, {'q', 'z'}, {'r', 't'}, {'s', 'n'}, {'t', 'w'}, 
    {'u', 'j'}, {'v', 'p'}, {'w', 'f'}, {'x', 'm'}, 
    {'y', 'a'}, {'z', 'q'}
};

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int N;
    scanf("%d\n", &N);
    
    for(int i = 0; i < N; ++i) {
        string str;
        getline(cin, str);

        for(int j = 0; j < str.length(); ++j)
            if(str[j] != ' ')
                str[j] = MAP[str[j] - 'a'][1];

        cout << "Case #" << i + 1 << ": " << str;
        if(i + 1 < N)
            cout << endl;
    }

    return 0;
}

