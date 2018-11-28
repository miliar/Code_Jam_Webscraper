#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;
#define forn(i,n) for(i=0;i<(n);i++)

int prod(vector<int> v1, vector<int> v2)
{
    int res = 0;
    int i;
    forn(i,v1.size())
    {
        res += v1[i] * v2[v2.size()-1-i];
    }
    return res;
}

int main()
{
    int n,k,x,j,res;
    int i = 0;
    ifstream text("A-small.in");
    ofstream ext("A-small.out");
    string st;
    getline(text,st);
    n = atoi(st.c_str());
    vector<int> v1(0),v2(0);
    while(i < n)
    {
        text >> st;
        k = atoi(st.c_str());
        v1.resize(0);
        v2.resize(0);
        forn(j,k)
        {
            text >> st;
            x = atoi(st.c_str());
            v1.push_back(x);
        }
        forn(j,k)
        {
            text >> st;
            x = atoi(st.c_str());
            v2.push_back(x);
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        res = prod(v1,v2);
        ext << "Case #" << i+1 << ": " << res << '\n';
        i++;
    }
    ext.close();
}
