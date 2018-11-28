/* 
 * File:   main.cpp
 * Author: zhwang
 *
 * Created on May 7, 2010, 10:46 PM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
/*
 * 
 */
using namespace std;

typedef struct snapper {
    bool isON;
    bool isPowered;
} Snapper;

void snap(Snapper snapperlist[], int num_snappers) {
    snapperlist[0].isPowered = true;

    for (int i = 0; i < num_snappers; i++) {
        if (snapperlist[i].isPowered == true)
            snapperlist[i].isON = (snapperlist[i].isON == true) ? false : true;
    }
    for (int i = 0; i < num_snappers; i++) {
        if (snapperlist[i].isON == true && snapperlist[i].isPowered == true && i != num_snappers - 1) {
            snapperlist[i + 1].isPowered = true;
        }
        if (snapperlist[i].isON == false) {
            for (int j = i + 1; j < num_snappers; j++) {
                snapperlist[j].isPowered = false;
            }
            break;
        }
    }
}

bool ONorOFF(int num_snappers, long num_times) {

#ifdef debug
    ofstream fout("trace.out");
    if (!fout.is_open()) {
        cout << "can not open trace.out" << endl;
        exit(-1);
    }
#endif

    Snapper snapperlist[num_snappers];
    for (int i = 0; i < num_snappers; i++) {
        snapperlist[i].isON = false;
        snapperlist[i].isPowered = false;
    }
#ifdef debug
    fout << "snap times";
    for (int i = 0; i < num_snappers; i++) {
        fout << "," << i;
    }
    fout << endl;
#endif
    for (long t = 0; t < num_times; t++) {
        snap(snapperlist, num_snappers);
        //for debug
#ifdef debug
        fout << t;
        for (int i = 0; i < num_snappers; i++) {
            fout << ", status: " << snapperlist[i].isON;
        }
        fout << endl;

        fout << t;
        for (int i = 0; i < num_snappers; i++) {
            fout << ", power: " << snapperlist[i].isPowered;
        }
        fout << endl;
#endif
    }

#ifdef debug
    fout.close();
#endif

    return snapperlist[num_snappers - 1].isON && snapperlist[num_snappers - 1].isPowered;
}

int main(int argc, char** argv) {
    ifstream fin("A-small.in");
    if (!fin.is_open()) {
        cout << "can not open A-small.in" << endl;
        exit(-1);
    }
    int num_limits;
    fin >> num_limits;

    ofstream fout("A-small.out");
    if (!fout.is_open()) {
        cout << "can not open A-small.out" << endl;
        exit(-1);
    }

    int num_snappers;
    long num_times;
    bool onoff;
    for (int i = 0; i < num_limits; i++) {
        fin >> num_snappers >> num_times;
        onoff = ONorOFF(num_snappers, num_times);
        fout << "Case #" << i+1 << ": ";
        if (onoff == true)
            fout << "ON";
        else
            fout << "OFF";
        fout << endl;
    }
    fin.close();
    fout.close();
    return (EXIT_SUCCESS);
}

