/* 
 * File:   main.cpp
 * Author: ben
 *
 * Created on May 8, 2010, 1:30 PM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>

/*
 * 
 */
int main(int argc, char** argv)
{
    int testcount;
    int* snappercount;
    int* togglecount;

    std::cin >> testcount;
    snappercount = new int[testcount];
    togglecount = new int[testcount];

    for (int i = 0; i < testcount; i++)
    {
        std::cin >> snappercount[i];
        std::cin >> togglecount[i];
    }

    for (int i = 0; i < testcount; i++)
    {
        bool* togglestate = new bool[snappercount[i]]; // assumes def value is false

        for (int z = 0; z < snappercount[i]; z++)
            togglestate[z] = false;

        for (int j = 0; j < togglecount[i]; j++)
        {
            for (int k = 0; k < snappercount[i]; k++)
            {
                togglestate[k] = !togglestate[k];

                if (togglestate[k]) // if true now, it was false on snap
                    break;
            }
        }


        bool on = true;

        for (int k = 0; k < snappercount[i]; k++)
            if (!togglestate[k])
            {
                on = false;
                break;
            }

        if (on)
            std::cout << "Case #" << i + 1 << ": ON" << std::endl;
        else
            std::cout << "Case #" << i + 1 << ": OFF" << std::endl;

        delete [] togglestate;
    }

    return (EXIT_SUCCESS);
}

