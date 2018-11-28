#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char** argv) {

    ifstream file(argv[1]);

    int testCnt;
    file >> testCnt;

    int counter = 1;
    for (int i = 0; i < testCnt; i++) {
        int runs, capacity, groupCount;
        file >> runs >> capacity >> groupCount;
        vector<int> groupSize;

//        cout << "runs: " << runs
//             << " capacity: " << capacity
//             << " groupCount: " << groupCount
//             << endl;

        // load groups
        for (int j = 0; j < groupCount; j++) {
            int tmp;
            file >> tmp;
            groupSize.push_back(tmp);                    
        }

        // count euros
        int grp = 0; // index of group to go next
        int euros = 0;
        for (int j = 0; j < runs; j++) {

            // place groups to rollercoaster
            int occupiedSeats = 0;
            int groupsInRollerCoaster = 0;
            while (occupiedSeats + groupSize[grp] <= capacity
                        && groupsInRollerCoaster < groupCount) {
                occupiedSeats += groupSize[grp];
                groupsInRollerCoaster++;
                euros += groupSize[grp];
                grp = (grp + 1) % groupCount;
            }            
        }

        // output
        cout << "Case #" << counter << ": " << euros << endl;
        counter++;
    }

    return (EXIT_SUCCESS);
}

