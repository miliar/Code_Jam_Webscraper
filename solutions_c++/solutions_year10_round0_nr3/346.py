#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long long LL;

    //strategy
    //17 rides of size 6 car with 4 group queue: 1,4,2,1
    //0,0: 1,4 = 5, 0->2 @ 0
    //1,2: 2,1,1 = +4 = 9, 2->1 @ 1
    //2,1: 4,2 = +6 = 15, 1->3 @ 2
    //3,3: 1,1,4 = +6 = 21, 3->2 @ 3
    //cycle 21-5 = +16 per 4-1
    //(17-4) / 3 = 4
    //21 + 4 * 16 = 85 @ 15
    //16,2: +4 = 89

struct rcNode
{
    int next;       // next node
    int run;        // first run # as base
    LL profit;      // profit for this ride
    LL accum;       // profit accumulated before this ride
    int people;     // number of people in the group
};

int main(int argc, char* argv[])
{
    ifstream input("C-large.in");
    assert(input.is_open());
    ofstream output("C-large.out");
    assert(output.is_open());

    int T;
    input>>T;
    for(int caseNum=0;caseNum<T;caseNum++)
    {
        rcNode nodes[1024];
        for(int i=0;i<1024;i++) nodes[i].run = -1;

        int R,k,N;
        input>>R>>k>>N;
        for(int i=0;i<N;i++) input>>nodes[i].people;

        // first, simulate until a cycle is reached (at most 1000 times)
        LL totalRevenue = 0;
        int curNode = 0;
        int baseNode;
        int rideNum = 0;

        while(nodes[curNode].run==-1 && rideNum<R)
        {
            baseNode = curNode;
            LL load = 0;
            while(load+nodes[curNode].people<=k && !(load>0&&curNode==baseNode))
            {
                load += nodes[curNode++].people;
                if(curNode==N) curNode=0;
            }
            nodes[baseNode].accum = totalRevenue;
            nodes[baseNode].next = curNode;
            nodes[baseNode].profit = load;
            nodes[baseNode].run = rideNum++;
            totalRevenue += load;
        }

        // next, add any cycle revenue
        int cyclePeriod = rideNum-nodes[curNode].run;
        int cycleCount = (R-rideNum)/cyclePeriod;
        totalRevenue += (totalRevenue-nodes[curNode].accum)*cycleCount;
        rideNum += cycleCount*cyclePeriod;

        // last, add any remaining rides
        while(rideNum++<R)
        {
            totalRevenue += nodes[curNode].profit;
            curNode = nodes[curNode].next;
        }

        output<<"Case #"<<caseNum+1<<": "<<totalRevenue<<endl;
    }

    input.close();
    output.close();

    return 0;
}