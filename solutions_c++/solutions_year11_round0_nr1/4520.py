/* 
 * File:   main.cpp
 * Author: TrentReed
 *
 * Created on May 6, 2011, 7:03 PM
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

#define MAX_FILENAME_LENGTH 100
#define MAX_ACTIONS_PER_TEST 100
#define DEBUG false

typedef enum BotType {
    BOT_BLUE,
    BOT_ORANGE,
};

/*
 * 
 */
int main(int argc, char** argv) {
    //Instance variables
    ifstream inputFile;
    ofstream outputFile;
    char filename[MAX_FILENAME_LENGTH];

    short tests;
    short actionsInCurrentTest;
    char botIdentifier;

    long currentTime;
    bool buttonPressed;
    short bluePos, orangePos,
            blueActions, orangeActions, currentAction,
            blueCurrentAction, orangeCurrentAction,
            blueButtons[MAX_ACTIONS_PER_TEST], orangeButtons[MAX_ACTIONS_PER_TEST],
            actionsCompleted;
    BotType botOrder[MAX_ACTIONS_PER_TEST];

    //Introduce the program to the user
    cout    << "Bot Trust - Trent Reed 2011" << endl << endl;

    //Prompt for input until a file is opened
    do {
        cout << "Please enter a file to open: ";
        cin.getline(filename, MAX_FILENAME_LENGTH);
        inputFile.open(filename, ios_base::in);
        if(inputFile.is_open())
            break;
        cout << "ERROR: Invalid filename or file not found!" << endl << endl;
    }while(!inputFile.is_open());

    //Delete old output.txt and open a new one for editing.
    remove("output.txt");
    outputFile.open("output.txt", ios_base::out);

    //Handle error opening file
    if(!outputFile.is_open()) {
        cout << "ERROR: Output file output.txt could not be opened for editing." <<
                "Please make sure the file has proper permissions or is not marked" <<
                "as read-only!";
        return 1;
    }

    inputFile >> tests;

    for(int count = 0; count < tests; count++) {
        //Reset Variables
        currentTime = 0;
        currentAction = 0;
        bluePos = 1;
        orangePos = 1;
        blueActions = 0;
        orangeActions = 0;
        blueCurrentAction = 0;
        orangeCurrentAction = 0;

        //Parse to seperate moves
        inputFile >> actionsInCurrentTest;
        for(int action = 0; action < actionsInCurrentTest; action++) {
            inputFile >> botIdentifier;
            switch(botIdentifier) {
                case 'b':
                case 'B':
                    botOrder[action] = BOT_BLUE;
                    inputFile >> blueButtons[blueActions];
                    blueActions++;
#if DEBUG == true
                    cout << "Action " << action + 1 << ": Blue -> " << blueButtons[blueActions - 1] << endl;
#endif
                    break;
                case 'o':
                case 'O':
                    botOrder[action] = BOT_ORANGE;
                    inputFile >> orangeButtons[orangeActions];
                    orangeActions++;
#if DEBUG == true
                    cout << "Action " << action + 1 << ": Orange -> " << orangeButtons[orangeActions - 1] << endl;
#endif
                    break;
            }
        }

        //Find shortest time
        do{
            buttonPressed = false;
            if(blueCurrentAction < blueActions)
                if(bluePos > blueButtons[blueCurrentAction])
                    bluePos--;
                else if (bluePos < blueButtons[blueCurrentAction])
                    bluePos++;
                else if (botOrder[currentAction] == BOT_BLUE) {
                    blueCurrentAction++;
                    currentAction++;
                    buttonPressed = true;
                }
            if(orangeCurrentAction < orangeActions)
                if(orangePos > orangeButtons[orangeCurrentAction])
                    orangePos--;
                else if (orangePos < orangeButtons[orangeCurrentAction])
                    orangePos++;
                else if (!buttonPressed && botOrder[currentAction] == BOT_ORANGE) {
                    orangeCurrentAction++;
                    currentAction++;
                }
            currentTime++;
        } while (currentAction < actionsInCurrentTest);

        //Record Time
#if DEBUG == true
                    cout << "Case #" << count + 1 << ": " << currentTime << endl;
#endif
        outputFile << "Case #" << count + 1 << ": " << currentTime << endl;
    }

    //Display a message stating the file was parsed correctly, and exit.
    cout << "File successfully parsed! Please review output.txt to see the answers." << endl;
    return 0;
}

