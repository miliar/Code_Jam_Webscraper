#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
    int t,n;

    cin>>t;

    for (int i =0;i<t;i++)
    {
        cin>>n;

        int bt=0,prevBt=0,currPosB=1,currPosO=1,prevNumOfMoves=0,numOfMovesB=0,numOfMovesO=0;
        char bot,prevBot;
        int times=0;

        for(int k=0;k<n;k++)
        {
            cin>>bot>>bt;

            if(k==0)
            {
                prevBot = bot;
                prevBt = bt;
                times = bt;

                if(bot=='B')
                {
                    currPosB = bt;
                }
                else if(bot=='O')
                {
                    currPosO = bt;
                }
                prevNumOfMoves = bt;
                continue;
            }

            if(bot=='B')
            {

                numOfMovesB = abs(currPosB-bt)+1;
                if(prevBot=='B')
                {
                    prevNumOfMoves += numOfMovesB;
                    times += numOfMovesB;
                }
                else
                {
                    if(prevNumOfMoves>=numOfMovesB)
                    {
                        times++;
                        prevNumOfMoves = 1;
                    }
                    else
                    {
                        times+=(numOfMovesB-prevNumOfMoves);
                        prevNumOfMoves = (numOfMovesB-prevNumOfMoves);
                    }
                }
                currPosB = bt;
            }
            else if(bot=='O')
            {
                numOfMovesO = abs(currPosO-bt)+1;
                if(prevBot=='O')
                {
                    prevNumOfMoves +=numOfMovesO;
                    times += numOfMovesO;
                }
                else
                {
                    if(prevNumOfMoves>=numOfMovesO)
                    {
                        times++;
                        prevNumOfMoves = 1;
                    }
                    else
                    {
                        times+=(numOfMovesO-prevNumOfMoves);
                        prevNumOfMoves = (numOfMovesO-prevNumOfMoves);
                    }
                }
                currPosO = bt;
            }
            prevBot = bot;
        }
        cout<<"Case #"<<(i+1)<<": "<<times<<endl;
    }
    return 0;
}
