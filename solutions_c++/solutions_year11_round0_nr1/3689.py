#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<sstream>
#include<algorithm>
using namespace std;

enum {PUSH_BUTTON=1};

int process( string & line ) {

    istringstream sin(line);
    int tmp; sin>>tmp; //skip first number

    int total_time = 0;

    int o_pos = 1; int o_last = 0;
    int b_pos = 1; int b_last = 0;

    char robot;
    int target;

    while( sin>>robot>>target ) {

        //cout<<robot<<target<<endl;
        if( robot=='O' ){
            int move_time = abs(target - o_pos);

            move_time = move_time - (total_time - o_last);

            if(move_time < 0)
                move_time = 0;

            total_time = total_time + move_time + PUSH_BUTTON;

            o_last = total_time;
            o_pos = target;

        } else { // robot==B
            int move_time = abs(target - b_pos);

            move_time = move_time - (total_time - b_last);

            if(move_time < 0)
                move_time = 0;

            total_time = total_time + move_time + PUSH_BUTTON;

            b_last = total_time;
            b_pos = target;
        }
    }

    return total_time;
}

int main() {

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int num_case;
    cin>>num_case;

    cin.ignore(10, '\n');

    for(int i=1;i<=num_case;++i) {

        /* parse command */
        string line;
        getline(cin, line);

        int time = process(line);

        printf("Case #%d: %d\n", i, time);
    }
    return 0;
}
