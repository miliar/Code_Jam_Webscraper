/* 
 * File:   main.cpp
 * Author: freemind
 *
 * Created on May 8, 2010, 5:11 PM
 */

#include <stdlib.h>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int numberOfTestCases, capasity, rollerTime, numberOfGroups;
    cin >> numberOfTestCases;
    for (int k = 0; k < numberOfTestCases; k++) {
        cin >> rollerTime >> capasity >> numberOfGroups;
        int list[numberOfGroups];
        
        int listIterator = 0, totalEarnings = 0;
        for (int listIterator = 0; listIterator < numberOfGroups; listIterator++) {
            cin >> list[listIterator];
        }
        listIterator = 0;

        for (int j = 0; j < rollerTime; j++) {
            int freeSeats = capasity;
            int startIterator = listIterator;
            bool start = 1;
            while (((freeSeats - list[listIterator]) >= 0) && ((listIterator != startIterator) || start)) {
                start = 0;
                freeSeats -= list[listIterator];
                listIterator++;
                if (listIterator == numberOfGroups)
                    listIterator = 0;
            }

            totalEarnings += (capasity - freeSeats);
        }



        cout << "Case #" << k + 1 << ": " << totalEarnings << endl;
    }

    return (EXIT_SUCCESS);
}

