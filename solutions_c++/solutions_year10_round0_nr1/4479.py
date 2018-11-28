#include <iostream>
#include <fstream>
using namespace std;

int main(void)
{
    fstream input;
    fstream output;
    input.open ("A-small-attempt0.in", fstream::in);
    output.open ("output.txt", fstream::out);
    int CaseNum=0;
    input >> CaseNum;
    for(int CaseCount=1; CaseCount<=CaseNum; CaseCount++)
    {
        int SnapperNum = 0, ClickTimes = 0;
        input >> SnapperNum >> ClickTimes;
        bool SnapperStatus[SnapperNum];
        for(int i=0; i<SnapperNum; i++)
            SnapperStatus[i]=false;
        for(int ClickCount=0; ClickCount<ClickTimes; ClickCount++)
        {
            for(int SnapperCount=0; SnapperCount<SnapperNum; SnapperCount++)
            {
                if(SnapperStatus[SnapperCount]==true)
                {
                    SnapperStatus[SnapperCount]=false;
                    continue;
                }
                else
                {
                    SnapperStatus[SnapperCount]=true;
                    break;
                }
            }
        }
        bool LightStatus=true;
        for(int SnapperCount=0; SnapperCount<SnapperNum; SnapperCount++)
            if(SnapperStatus[SnapperCount]==false)
                LightStatus=false;
        output << "Case #" << CaseCount << ": ";
        if(LightStatus)
            output << "ON" << endl;
        else
            output << "OFF" << endl;
    }
    return 0;
}
