#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>
#include <map>


using namespace std;

vector<int> src;
vector<int> dst;
set<pair<int, int> > exc;
map<int, int> mp;
int t, n, pc;


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>t;
    for(int test = 1; test <= t; test++)
    {
        cin>>n;
        src.resize(n);
        dst.resize(n);
        exc.clear();

        mp.clear();
        for(int i = 0; i < n; i++)
        {
            cin>>src[i];
            dst[i] = src[i];
        }
        int cnt = 0;
        sort(dst.begin(), dst.end());
        for(int i = 0; i < n; i++)
            if(src[i] != dst[i])
                cnt++;
        cout<<"Case #"<<test<<": "<<cnt<<endl;
    }
    return 0;
}