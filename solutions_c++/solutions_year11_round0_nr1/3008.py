#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int sgn(int x)
{
    return x > 0 ? 1 : (x < 0 ? -1 : 0);
}

int main()
{
    int nTests;
    cin >> nTests;
    for (int test = 0; test < nTests; test++)
    {
        int n;
        cin >> n;

        vector< pair<char, int> > acts(n);
        for (int i = 0; i < n; i++)
            cin >> acts[i].first >> acts[i].second;

        vector<int> nextBluePos(n, -1), nextOrangePos(n, -1);
        for (int i = 0; i < n; i++)
        {
            for (int j = i; j < n; j++)
                if (acts[j].first == 'B')
                {
                    nextBluePos[i] = acts[j].second; 
                    break;
                }
            for (int j = i; j < n; j++)
                if (acts[j].first == 'O')
                {
                    nextOrangePos[i] = acts[j].second; 
                    break;
                }
        }

        int oPos = 1, bPos = 1, curAct = 0, t = 0;
        while (curAct != n)
        {
            bool actionDone = false;

            if (acts[curAct].first == 'O' && oPos == acts[curAct].second)
                actionDone = true;   
            else 
            {
                int next = nextOrangePos[curAct];
                if (next != -1) oPos += sgn(next - oPos);
            }

            if (acts[curAct].first == 'B' && bPos == acts[curAct].second)
                actionDone = true;
            else
            {
                int next = nextBluePos[curAct];
                if (next != -1) bPos += sgn(next - bPos);
            }

            if (actionDone) curAct++;
            t++;
        }

        printf("Case #%d: %d\n", test + 1, t);
    }

    return 0;
}