#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <sstream>
#include <math.h>
#include <algorithm>

//#define DEBUG

using namespace std;

/*
 *  Reads out input file and starts processing
 */
int main(int argc, char** argv) {
    ifstream input(argv[1]);
    string line;

    getline(input, line);
    
    int cases = atoi(line.data());

    // Parse Items from Input
    for(int c = 1; c <= cases; c++) {
        getline(input,line);
        istringstream linestream(line);
        string data;
#ifdef DEBUG
        cout << "Parsing " << line << endl;
#endif

        int actions = 0;
        linestream >> actions;
        
        int time = 0;
        int b_pos = 1, o_pos = 1;
        int b_time = 0, o_time = 0;
        
        for (int a = 0; a < actions; a++) {
          char player = ' ';
          int button = 0;
          linestream >> player >> button;
          
          if (player == 'O') {
            o_time += abs(button - o_pos);
            o_pos = button;
            if (o_time < b_time) o_time = b_time;
            o_time++; // press the button
          } else {
            b_time += abs(button - b_pos);
            b_pos = button;
            if (b_time < o_time) b_time = o_time;
            b_time++; // press the button
          }
          
        }
        
        cout << "Case #" << c << ": " << (b_time > o_time ? b_time : o_time) << endl;
    }
    
    return 0;
}
