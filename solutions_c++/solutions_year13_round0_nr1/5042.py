#include <stdio.h>
#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

inline unsigned int convertToBits(const char *str, char value)
{
    int t = 0;
    for (int i=0;str[i]!=0;++i)
    {
        t |= ( ((str[i] == value)|(str[i]=='T')) << i);
    }
    return t;
}

inline bool checkItemWon(unsigned short int a)
{
    int solutionVector[] = { 0x000f, 0x00f0, 0x0f00, 0xf000, 0x1111, 0x2222, 0x4444, 0x8888, 0x1248, 0x8421 };

    for (int i=0;i<sizeof(solutionVector)/sizeof(int);++i) 
    {
        if ((a&solutionVector[i]) == solutionVector[i])
        {
            return true;
        }
    }
    return false;
}

int main(int argc, char *args[])
{
    int nr;
    cin >> nr;

    string adi;


    for (int caseNr=1;caseNr<=nr;++caseNr)
    {
        unsigned short int x = 0;
        unsigned short int o = 0;
        
        x = 0;
        o = 0;
        for (int i=0;i<4;++i)
        {
            cin >> adi;
            x |= convertToBits(adi.c_str(), 'X') << 4*i;
            o |= convertToBits(adi.c_str(), 'O') << 4*i;
        } 
        
        bool possibleDraw = ((x | o) == 0xffff);
        cout << "Case #" << caseNr << (checkItemWon(x) ? ": X won" : (checkItemWon(o) ? ": O won" : (possibleDraw ? ": Draw" : ": Game has not completed" ))) << "\n"; 
    }
    return 0;
}
