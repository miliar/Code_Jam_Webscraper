#include <iostream>
#include <utility>

using namespace std;

const int c_maxInstructions(100);

enum RobotColor
{
    ORANGE,
    BLUE
};

typedef std::pair<RobotColor, int> Instruction;

struct Robot
{
    Robot(RobotColor p_color) :
        m_color(p_color),
        m_position(1)
    {
    }

    RobotColor m_color;
    int m_position;
};

int runTestCase(const Instruction *const p_instructionArray,
    const int p_numInstructions)
{
    Robot orangeRobot(ORANGE);
    Robot blueRobot(BLUE);

    const Instruction* nextInstruction(p_instructionArray);
    const Instruction* endOfSequence(p_instructionArray + p_numInstructions);
    const Instruction* nextBlueInstruction(p_instructionArray);
    const Instruction* nextOrangeInstruction(p_instructionArray);
    for (; (nextOrangeInstruction < endOfSequence) && (nextOrangeInstruction->first != ORANGE); ++nextOrangeInstruction );
    for (; (nextBlueInstruction < endOfSequence) && (nextBlueInstruction->first != BLUE); ++nextBlueInstruction );

    int time(0);
    for (; nextInstruction < endOfSequence; ++time)
    {
        bool instructionCompleted(false);
        if ( orangeRobot.m_position > nextOrangeInstruction->second )
        {
            --orangeRobot.m_position;
        }
        else if ( orangeRobot.m_position < nextOrangeInstruction->second )
        {
            ++orangeRobot.m_position;
        }
        else
        {
            // Pressing the button
            if ( nextOrangeInstruction == nextInstruction )
            {
                instructionCompleted = true;
                ++nextOrangeInstruction;
                for (; (nextOrangeInstruction < endOfSequence) && (nextOrangeInstruction->first != ORANGE); ++nextOrangeInstruction );
            }
        }

        if ( blueRobot.m_position > nextBlueInstruction->second )
        {
            --blueRobot.m_position;
        }
        else if ( blueRobot.m_position < nextBlueInstruction->second )
        {
            ++blueRobot.m_position;
        }
        else
        {
            // Pressing the button
            if ( nextBlueInstruction == nextInstruction )
            {
                instructionCompleted = true;
                ++nextBlueInstruction;
                for (; (nextBlueInstruction < endOfSequence) && (nextBlueInstruction->first != BLUE); ++nextBlueInstruction );
            }
        }

        if ( instructionCompleted )
        {
            ++nextInstruction;
        }
    }
    return time;
}

int main(int argc, char* argv[])
{
    int numTestCases(0);
    cin >> numTestCases;

    Instruction sequence[c_maxInstructions];
    for ( int i = 1; i <= numTestCases; ++i )
    {
        int numInstructions(0);
        char color;
        int buttonNumber;

        // Read in our test case
        cin >> numInstructions;
        for ( int j = 0; j < numInstructions; ++j )
        {
            cin >> color;
            cin >> buttonNumber;
            if ( color == 'O' )
                sequence[j].first = ORANGE;
            else if ( color == 'B' )
                sequence[j].first = BLUE;
            else
                cerr << "ERROR: invalid robot color" << endl;
            if ( buttonNumber >= 1 && buttonNumber <= 100)
                sequence[j].second = buttonNumber;
            else
                cerr << "ERROR: invalid robot number" << endl;
        }

        // Run our test case
        int runTime = runTestCase(&sequence[0], numInstructions);

        // Output the results of our test case
        cout << "Case #" << i << ": " << runTime << endl;
    }
    return 0;
}

