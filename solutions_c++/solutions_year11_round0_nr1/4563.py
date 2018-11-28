#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

int main(int argc, char** argv) {

    int cases;
    int case_num = 1;

    cin >> cases; //get number of cases

    //go through the cases
    for(int i = 0; i < cases; i++)
    {
        int numButtons;
        cin >> numButtons;
        int steps = 0;

        //arrays to hold locations where O and B have to press button
        int orange[numButtons];
        int blue[numButtons];
        int o_count = 0;
        int b_count = 0;
        //store the order
        int order_loc[numButtons];
        char order_bot[numButtons];
        for(int k = 0; k < numButtons; k++) //go through the line
        {
            orange[k] = -1;
            blue[k] = -1;
            char robot;
            int loc;
            cin >> robot; //gets which robot
            cin >> loc; //gets location
            order_loc[k] = loc;
            order_bot[k] = robot;
            //cout << order_bot[k] << "  " << order_loc[k] << endl;
            if(robot == 'O')
            {
                orange[o_count] = loc;
                o_count++;
            }
            else
            {
                blue[b_count] = loc;
                b_count++;
            }
        }

        bool solved = false;
        int cur_o = 0;
        int cur_b = 0;
        //holds which loc robot is at
        int o = 1;
        int b = 1;
        int button_count = 0;

        int buttons_hit = 0;

        while(!solved)
        {
            //check if solved
            if(buttons_hit == numButtons)
            {
                solved = true;
                break;
            }
            else
            {
                int current_loc = order_loc[button_count];
                int current_rob = order_bot[button_count];

                //cout << (char)current_rob << " " << current_loc << endl;

                if(o == current_loc && current_rob == 'O') //orange pushes button
                {
                    buttons_hit++;
                    button_count++;
                    cur_o++;
                    /*
                    if(button_count <= numButtons-1)
                    {
                        int next_loc = order_loc[button_count];
                        int next_rob = order_bot[button_count];
                        if(b < blue[cur_b])
                        {
                            b++;
                        }
                        else if(b < blue[cur_b])
                        {
                            b--;
                        }
                    }
                    */
                        if(b < blue[cur_b])
                        {
                            b++;
                        }
                        else if(b > blue[cur_b])
                        {
                            b--;
                        }

                }
                else if(b == current_loc && current_rob == 'B') //blue pushes button
                {
                    buttons_hit++;
                    button_count++;
                    cur_b++;
                    /*
                    if(button_count <= numButtons-1)
                    {
                        int next_loc = order_loc[button_count];
                        int next_rob = order_bot[button_count];
                        if(o < orange[cur_o])
                        {
                            o++;
                        }
                        else if(o < orange[cur_o])
                        {
                            o--;
                        }
                    }
                    */
                                            if(o < orange[cur_o])
                        {
                            o++;
                        }
                        else if(o > orange[cur_o])
                        {
                            o--;
                        }

                }
                else //no buttons pushed
                {
                    if(o < orange[cur_o])
                    {
                        o++;
                    }
                    else if(o > orange[cur_o])
                    {
                        o--;
                    }
                    if(b < blue[cur_b])
                    {
                        b++;
                    }
                    else if(b > blue[cur_b])
                    {
                        b--;
                    }

                }
            }
            steps++;

        }


/*
        //testing
        cout << "case" << (i+1) << ": " << endl;
        for(int k = 0; k < numButtons; k++)
        {
            cout << "Orange = " << orange[k] << endl;
        }
        for(int k = 0; k < numButtons; k++)
        {
            cout << "blue = " << blue[k] << endl;
        }
*/
        cout << "Case #" << case_num << ": " << steps << endl;
        case_num++;
    }



  return 0;
}
