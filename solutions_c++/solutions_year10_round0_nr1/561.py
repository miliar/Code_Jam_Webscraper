/* 
 * File:   main.cpp
 * Author: Administrator
 *
 * Created on 2010年5月8日, 上午10:01
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    char* input = "A-large.in";
    char* output = "output.out";
    ifstream ifs(input);
    ofstream ofs(output);
    int T;
    ifs>>T;
    int count=0;
    unsigned int N, K;
    char map[2][4] = {"OFF", "ON"};
    while(T-- >0 ){
        count++;
        ifs>>N;
        ifs>>K;
        if(count > 1){
            ofs<<"\n";
        }
        unsigned int cmp = (0x1<<N)-1;
        K = K&cmp;
        if(K == cmp){
            ofs<<"Case #"<<count<<": ON";
        }else{
            ofs<<"Case #"<<count<<": OFF";
        }
    }
    ifs.close();
    ofs.close();
    return 0;
}

