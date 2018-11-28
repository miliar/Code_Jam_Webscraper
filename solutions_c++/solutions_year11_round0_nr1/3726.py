#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t, n;
    vector<int> orange;
    vector<int> blue;

    cin >> t;

    for (int it = 1; it <= t; it++)
    {
        int positionOrange;
        int positionBlue;
        int slackOrange;
        int slackBlue;
        int totalSteps;

        cin >> n;
        positionOrange = positionBlue = 1;
        slackOrange = slackBlue = 0;
        totalSteps = 0;

        for (int i = 0; i < n; i++)
        {
            char bot;
            int button;
            int dist;

            cin >> bot >> button;
            if (bot == 'O')
            {
                dist = button > positionOrange ? button - positionOrange : positionOrange - button;
                dist -= slackOrange;
                if (dist < 0) dist = 0;
                totalSteps += 1 + dist;
                slackBlue += 1 + dist;
                slackOrange = 0;
                positionOrange = button;
            } else {
                dist = button > positionBlue ? button - positionBlue : positionBlue - button;
                dist -= slackBlue;
                if (dist < 0) dist = 0;
                totalSteps += 1 + dist;
                slackOrange += 1 + dist;
                slackBlue = 0;
                positionBlue = button;
            }
        }

        cout << "Case #" << it << ": " << totalSteps << endl;
    }

    return 0;
}
