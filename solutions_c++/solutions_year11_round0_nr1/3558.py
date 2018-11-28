#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <math.h>
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
typedef long s32;
typedef unsigned long long u32;



#define ORANGE 0
#define BLUE 1



int main(int argc, char* argv[])
{
	string line;
	int T;
	cin >> T;
	getline(cin, line);

	for (int t=0; t < T; t++) {

        cout << "Case #" << (t+1) << ": ";

		u64 N;
		cin >> N;

        list<pair<int, int> > orangeSequence;
        list<pair<int, int> > blueSequence;
        list<pair<int, int> > totalSequence;


        for (int n=0; n < N; n++) {
            char robot;
            int index;
            cin >> robot >> index;
            if (robot == 'O') {
                orangeSequence.push_back(pair<int, int>(ORANGE, index));
                totalSequence.push_back(pair<int,int>(ORANGE, index));

            } else {
                blueSequence.push_back(pair<int, int>(BLUE, index));
                totalSequence.push_back(pair<int,int>(BLUE, index));
            }
        }

        int orangeIndex = 1;
        int blueIndex = 1;
        int time = 0;

        do {

            bool buttonPress = false;


            // Orange robot check, only if queue is valid
            if (orangeSequence.size()) {

                // 1. If we are standing on a button and it is the next in the sequence, push it
                if ((orangeSequence.front().second == orangeIndex) && (totalSequence.front().first == ORANGE) && (totalSequence.front().second == orangeIndex)) {
                    buttonPress = true;
                    orangeSequence.pop_front();

                // 2. If we are not standing on a button, move to it
                } else {
                    if (orangeIndex > orangeSequence.front().second) {
                        orangeIndex--;

                    } else if (orangeIndex < orangeSequence.front().second) {
                        orangeIndex++;
                    }
                }
            }


            // Blue robot check, only if queue is valid
            if (blueSequence.size()) {

                // 1. If we are standing on a button and it is the next in the sequence, push it
                if ((blueSequence.front().second == blueIndex) && (totalSequence.front().first == BLUE) && (totalSequence.front().second == blueIndex)) {
                    buttonPress = true;
                    blueSequence.pop_front();

                // 2. If we are not standing on a button, move to it
                } else {
                    if (blueIndex > blueSequence.front().second) {
                        blueIndex--;

                    } else if (blueIndex < blueSequence.front().second) {
                        blueIndex++;
                    }
                }
            }

            if (buttonPress) {
                totalSequence.pop_front();
            }

            time++;

        } while (totalSequence.size());


        // Output the time
        cout << time << endl;
    }

    return 0;
}


