#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

enum ERobot
{
    Blue = 66,
    Orange = 79
};

struct Waypoint
{
    ERobot robot;
    unsigned int place;
};

Waypoint* findNextWaypoint(const vector<Waypoint*> &waypoints, int currentMove)
{
    ERobot currentRobot = waypoints[currentMove]->robot;
    ERobot nextRobot = (currentRobot == Blue) ? Orange : Blue;

    for (unsigned int i = currentMove + 1; i < waypoints.size(); i++)
    {
        if (waypoints[i]->robot == nextRobot)
            return waypoints[i];
    }

    return 0;
}

int main()
{
    ifstream input("input.dat");
    ofstream output("output.dat");

    if (!input.good())
    {
        cout << "Error while reading the file.";
        return 1;
    }

    Waypoint oBot;
    Waypoint bBot;

    vector<Waypoint*> waypoints;

    oBot.robot = Orange;
    oBot.place = 1;
    bBot.robot = Blue;
    bBot.place = 1;

    int n, cnt, i;
    int currentMove = 0;
    int time = 0;
    // helpers
    char robot; unsigned int place;
    string debugBot;
    Waypoint *currentRobot,
             *currentWaypoint,
             *nextRobotWaypoint;

    // start reading
    input >> n;

    int cn = n;

    while (cn--)
    {
        waypoints.clear();
        input >> cnt;

        // read waypoints
        for (i = 0; i < cnt; i++)
        {
            input >> robot >> place;
            
            Waypoint* waypoint = new Waypoint;
            waypoint->robot = (ERobot)robot;
            waypoint->place = place;

            //cout << robot << " " << place << " ";

            waypoints.push_back(waypoint);
        }

        //cout << endl;
        
        // start processing
        time = 0;
        currentMove = 0;
        oBot.place = 1;
        bBot.place = 1;

        while (currentMove != waypoints.size())
        {
            time++;
            currentWaypoint = waypoints[currentMove];
            nextRobotWaypoint = findNextWaypoint(waypoints, currentMove);

            if (currentWaypoint->robot == Blue)
            {
                currentRobot = &bBot;
                debugBot = "Blue";
            }
            else
            {
                currentRobot = &oBot;
                debugBot = "Orange";
            }

            if (currentRobot->place == currentWaypoint->place)
            {
                // push button
                //cout << debugBot << " pushes button at " << currentRobot->place << endl;
                currentMove++;
            }

            // move the robot
            if (currentRobot->place > currentWaypoint->place)
            {
                currentRobot->place--;
                //cout << debugBot << " moves to " << currentRobot->place << endl;
            }
            else if (currentRobot->place < currentWaypoint->place)
            {
                currentRobot->place++;
                //cout << debugBot << " moves to " << currentRobot->place << endl;
            }

            // if we have a next waypoint do the same but without pushing a button
            if (nextRobotWaypoint)
            {
                if (nextRobotWaypoint->robot == Blue)
                {
                    currentRobot = &bBot;
                    debugBot = "Blue";
                }
                else
                {
                    currentRobot = &oBot;
                    debugBot = "Orange";
                }

                if (currentRobot->place > nextRobotWaypoint->place)
                {
                    currentRobot->place--;
                    //cout << debugBot << " moves to " << currentRobot->place << endl;
                }
                else if (currentRobot->place < nextRobotWaypoint->place)
                {
                    currentRobot->place++;
                    //cout << debugBot << " moves to " << currentRobot->place << endl;
                }
                else
                {
                    //cout << debugBot << " stays at " << currentRobot->place << endl;
                }
            }
        }

        //cout << endl << "Finished in " << time << " seconds." << endl << endl;
        output << "Case #" << n - cn << ": " << time << "\n";

        // memory cleanup
        for (i = 0; i < waypoints.size(); i++)
            delete waypoints[i];
    }

    input.close();
    output.close();

    return 0;
}