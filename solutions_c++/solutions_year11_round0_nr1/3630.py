/*
- start at 1
- have to wait for the other to finish his turn
- at step i => the second one should be at its pressing position  
- other don't hvae to move if not unnecessary
*/

#include <iostream>
#include <cstdio>

// #define abs(x) ((x)>0)?(x):(-x)

using namespace std;

int robot[101];
int step[101];
int n;

int abs(int a){
    return (a>0)?a:(-a);
}

int main(){

    int ntest;
    cin>>ntest;

    for(int test=1;test<= ntest;test++){
        cin>>n;
        char ch;
        for(int i=0;i<n;i++){
            cin>>ch>>step[i];
            robot[i] = (ch=='O')?0:1;
        }

        int pos[2];
        pos[0] = pos[1] = 1;
        int cost = step[0];
        int mov = step[0];
        pos[robot[0]] = step[0];
        for(int i=1;i<n;i++){
            // compute requred moves
            int delta= abs(step[i] - pos[robot[i]])+1;
            // cout<< " d " <<delta<<endl;
            // update position
            pos[robot[i]] = step[i];
            if (robot[i] == robot[i-1]){
                // move the robot to new position
                mov += delta;
            } else {
                // moving during the time other robot moving
                // but still have to press => delta = 1
                if (delta <= mov) delta=1;
                else delta -= mov;
                mov = delta;
            }

            // cout<<cost<<" i "<<i<<" r "<<robot[i]<<" delta "<<delta<<" move "<<mov<<endl;
            cost += delta;
        }
        cout<<"Case #"<<test<<": "<<cost<<endl;
    }

    return 0;
}
