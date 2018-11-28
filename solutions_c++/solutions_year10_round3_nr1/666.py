#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct wire
{
    int left, right;
};

bool comp(wire i, wire j)
{
    return i.left < j.left;
}

int main()
{
    int t, c;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.OUT", "w", stdout);

    cin>>t;
    for(c=1;c<=t;c++)
    {
        int no_wire;
        int i, j;
        cin>>no_wire;
        wire wires[no_wire];
        for(i=0;i<no_wire;i++) cin>>wires[i].left>>wires[i].right;
        sort(wires, wires+no_wire, comp);
        int ans=0;
        for(i=0;i<no_wire;i++)
        {
            for(j=i+1;j<no_wire;j++)
            {
                if(wires[i].right > wires[j].right) ans++;
            }
        }
        cout<<"Case #"<<c<<": "<<ans<<endl;
    }
    return 0;
}
