// A. Bot Trust.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
using namespace std;

#define O_BASE 200
int t, n;
char s;
int p;
vector<int> vec;

int find_next(int current, bool is_o)
{
    for (;;)
    {
        ++current;
        if (current >= vec.size())
            return -1;
        bool cond;
        if (is_o)
            cond = (vec[current] > O_BASE);
        else 
            cond = (vec[current] < O_BASE);
        
        if (cond)
        {
            return current;
        }
    }
    return 0;
}

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> t;
    for (int c = 1; c <= t; c++)
    {
        vec.clear();

        cin >> n;
        for (int j = 0; j < n; j++)
        {
            cin >> s;
            cin >> p;
            if (s == 'O')
            {
                vec.push_back(p + O_BASE);
            }
            else if (s == 'B')
            {
                vec.push_back(p);
            }
        }

        int o_next, b_next;
        int o_value = O_BASE + 1, b_value = 1;
        int cnt = 0;
        int index = 0;

        if (vec[0] > O_BASE)
        {
            o_next = 0;
            b_next = find_next(0, false);
        }
        else
        {
            b_next = 0;
            o_next = find_next(0, true);
        }

        for(;;)
        {
            if (index >= vec.size())
                break;

            bool o_can_presss = false, b_can_press = false;
            if (vec[index] > O_BASE)
            {
                o_can_presss = true;
            }
            else
            {
                b_can_press = true;
            }

            if (o_next != -1)
            {
                if (vec[o_next] == o_value)
                {
                    if (o_can_presss)
                    {
                        index++;
                        o_next = find_next(o_next, true);
                    }
                }
                else if (o_value < vec[o_next])
                {
                    o_value++;
                }
                else
                {
                    o_value--;
                }
            }
            

            if (b_next != -1)
            {
                if (vec[b_next] == b_value)
                {
                    if (b_can_press)
                    {
                        index++;
                        b_next = find_next(b_next, false);
                    }
                }
                else if (b_value < vec[b_next])
                {
                    b_value++;
                }
                else
                {
                    b_value--;
                }
            }
            

            cnt++;
        }
        cout << "Case #" << c << ": ";
        cout << cnt << endl;
    }


	return 0;
}

