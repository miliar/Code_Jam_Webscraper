#include <WTypes.h>
#include <stdlib.h>
#include <ctype.h>
#include "stdio.h"
#include "string.h"
#include <vector>
using namespace std;

enum {MAX_STEPS = 100};
enum {MAX_LINE = 5*MAX_STEPS + 5};
char Line[MAX_LINE];

class Target
{
public:
    char Robot;
    int  Button;
};

class Robot
{
public:
    Robot() 
    {
        m_currPos = 1;
        m_target = 0;
    }

    void SetTarget(int pos)
    {
        m_target = pos;
    }

    // Return true is target was pressed
    bool Move()
    {
        if (m_currPos == m_target)
            return true;

        if (m_currPos < m_target)
            ++m_currPos;
        else
            --m_currPos;

        return false;
    }

private:
    int m_currPos;
    int m_target;

};

typedef vector<Target> TargetsArray;


int readNumLine(FILE* a_hInput)
{
    char* ret = fgets(Line, MAX_LINE, a_hInput);
    if (ret == NULL)
        return 0;

    int num; 
    sscanf_s(Line, "%d", &num);
    return num;
}

static char* next_token;
char* ReadNextToken()
{
    return strtok_s(NULL, " ", &next_token);
}

// Returns the num of steps
int readCase(FILE* a_hInput, TargetsArray& a_rTargets)
{
    char* ret = fgets(Line, MAX_LINE, a_hInput);
    if (ret == NULL)
        return 0;

    int numSteps;
    sscanf_s(Line, "%d", &numSteps);
    if ((numSteps > MAX_STEPS) || (numSteps < 1))
    {
        printf("illegal num of steps");
        return 0;
    }

    Target newTarget;
    char* token = strtok_s(Line, " ", &next_token);     
    for (int i=0; i<numSteps; i++)
    {
        token = ReadNextToken();
        newTarget.Robot = toupper(*token);

        token = ReadNextToken();
        newTarget.Button = atoi(token);

        a_rTargets.push_back(newTarget);
    }

    return numSteps;
}


void setOtherTarget(Robot* a_pRobot, TargetsArray& a_rTargets, UINT a_posInArray)
{
    char currRobot = a_rTargets[a_posInArray].Robot;
    a_posInArray++;

    while (a_posInArray < a_rTargets.size() )
    {
        if (a_rTargets[a_posInArray].Robot != currRobot)
        {
            a_pRobot->SetTarget(a_rTargets[a_posInArray].Button);
            return;
        }

        ++a_posInArray;
    }
}

// Return min num of steps
int calcSteps(TargetsArray& a_rTargets)
{
    UINT posInArray = 0;
    int numOfSteps = 0;
    bool fSetNewTarget = true;

    Robot R_Orange;
    Robot R_Blue;
    Robot* pActiveRobot = NULL;
    Robot* pOtherRobot = NULL;

    while (posInArray < a_rTargets.size())
    {
        numOfSteps++;
        
        if (fSetNewTarget)
        {
            fSetNewTarget = false;

            if (a_rTargets[posInArray].Robot == 'O')
            {
                pActiveRobot = &R_Orange;
                pOtherRobot  = &R_Blue;
            }
            else
            {
                pActiveRobot = &R_Blue;
                pOtherRobot  = &R_Orange;
            }

            pActiveRobot->SetTarget(a_rTargets[posInArray].Button);
            setOtherTarget(pOtherRobot, a_rTargets, posInArray);
        }

        bool fTargetDone = pActiveRobot->Move();
        pOtherRobot->Move();

        if (fTargetDone)
        {
            fSetNewTarget = true;
            ++posInArray;
        }
    }

    return numOfSteps;
}

void Run(char* a_inputFile)
{
    FILE* hInput;
    errno_t err = fopen_s(&hInput, a_inputFile, "r");
    if (err != 0)
        return;

    int T = readNumLine(hInput);  // num of cases
    TargetsArray targets;

    for (int i=0; i < T; i++)
    {
        targets.clear();
        int N = readCase(hInput, targets);   // N = buttons to press

        int minSteps = calcSteps(targets);
        printf("Case #%d: %d\n", i+1, minSteps);
    }
}

void main()
{
    //Run(".\\A-small-robot.in");
    //Run(".\\A-small-attempt0.in");
    Run(".\\A-large-robots.in");
    system("Pause");
}

