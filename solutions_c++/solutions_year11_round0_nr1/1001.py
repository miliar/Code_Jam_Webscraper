#include <vector>
#include <iostream>

using namespace std;


static const int MaxButtonNum = 100;

int testNum;
int buttonNum;
int maxO;
int maxB;
int testIndex;
char color[MaxButtonNum];
int pos[MaxButtonNum];

void readInput()
{
    //cout << "Test " << testIndex << "\n";
    cin >> buttonNum;
    //cout << buttonNum;
    for (int i = 0;i < buttonNum; ++i)
    {
        cin >> color[i] >> pos[i];
        //cout << " " << color[i] << " " << pos[i]; 
    }
    //cout << "\n";
}

void init()
{
}

int findTarget( int button, char targetColor )
{
    for (int i = button; i < buttonNum; ++i)
        if (color[i] == targetColor)
            return pos[i];
    return -1;
}

void move( int &current, int target )
{
    if (target == -1 || current == target) return;
    if (current < target) ++current;
    else --current;
    return;
}


void compute()
{
    int total = 0;
    int currentO = 1;
    int currentB = 1;
    for (int i = 0; i < buttonNum;++i)
    { 
        int targetO = findTarget( i, 'O' );
        int targetB = findTarget( i, 'B' );
        //cout << "Button " << i << ": targetO = " << targetO << ",";
        //cout << "targetB = " << targetB << ", total = " << total << ",";
        //cout << "currentO = " << currentO << ", currentB = " << currentB << "\n";
        while ((color[i] == 'O' && currentO != targetO) ||
               (color[i] == 'B' && currentB != targetB))
        {
            move(currentO, targetO);
            move(currentB, targetB);
            ++total;            
        }
        if (color[i] == 'O') move( currentB, targetB );
        else move( currentO, targetO );
        ++total;
    }
    cout << "Case #" << testIndex << ": " << total << "\n";
}

int main()
{
    cin >> testNum;   
    for (testIndex = 1; testIndex <= testNum; ++testIndex)
    {        
        readInput();
        init();
        compute();
    }
}
