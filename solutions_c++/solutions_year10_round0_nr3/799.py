/*
 * =====================================================================================
 *
 *       Filename:  themepark.cpp
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  05/07/2010 11:52:10 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (),
 *        Company:
 *
 * =====================================================================================
 */

#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>


using std::cout;
using std::endl;
using std::ifstream;
using namespace std;

#define MAX_GROUPS 1000
unsigned long groupsize[MAX_GROUPS];

struct Group {
    // int index;   // index of first group in groups
    int next;
    long round;
    long profit;
};

Group groups[MAX_GROUPS];
void reset() {
    for (int i = 0; i < MAX_GROUPS; ++i)
        groups[i].round = -1;
}

long long themepark (unsigned long nrounds, unsigned long capacity, unsigned int ngroups) {
    unsigned long roundidx = 0, count = 0, i = 0;
    long index = 0;
    long repeatidx = -1;
    Group *last = NULL;
    while (roundidx < nrounds) {
        index = i;
        unsigned long indexbase = index%ngroups;
        if (groups[indexbase].round != -1) { // repeat
            repeatidx = indexbase;
            if (last) last->next = indexbase;
            break;
        }

        while (count + groupsize[i%ngroups] <= capacity) {
            count += groupsize[i%ngroups];
            ++i;
            if (i%ngroups == indexbase) break;
        }

        groups[indexbase].round = roundidx;
        groups[indexbase].profit = count;
        if (last)
            last->next = indexbase;
        last = groups+indexbase;

        ++roundidx;
        count = 0;
    }

    long long profit = 0, repeatProfit = 0, repeatRounds = 0;
    if (repeatidx != -1) {
        for (int i = repeatidx; ; ) {
            repeatProfit += groups[i].profit;
            i = groups[i].next;
            ++ repeatRounds;
            if (i == repeatidx) break;
        }
    }

    index = 0;
    Group *temp = groups;
    for (unsigned int i = 0; i < nrounds; ) {
        if (index == repeatidx) {
            if (i + repeatRounds < nrounds) {
                i += repeatRounds;
                profit += repeatProfit;
                continue;
            }
        }
        profit += temp->profit;
        index = temp->next;
        temp = groups + index;
        ++i;
    }

    return profit;
}

int main() {
    ifstream ifs("C-large.in");
    int ntestcases;
    ifs>>ntestcases;

    unsigned long nrounds, capacity, ngroups;
    long long result;
    for (int i = 0; i < ntestcases; ++i) {
        reset();
        ifs>>nrounds>>capacity>>ngroups;
        for (unsigned int j = 0; j < ngroups; ++j)
            ifs>>groupsize[j];
        result = themepark(nrounds, capacity, ngroups);
        cout<<"Case #"<<i+1<<": "<<result<<endl;
    }
}

