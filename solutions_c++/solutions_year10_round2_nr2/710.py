/* 
 * File:   main.cpp
 * Author: Neil
 *
 * Created on May 22, 2010, 1:12 PM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
/*
 * 
 */

struct chick{
    int speed;
    int actspeed;
    int pos;
    bool arrive;
    bool canarrive;
};

int doswap(struct chick cl[], int from, int dest){
    struct chick temp;
    int numswap = 0;
    for(int i = from; i < dest; i++){
        
        temp = cl[i];
        cl[i] = cl[i+1];
        cl[i+1] = cl[i];
        numswap++;
    }
    return numswap;
}

int swap(struct chick cl[], int numchi, int numarrive, long posbarn, int time, int need){
    int notarrive_pos = 0;
    for(int i = numchi - 1; i >=0 ; i--){
        if(cl[i].arrive == false){
            notarrive_pos = i;
            break;
        }
    }

    int sum = 0;
    while(need-- > 0){
        int canarrive_pos = 0;
        for(int i = notarrive_pos; i >= 0; i--){
            if(cl[i].canarrive == true){
                canarrive_pos = i;
				break;
            }
        }
        int numswap = doswap(cl, canarrive_pos, notarrive_pos);
        notarrive_pos--;
        sum += numswap;
    }
    return sum;
}

int setarriveflas(struct chick cl[], int numchi, int numarrive, long posbarn, int time){
	for(int i = 0; i < numchi; i++){
		cl[i].actspeed = cl[i].speed;
	}
    for(int i = numchi - 2; i >= 0; i--){
		if(cl[i+1].actspeed < cl[i].speed)
            cl[i].actspeed = cl[i+1].actspeed;
    }

    int sum = 0;
    for(int i = 0; i < numchi; i++){
        long final = cl[i].pos + cl[i].actspeed * time;
        if(final >= posbarn){
            cl[i].arrive = true;
            sum++;
        }
        else
            cl[i].arrive = false;
    }
    return numarrive - sum;
    
}

bool checkpossible(struct chick cl[], int numchi, int numarrive, long posbarn, int time){
    int sum = 0;
    for(int i = 0; i < numchi; i++){
        long final = cl[i].pos + cl[i].speed * time;
        if(final >= posbarn){
            cl[i].canarrive = true;
            sum++;
        }
        else{
            cl[i].canarrive = false;
        }
    }
    if(sum >= numarrive)
        return true;
    else
        return false;
}

int main(int argc, char** argv) {
    ifstream fin("B-large.in", ios::in);
    if (!fin.is_open()) {
        cout << "can not open input file" << endl;
        exit(-1);
    }

    ofstream fout("B-large.out", ios::out);
    if (!fout.is_open()) {
        cout << "can not open output file" << endl;
        exit(-1);
    }

    int testnum;
    fin >> testnum;

    int numchi, numarrive, time;
    long posbarn;
    for (int i = 0; i < testnum; i++) {
        fin >> numchi >> numarrive >> posbarn >> time;
        struct chick *cl = new struct chick [numchi];
        for(int j = 0; j < numchi; j++){
            fin >> cl[j].pos;
        }
        for(int j = 0; j < numchi; j++){
            fin >> cl[j].speed;
        }
        bool possible = checkpossible(cl, numchi, numarrive, posbarn, time);
        if(!possible){
            fout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
            continue;
        }
        int need = setarriveflas(cl, numchi, numarrive, posbarn, time);
        if(need <= 0){
            fout << "Case #" << i+1 << ": 0" << endl;
            continue;
        }
        
        int sum = swap(cl, numchi, numarrive, posbarn, time, need);
        fout << "Case #" << i+1 << ": " << sum << endl;
        
            
    }
    return (EXIT_SUCCESS);
}

