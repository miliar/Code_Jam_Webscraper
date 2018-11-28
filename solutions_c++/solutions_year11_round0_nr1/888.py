#include <stdio.h>
#include <assert.h>
#include <string.h>

int T;              // no of test cases

int N;              // no of buttons to press
char robot[2000];   // the robot who presses the button
int button[2000];   // the button that needs to be pressed

int time;           // total time needed to press all buttons

// gets the next (after kth button press) door number to be pressed for the color
int getNextButton(int k, char color)
{
    for(int i=k;i<N;i++)
        if(robot[i] == color) return button[i];

    return N+1;
}

void emulateRobots()
{

    char currentTurn = robot[0];
    int curOPos = 1, curBPos = 1;
    int i = 0;
    int nextOButton = getNextButton(i, 'O');
    int nextBButton = getNextButton(i, 'B');

    time = 0;
    while (i < N)
    {
        bool ODone = false, BDone = false;
        if(nextOButton == curOPos && currentTurn == 'O')
        {
            i++;
            nextOButton = getNextButton(i, 'O');
            currentTurn = robot[i];
            ODone = true;
        }
        else if(nextBButton == curBPos && currentTurn == 'B')
        {
            i++;
            nextBButton = getNextButton(i, 'B');
            currentTurn = robot[i];
            BDone = true;
        }
        if(!ODone)
        {
            if(nextOButton > curOPos) curOPos++;
            if(nextOButton < curOPos) curOPos--;
        }
        if(!BDone)
        {
            if(nextBButton > curBPos) curBPos++;
            if(nextBButton < curBPos) curBPos--;
        }
        time++;
    }

}

int main()
{
    FILE *fp = fopen("c:\\inp.txt", "r+"); // get input data from file
    fscanf(fp, "%d", &T);

    FILE *fpo = fopen("c:\\op.txt", "w+"); // write op data to file

    for(int c=1;c<=T;c++)    // process each test case
    {
        fscanf(fp, "%d", &N);
        for(int i=0;i<N;i++)
            fscanf(fp, "%s %d", &robot[i], &button[i]);

        emulateRobots();
        fprintf(fpo, "Case #%d: %d\n", c, time);
    }

    fclose(fp);
    fclose(fpo);
    return 0;
}

