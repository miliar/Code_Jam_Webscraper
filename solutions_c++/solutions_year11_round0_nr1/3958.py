

#include <iostream>
#include <map>
#include <vector>
using namespace std;


int Sign(int n)
{
    if(n < 0) return -1;
    if(n == 0) return 0;
    return 1;
}


int Simulate(const vector<int>& orange_queue, const vector<int>& blue_queue, const vector<bool>& orange_turns, int orange_index, int blue_index, int orange_position, int blue_position, int turn, int time)
{
    int orange_direction = 0;
    if(orange_index != orange_queue.size())
    {
        orange_direction = Sign(orange_queue[orange_index] - orange_position);
    }
    int blue_direction = 0;
    if(blue_index != blue_queue.size())
    {
        blue_direction = Sign(blue_queue[blue_index] - blue_position);
    }
    if(orange_index == orange_queue.size() && blue_index == blue_queue.size())
    {
        return time;
    }
    else if(orange_index != orange_queue.size() && orange_queue[orange_index] == orange_position && orange_turns[turn] == true)
    {
        return Simulate(orange_queue, blue_queue, orange_turns, orange_index + 1, blue_index,
            orange_position, blue_position + blue_direction, turn + 1, time + 1);
    }
    else if(blue_index != blue_queue.size() && blue_queue[blue_index] == blue_position && orange_turns[turn] == false)
    {
        return Simulate(orange_queue, blue_queue, orange_turns, orange_index, blue_index + 1,
            orange_position + orange_direction, blue_position, turn + 1, time + 1);
    }
    else
    {
        return Simulate(orange_queue, blue_queue, orange_turns, orange_index, blue_index,
            orange_position + orange_direction, blue_position + blue_direction, turn, time + 1);
    }
}


int main()
{
    int cases;
    cin >> cases;
    
    for(int i = 0; i < cases; i++)
    {
        int buttons;
        cin >> buttons;
        vector<int> orange_queue;
        vector<int> blue_queue;
        vector<bool> orange_turns;
        for(int j = 0; j < buttons; j++)
        {
            string color;
            int position;
            cin >> color >> position;
            if(color == "O")
            {
                orange_queue.push_back(position - 1);
                orange_turns.push_back(true);
            }
            else
            {
                blue_queue.push_back(position - 1);
                orange_turns.push_back(false);
            }
        }
        cout << "Case #" << (i + 1) << ": " << Simulate(orange_queue, blue_queue, orange_turns, 0, 0, 0, 0, 0, 0) << "\n";
    }
    return 0;
}



