#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstdlib>
using namespace std;

int main(void)
{
    int n;
    string fileName = "A-large";
    string finName = fileName + ".in";
    string foutName = fileName + ".out";
    ifstream fin(finName.c_str());
    ofstream fout(foutName.c_str());
    fin >> n;
    for (int caseID = 1; caseID <= n; caseID++)
    {
        int m;
        fin >> m;
        //sequence: 1xxx for orange, 2xxx for blue
        vector<int> seq;
        vector<int> sO;
        vector<int> sB;
        char temp1;
        int temp2;
        for (int i = 0; i < m; i++)
        {
            fin >> temp1;
            fin >> temp2;
            if (temp1 == 'O')
            {
                sO.push_back(temp2);
                seq.push_back(temp2 + 1000);
            }
            else
            {
                sB.push_back(temp2);
                seq.push_back(temp2 + 2000);
            }
        }
        int buttons = m;
        int ans = 0;
        int bO = 0;
        int buttonO = 0;
        if (bO != sO.size()) buttonO = sO[bO];
        int bB = 0;
        int buttonB = 0;
        if (bB != sB.size()) buttonB = sB[bB];
        int rO = 1;
        int rB = 1;
        int c = 0;
        int current = seq[c];
        while (buttons > 0)
        {
            bool pressed = false;
            if (bO < sO.size())
            {
                if (rO == buttonO)
                {
                    //if the robot is at its place for button,
                    //check if it needs to wait for other robot
                    if (current <= 2000)
                    {
                        bO++;
                        buttonO = sO[bO];
                        c++;
                        current = seq[c];
                        buttons--;
                        pressed = true;
                    }
                }
                else
                {
                    if (rO < buttonO)
                    {
                        rO++;
                    }
                    else
                    {
                        if (rO > buttonO)
                        {
                            rO--;
                        }
                    }
                }
            }
            if (bB < sB.size())
            {
                if (rB == buttonB)
                {
                    //if the robot is at its place for button,
                    //check if it needs to wait for other robot
                    if (!pressed)
                    {
                        if (current > 2000)
                        {
                            bB++;
                            buttonB = sB[bB];
                            c++;
                            current = seq[c];
                            buttons--;
                        }
                    }
                }
                else
                {
                    if (rB < buttonB)
                    {
                        rB++;
                    }
                    else
                    {
                        if (rB > buttonB)
                        {
                            rB--;
                        }
                    }
                }
            }
            cout << rO << " " << rB << " " << bO << " " << bB << endl;
            ans++;
        }
        cout << "Case #" << caseID << ": " << ans << endl;
        fout << "Case #" << caseID << ": " << ans << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
