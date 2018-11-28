#include <cmath>
#include <queue>
#include <utility>
#include <fstream>
#include <iostream>
using namespace std;

#define min(a,b) ((a>b)?b:a)
int get_move(int target, int loc, int max);

int main()
{
    istream &in= cin;
    ostream &out= cout;

    int count;
    in >> count;
    for (int i= 0; i < count; ++i)
    {
        int blue= 1;
        int orng= 1;
        queue< pair<char,int> > next;
        queue<int> blues;
        queue<int> orngs;
        int c;
        in >> c;
        for (int j= 0; j < c; ++j)
        {
            char which;
            int button;
            in >> which >> button;
            next.push(pair<char,int>(which,button));
            if (which == 'O') orngs.push(button);
            else blues.push(button);
        }
        int t= 0;
        while (!next.empty())
        {
            char which= next.front().first;
            int target= next.front().second;
            int d;
            if (which == 'O')
            {
                d= abs(orng-target)+1;
                if (!blues.empty()) blue+= get_move(blues.front(), blue, d);
                orng= target;
                orngs.pop();
            }
            else
            {
                d= abs(blue-target)+1;
                if (!orngs.empty()) orng+= get_move(orngs.front(), orng, d);
                blue= target;
                blues.pop();
            }
            t+= d;
            next.pop();
        }
        cout << "Case #" << i+1 << ": " << t << endl;
    }
}

int get_move(int target, int loc, int max)
{
    int distance= target-loc;
    if (distance == 0) return 0;
    int sign= distance/abs(distance);
    return sign * min(abs(distance), max);
}
