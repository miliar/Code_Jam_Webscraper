#include<iostream>
#include <string>
#include <vector>
#include <bitset>

#include <cmath>

#define dout if(0) cout

using namespace std;
class Bot
{
public:
    int Press(int b, int gtime);
    Bot(): pos(1), time(0) {}
private:    
    int pos;
    int time;
};

int main()
{

    int T;
    cin >>T;
    dout << T << endl;
    for(int t=1; t<=T; ++t)
    {
        int N; cin >>N;
        dout << "-----------------------" << endl;
        dout << N << endl;

        char bot;
        int  bno;
        Bot O, B;
        
        int gtime=0;
        for(int i=0; i<N; ++i)
        {
            cin >> bot >> bno;
            dout << bot << " " << bno;
            if(bot == 'O')
                gtime = O.Press(bno, gtime);
            else if(bot == 'B')
                gtime = B.Press(bno, gtime);

            dout << " gtime " << gtime << endl;

        }
        dout << endl;

        cout << "Case #" << t << ": " << gtime;
        cout << endl;
    }
}

int Bot::Press( int b, int gtime)
{
    int distance = b-pos;
    if(distance <0) distance = -distance;

    pos = b;
    time = time + distance; //travel time

    time = gtime > time ? gtime : time;
    
    ++time;                     //press time

    return time;
}
