#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <string>
#include <cassert>
#include <cstdio>
#include <cstring>

using namespace std;

#define MAX_LINE 600
#define MAX_PHRASE 25
typedef long long counter_t;

void do_testcase() {
    counter_t data [MAX_LINE] [MAX_PHRASE];
    for (int i = 0; i < MAX_LINE; i++){ 
        for (int j = 0; j < MAX_PHRASE; j++) {
            data [i] [j] = 0;
        }
    }

    char line[MAX_LINE];
    cin.getline(line, sizeof(line));

    cerr << sizeof(counter_t) << endl;

    counter_t count = 0;

    for (int i = 0; i < MAX_LINE; i++) {
        counter_t * row = data [i];

        char at = line [i];
        if (at == '\0') {
            if (i > 0) {
                count = data [i - 1] [18];                
            } // Else: i = 0 so count = 0
            break;
        }
        if (i > 0) {
            memcpy(row, data [i - 1], sizeof(counter_t) * MAX_PHRASE);
        }

        switch (at) {
            case ' ':
                row [7]     += row[6];
                row [10]    += row[9];
                row [15]    += row[14];
                break;
            case 'a':
                row [17]    += row[16];
                assert(row [17] >= 0);
                break;
            case 'c':
                row [3]     += row [2];
                row [11]    += row [10];
                break;
            case 'd':
                row [13]    += row [12];
                break;
            case 'e':
                row [1]     += row[0];
                row [6]     += row [5];
                row [14]    += row [13];

                row [14]    %= 10000;
                assert(row [14] >= 0);
                break;
            case 'j':
                cerr << row [16] << " " << row [15] << endl;
                row [16]    += row [15]; 
                row [16]    %= 10000;
                cerr << row [16] << endl;
                assert(row [16] >= 0);
                break;
            case 'l':
                row [2]     += row [1]; 
                break;
            case 'm':
                row [5]     += row [4];
                row [18]    += row [17];
                row [18]    %= 10000;
                assert(row [18] >= 0);
                break;
            case 'o':
                row [4]     += row [3];
                row [9]     += row [8];
                row [12]    += row [11];
                break;
            case 't':
                row [8]     += row [7];
                break;
            case 'w':
                row [0]++;            
                break;
            default:
                break;
        }
        // 0123456789012345678
        // welcome to code jam
        //
        /* for (int j = 0; j <= 18; j++) {
           cout << row [j] << " ";
        }
        cout << endl; */
    }
    assert(count >= 0);
    int result_count = count % 10000;
    if (result_count >= 1000) {
        cout << (result_count / 1000);
    } else {
        cout << '0';
    }
    result_count %= 1000;
    
    if (result_count >= 100) {
        cout << (result_count / 100);
    } else {
        cout << '0';
    }
    result_count %= 100;
 
    if (result_count >= 10) {
        cout << (result_count / 10);
    } else {
        cout << '0';
    }
    result_count %= 10;

    cout << result_count << endl;
}

int main(int argc, char **argv) {
    int test_cases;
    cin >> test_cases;

    // Needed to clear the line
    char line[MAX_LINE];
    cin.getline(line, sizeof(line));


    for (int i = 0; i < test_cases; i++) {
        cout << "Case #" << (i + 1) << ": ";
        do_testcase();
    }
}


