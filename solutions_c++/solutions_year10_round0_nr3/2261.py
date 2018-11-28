/* 
 * File:   main.cpp
 * Author: zhwang
 *
 * Created on May 8, 2010, 12:11 PM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
using namespace std;
/*
 * 
 */

long long getLoopsum(vector< queue<long> > & past, long loopstart_index, long offset, long long * offset_sum, long capacity_k){
    long long loopsum = 0;
    *offset_sum = 0;
    for(long i = loopstart_index; i < past.size(); i++){
        long long sum = 0;
        while(!past[i].empty() && (sum + past[i].front()) <= capacity_k ){
            sum += past[i].front();
            past[i].pop();
        }
        loopsum += sum;
        if(offset > 0)
            *offset_sum += sum;
        offset--;
    }
    return loopsum;
}

bool isEqual(queue<long> q1, queue<long> q2){
    if(q1.size() != q2.size())
        return false;
    while(!q1.empty()){
        if(q1.front() != q2.front())
            return false;
        q1.pop();
        q2.pop();
    }
    return true;
}

long isLoopStart(const vector< queue<long> > & past, const queue<long> & oncoaster){
    for(long i = 0; i < (long)past.size(); i++){
        if(isEqual(past[i], oncoaster))
            return i;
    }
    return -1;
}

long long makeMoney(long num_times_R, long capacity_k, long g[], int num_group_N){
    long long money = 0;
    queue<long> waitingline;
    queue<long> oncoaster;
    vector< queue<long> > past;
    for(int i = 0; i < num_group_N; i++){
        waitingline.push(g[i]);
    }

    long temp_capacity;
    long long loop_sum;
    long loop_size;
    //for each time
    for(long i = 0; i < num_times_R; i++){
        long long sum = 0;
        //checking loop
        long loopstart_index = isLoopStart(past, waitingline);
        if( loopstart_index != -1){
            //there is a loop
            loop_size = past.size() - loopstart_index;
            long loop_num = (num_times_R - i) / loop_size;
            long offset = (num_times_R - i) % loop_size;

            long long offset_sum;
            loop_sum = getLoopsum(past, loopstart_index, offset, &offset_sum, capacity_k);

            money += loop_sum * loop_num + offset_sum;
            break;
        }
        
        past.push_back(waitingline);
        while(!waitingline.empty() && (sum + waitingline.front()) <= capacity_k){
            int temp = waitingline.front();
            waitingline.pop();
            oncoaster.push(temp);
            sum += temp;
        }

        
        
        money += sum;
        while(!oncoaster.empty()){
            waitingline.push(oncoaster.front());
            oncoaster.pop();
        }
        
    }

    return money;
}

int main(int argc, char** argv) {
    ifstream fin("C-large.in");
    if (!fin.is_open()) {
        cout << "can not open A-small.in" << endl;
        exit(-1);
    }
    int num_limits;
    fin >> num_limits;

    ofstream fout("C-large.out");
    if (!fout.is_open()) {
        cout << "can not open A-small.out" << endl;
        exit(-1);
    }

    long num_times_R, capacity_k;
    int num_group_N;
    for (long i = 0; i < num_limits; i++) {
        fin >> num_times_R >> capacity_k >> num_group_N;
        long g[num_group_N];
        for(long j = 0; j < num_group_N; j++){
            fin >> g[j];
        }
        
        long long money = makeMoney(num_times_R, capacity_k, g, num_group_N);
        fout << "Case #" << i+1 << ": ";
        fout << money;
        fout << endl;
    }
    return (EXIT_SUCCESS);
}

