#include <iostream>
#include <fstream>
#include <sstream>
#include <iterator>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

#include <cstdio>

using namespace std;


#define Min(x, y) (x < y ? x : y)


int get_maximum(int S, int p, const vector<int> & vtot)
{
    if(p > 1)
    {
        int cnt = 0, ret = 0;
        for(vector<int>::const_iterator it = vtot.begin(); it != vtot.end(); it++)
        {
            if(*it >= 3 * p - 4)
            {
                if(*it >= 3 * p - 2)
                    ret += 1;
                else
                    cnt += 1;
            }
        }
        return ret + Min(S, cnt);
    }
    else if(p == 1)
    {
        int ret = 0;
        for(vector<int>::const_iterator it = vtot.begin(); it != vtot.end(); it++)
        {
            if(*it >= 1)
                ret += 1;
        }
        return ret;
    }
    else
        return vtot.size();
}


int main()
{
    int T;
    cin >> T;
    for(int k = 1; k <= T; k++)
    {
        int N, S, p;
        cin >> N >> S >> p;
        vector<int> vtot;
        int t;
        for(int i = 0; i < N; i++)
        {
            cin >> t;
            vtot.push_back(t);
        }
        cout << "Case #" << k << ": " << get_maximum(S, p, vtot) << endl;
    }
    return 0;
}
