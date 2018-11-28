#include <iostream>

using namespace std;

inline int dist(int a, int b) {
    return (a > b) ? (a - b) : (b - a);
}
inline int max2(int a, int b) {
    return (a > b) ? a : b;
}

int main()
{
    int coden, t;
    cin >> t;
    // define vars
    //char robot[102];
    //int n[102];
    int buttonnum;

    for (coden = 1; coden <= t; coden++)
    {
        char robotid;
        int buttonpos;
        int robotPos[2] = {1, 1};
        int robotTime[2] = {0, 0}; // last event finish at this time
        int id; // robot id
        int eventtime = 1; // sequent events starts at/after this time
        int nexteventtime;
        cin >> buttonnum;
        for (int i = 0; i < buttonnum; i++) {
            cin >> robotid;
            cin >> buttonpos;
            if (robotid == 'O') {
                id = 0;
            } else {
                id = 1;
            }

            // move robot here
            nexteventtime = robotTime[id] + dist(buttonpos, robotPos[id]) + 1; // move and push button, finish after this time
            //cerr << "Robot #" << id << "move " << endl;

            eventtime = max(nexteventtime, eventtime) + 1; // add 1 means next action could start at that time
            // last action ends after nexteventtime(move and pushbutton)
            // or after eventtime(wait and pushbutton at eventtime)
            robotPos[id] = buttonpos;
            robotTime[id] = eventtime - 1;
        }

        // output result
        cout << "Case #" << coden << ": " << (eventtime - 1) << endl;
    }
    return 0;
}

