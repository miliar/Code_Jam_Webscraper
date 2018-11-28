#include <iostream.h>
#include <sstream>
#include <queue.h>

using namespace std;

int main()
{
    int noOfTestCases = 0;
    unsigned long noOfTrips;
    unsigned long maxPeople;
    unsigned long noOfGroups;
    unsigned long groupSize = 0;
    unsigned long earnings = 0;
    unsigned long totalNoOfPeople = 0;
    unsigned long qSize = 0;
    unsigned long tempPassSize = 0;

    freopen ("input.txt", "rt", stdin);
    freopen ("output.txt", "wt", stdout);

    cin >> noOfTestCases;

    for (int i=0; i< noOfTestCases; i++)
    {
        queue<unsigned long> q;
        cout << "Case #" << i+1<<": ";
        earnings = 0;
        totalNoOfPeople = 0;
        cin >> noOfTrips; cin >> maxPeople; cin >> noOfGroups;
        int l = noOfGroups;
        while (l>0)
        {
            cin >> groupSize;
            totalNoOfPeople += groupSize;
            q.push(groupSize);
            l--;
        }

        if (totalNoOfPeople <= maxPeople)
            earnings = totalNoOfPeople * noOfTrips;
        else
        {
            for (int z=0; z<noOfTrips; z++)
            {
                tempPassSize = 0;
                for (int j=0; j<noOfGroups; j++)
                {
                    tempPassSize += q.front();
                    if (tempPassSize <= maxPeople)
                    {
                        q.push(q.front());
                        q.pop();
                    }
                    else
                    {
                        tempPassSize -=q.front();
                        break;
                    }
                } 
                earnings += tempPassSize;
            }
        }
        cout << earnings  << endl;
    }
}


// vim:ts=4:sw=4:expandtab:ai:cindent
