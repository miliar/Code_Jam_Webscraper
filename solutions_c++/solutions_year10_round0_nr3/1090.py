#include <time.h>
#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
    fstream fIn, fOut;
    fIn.open("C-large.in", fstream::in);
    fOut.open("Output.txt", fstream::out);

    int caseNum = 0;
    fIn >> caseNum;
    
    for(int i = 0; i < caseNum; i++)
    {
        long long g[1000][3];
        int r, k, n;
        r = k = n = 0;
        fIn >> r >> k >> n;
        for(int j = 0; j < n; j++)
        {
            fIn >> g[j][0];
            g[j][1] = g[j][2] = -1;
        }

        /*
        cout << i << endl;
        cout << r << " " << k << " " << n << endl;
        for(int j = 0; j < n; j++)
        {
            cout << g[j][0] << " ";
        }
        cout << endl;
        */
        
        long long money = 0;
        long long round = 0;
        int id = 0;
        int group = 0;
        long long people = 0;

        while(g[id][1] == -1 && round < r)
        {
            g[id][1] = round;
            g[id][2] = money;

            group = 0;
            people = 0;

            while((people + g[id][0] <= k) && group < n)
            {
                people += g[id][0];
                money += g[id][0];
                id++;
                group++;
                if(id == n)
                    id = 0;
            }
        
            round++;
        }
        /*
        cout << id << " "
            << g[id][1] << " " << g[id][2] << " "
            << round << " " << money << endl;
            */

        int rep = (r - round) / (round - g[id][1]);
        round = round + (round - g[id][1]) * rep;
        money = money + (money - g[id][2]) * rep;

        //cout << rep << " " << round << " " << money << endl;

        while(round < r)
        {
            group = 0;
            people = 0;

            while((people + g[id][0] <= k) && group < n)
            {
                people += g[id][0];
                money += g[id][0];
                id++;
                group++;
                if(id == n)
                    id = 0;
            }
        
            round++;
        }

        fOut << "Case #" << i + 1 << ": " << money << endl;

    }

    fIn.close();
    fOut.close();

    return 0;
}
