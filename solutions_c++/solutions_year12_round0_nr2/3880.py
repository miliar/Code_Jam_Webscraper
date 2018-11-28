#include <iostream>

using namespace std;

int main()
{
    int tetC;
    cin >> tetC;
    for(int cnt = 1; cnt <= tetC; cnt++)
    {
            int numG;
            int tChn;
            int wN;
            cin >> numG;
            cin >> tChn;
            cin >> wN;
            int res = 0;
            for(int gCnt = 0; gCnt < numG; gCnt++)
            {
                    int curT;
                    cin >> curT;
                    if(curT == 0)
                    {
                            if(wN == 0)
                            {
                                  res++;
                                  continue;
                            }      
                    }
                    else if(curT >= (wN*3 - 2))
                    {
                            res++;
                            continue; 
                    } 
                    else if(curT < (wN*3 - 4))
                    {
                         continue;
                    }
                    else if(tChn > 0 && (curT == (wN*3 - 3) || curT == (wN*3 - 4)))
                    {
                         res++;
                         tChn--;
                         continue;
                    }
            }               
            cout << "Case #" << cnt << ": " << res << endl; 
            
    }
    return 0;
}
