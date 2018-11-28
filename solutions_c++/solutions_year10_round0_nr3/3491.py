/* 
 * File:   C-ThemePark.cpp
 * Author: vdyy
 *
 * Created on May 8, 2010, 11:56 AM
 */

#include <stdlib.h>
#include <queue>
#include <fstream>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {

    ifstream in("C-small-attempt0.in");
    if (!in) {
        cout << "Cannot open input file for reading" << endl;
        getchar();
        return -1;
    }

    ofstream out("C-small-attempt0.out");
    if (!out) {
        cout << "Cannot open output file for writing" << endl;
        getchar();
        return -1;
    }

    unsigned int cases;

//    cin >> cases;
    in >> cases;

    for (unsigned int i = 1; i <= cases; i++) {
        unsigned long int rides = 0;
        unsigned long int cap = 0;
        int numGroups = 0;

//        cin >> rides;
//        cin >> cap;
//        cin >> numGroups;
        in >> rides;
        in >> cap;
        in >> numGroups;

        queue< unsigned long int > groups;
        for (int j = 1; j <= numGroups; j++) {
            unsigned long int people = 0;
//            cin >> people;
            in >> people;
            
            groups.push(people);
        }

        unsigned long int earning = 0;
        for (int j = 1; j <= rides; j++) {
            unsigned long int passengers = 0;
            int groupsOnBoard = 0;
            do {
                passengers += groups.front();
                groups.push(groups.front());
                groups.pop();
                groupsOnBoard++;
            } while (((groups.front() + passengers) <= cap) && (groupsOnBoard < numGroups));
            
            earning += passengers;
        }

//        cout << "Case #" << i << ": " << earning << endl;
        out << "Case #" << i << ": " << earning << endl;
    }

    if (in) in.close();
    if (out) out.close();

    return 0;
}

