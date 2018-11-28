#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int main (void) {
    int testCases = 0;
    string input;
    int currentCase = 0;
    int numMoves = 0;

    ifstream fileInput("input.in");
    ofstream fileOutput("output.txt");

    if (fileInput.is_open()) {
        fileInput >> input;
        istringstream stream(input);
        stream >> testCases;
    }

    for (currentCase = 0; currentCase < testCases; currentCase++) {

        vector<int> bluesButtons;
        vector<int> orangesButtons;
        vector<char> buttonOrder;
        int i = 0, j = 0, k = 0;
        int orangesPos = 1;
        int bluesPos = 1;
        int seconds = 0;
        int temp;

        if (fileInput.is_open()) {
            fileInput >> input;
            istringstream stream(input);
            stream >> numMoves;
        }

        for (i = 0; i < numMoves; i++) {
            fileInput >> input;
            if (input[0] == 'O') {
                buttonOrder.push_back('O');
                fileInput >> input;
                istringstream stream(input);
                stream >> temp;
                orangesButtons.push_back(temp);
            } else {
                buttonOrder.push_back('B');
                fileInput >> input;
                istringstream stream(input);
                stream >> temp;
                bluesButtons.push_back(temp);
            }
        }

        if (orangesButtons.size() == 0) {
            orangesButtons.push_back(1);
        }
        if (bluesButtons.size() == 0) {
            bluesButtons.push_back(1);
        }

        i = 0;
        j = 0;
        k = 0;
        while (k < buttonOrder.size()) {
            //Check for presses
            if (buttonOrder[k] == 'O' && orangesPos == orangesButtons[i]) {
                k++;
                i++;
                if (bluesButtons[j] > bluesPos) {
                    bluesPos++;
                } else if (bluesButtons[j] < bluesPos) {
                    bluesPos--;
                }
                seconds++;

            } else if (buttonOrder[k] == 'B' && bluesPos == bluesButtons[j]) {
                k++;
                j++;
                if (orangesButtons[i] > orangesPos) {
                    orangesPos++;
                } else if (orangesButtons[i] < orangesPos) {
                    orangesPos--;
                }
                seconds++;

            } else {
                 if (orangesButtons[i] > orangesPos) {
                    orangesPos++;
                } else if (orangesButtons[i] < orangesPos) {
                    orangesPos--;
                }
                if (bluesButtons[j] > bluesPos) {
                    bluesPos++;
                } else if (bluesButtons[j] < bluesPos) {
                    bluesPos--;
                }
                seconds++;

            }
        }
        cout << "Case #" << (currentCase+1) << ": " << seconds << endl;
        fileOutput << "Case #" << (currentCase+1) << ": " << seconds << endl;

    }



}
