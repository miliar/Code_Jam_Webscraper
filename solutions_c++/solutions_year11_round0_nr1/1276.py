#include <iostream>

const int MAX_CASES = 100; // as per limits of large dataset
const int MAX_STEPS = 100; // as per limits of large dataset
const int MAX_BUTTONS = 100; // as per test description

enum BotId { BOT_ORANGE, BOT_BLUE, MAX_BOT };

struct Step
{
    BotId bot;
    int button;
};

struct Case
{
    int numSteps;
    Step steps[MAX_STEPS];
};

struct Test
{
    int runTime;
    int atButton[MAX_BOT];
    int lastEvent[MAX_BOT];
};

namespace {
Case cases[MAX_CASES];
Test results[MAX_CASES];
}

int main()
{
    int numCases = 0;
    std::cin >> numCases;

    for(int i = 0; i < numCases; i++)
    {
        std::cin >> cases[i].numSteps;
        for(int n = 0; n < cases[i].numSteps; n++)
        {
            char botChar;
            std::cin >> botChar;
            cases[i].steps[n].bot = (botChar == 'B') ? BOT_BLUE : BOT_ORANGE;
            std::cin >> cases[i].steps[n].button;
        }
    }

    for(int i = 0; i < numCases; i++)
    {
        results[i].runTime = 0;
        for(int n = 0; n < MAX_BOT; n++)
        {
            results[i].lastEvent[n] = 0;
            results[i].atButton[n] = 1;
        }

        std::cout << "Case #" << (i+1) << ": ";
        for(int n = 0; n < cases[i].numSteps; n++)
        {
            int botNum = cases[i].steps[n].bot;
            int totalTravel = abs(cases[i].steps[n].button - results[i].atButton[botNum]);
            int alreadyTraveled = results[i].runTime - results[i].lastEvent[botNum];
            if (alreadyTraveled > totalTravel) { alreadyTraveled = totalTravel; }

            // total step time includes travel-time + button press
            int thisTime = totalTravel - alreadyTraveled + 1;
            results[i].runTime += thisTime;
            results[i].atButton[botNum] = cases[i].steps[n].button;
            results[i].lastEvent[botNum] = results[i].runTime;
        }
        std::cout << results[i].runTime << std::endl;
    }
}
