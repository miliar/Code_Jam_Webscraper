#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <bitset>
#include <functional>
#include <stdio.h>
#include <stdarg.h>
#include <stddef.h>
#include <math.h>
#include <stdlib.h>
#include <iomanip>

using namespace std;

void solve(int ind) {
    int i,j,NV,NE;
    //input
    cin >> NV >> NE;
    vector<int> ebeg(NE), eend(NE);
    for (i=0; i<NE; i++) {
        cin >> ebeg[i];
        ebeg[i] --;
    }
    for (i=0; i<NE; i++) {
        cin >> eend[i];
        eend[i] --;
    }
    //process
    //first figure out the sets of vertices which make each room
    vector<set<int> > rooms(NE+1);
    for (i=0; i<NV; i++)
        rooms[0].insert(i);
    //add edges one by one
    //it divides in two the room which has both of the edges in there
    set<int>::iterator it;
    for (i=0; i<NE; i++) {
        //edge i makes room i+1
        //check all rooms - which one does it divide?
        for (j=0; j<i+1; j++)
            if (rooms[j].count(ebeg[i])==1 && rooms[j].count(eend[i])==1)
                break;
        //divide the room
        for (it = rooms[j].begin(); it != rooms[j].end(); it ++)
            if (*it > ebeg[i] && *it < eend[i])
                rooms[i+1].insert(*it);
        //delete moved vertices from old room
        for (it = rooms[i+1].begin(); it != rooms[i+1].end(); it ++)
            rooms[j].erase(*it);
        //and add the wall to new room
        rooms[i+1].insert(ebeg[i]);
        rooms[i+1].insert(eend[i]);
    }
/*    for (i=0; i<NE+1; i++) {
        for (it = rooms[i].begin(); it != rooms[i].end(); it ++)
            cout << *it << " ";
        cout << endl;
    }*/
    //find min number of vertices in a room
    int C = NV;
    for (i=0; i<NE+1; i++)
        C = min<int>(C, rooms[i].size());
    //try all possible colorings in this number of colors
    //and find a valid one
    vector<int> bit(NV+1,0);
    vector<bool> has;
    bool ok;
    for (; bit[NV]==0; ) {
        //color of vertice i is in bit[i]
        ok = true;
        for (i=0; i<NE+1 && ok; i++) {
            //check whether this room has all colors
            has = vector<bool>(C,false);
            for (it = rooms[i].begin(); it != rooms[i].end(); it++)
                has[bit[*it]] = true;
            for (j=0; j<C; j++)
                if (!has[j]) {
                    ok = false;
                    break;
                }
        }
        if (ok)
            break;
        //increase bit counter
        bit[0]++;
        i=0;
        while (bit[i]==C) {
            bit[i]=0;
            i++;
            bit[i]++;
        }
    }
    
    //output current coloring
    cout << "Case #" << ind << ": " << C << endl;
    for (i=0; i<NV; i++)
        cout << bit[i]+1 << " ";
    cout << endl;
}

int main() {
    int i,T;
    cin >> T;
    for (i=1; i<=T; i++) {
        solve(i);
    }
}
