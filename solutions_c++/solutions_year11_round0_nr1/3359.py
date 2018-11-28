/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Moritz Schaefer (), mollitz@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

struct Data
{
    bool player; // false is O true is B
    int position;
};


class Robot
{
public:
    Robot(int target) 
    {
        position = 1;
        hasPressed = false;
        this->target = target;

    }

    bool step(bool pressFree)
    {
        if(position == target)
        {
            if(!hasPressed && pressFree)
            {
                hasPressed = true; //Press
                return true;
                //Do nothing else now...
            }
        }
        else
        {
            //Walk now
            if(target > position)
                position++;
            else
                position--;
        }
        return false;
    }

    int getPosition()
    {
        return position;
    }

    bool outOfWork() 
    {
        return hasPressed;
    }

    void setTarget(int newTarget)
    {
        target = newTarget;
        hasPressed = false;
    }


private:
    bool hasPressed;
    int position;
    int target;
};

void preCalculation()
{}


int nextTarget(const vector<Data> &data, int i, bool player)
{
    for(; i < data.size(); i++)
    {
        if(data[i].player == player)
            return data[i].position;
    }
    return 0;
}

string calculate()
{
    int count;
    cin >> count;
    vector<Data> data(count);
    for(int i=0; i<count; i++)
    {
        char player;
        cin >> player;
        data[i].player = (player == 'B');
        int position;
        cin >> position;
        data[i].position = position;
    }

    Robot orange(nextTarget(data, 0, false));
    Robot blue(nextTarget(data, 0, true));

    int i = 0;
    int sec = 0;
    while(i < count)
    {

       bool currentRobot = data[i].player;

       if(orange.step(!currentRobot))
       {
           i++;
           orange.setTarget(nextTarget(data, i, false));
      }
       if(blue.step(currentRobot))
       {
           i++;
           blue.setTarget(nextTarget(data, i, true));
       }
       sec++;
    }

    stringstream s;
    s << sec;

    return s.str();
}



int main(int argc, char *argv[])
{
    int cases;
    cin >> cases;
    preCalculation();
    for(int i = 0; i < cases; i++)
    {
        cout << "Case #" << i+1 << ": " << calculate() << endl;
    }
    return 0;
}
