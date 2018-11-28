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

using namespace std;

bool isBest(int a, int b, int c, int p)
{
    int m = max(max(a, b), c);
    if(m>=p)
        return true;
    return false;
}

bool surpriseCheck(int a, int b, int c)
{
    int mx = max(max(a, b), c);
    int mn = min(min(a, b), c);
    if (mx-mn==2)
        return true;
    return false;
    
}

bool isValid(int a, int b, int c)
{
    int mx = max(max(a, b), c);
    int mn = min(min(a, b), c);
    if (mx-mn>2)
        return false;
    return true;
}

int main()
{

    int T;
    cin>>T;
    int N, S, p;
    for(int t=1;t<=T;t++)
    {
        cin>>N>>S>>p;
        vector<int> v;
        int s;
        for(int i=0;i<N;i++)
        {
            cin>>s;
            v.push_back(s);
        }
        int count = 0;
        for(int ii=0;ii<v.size();ii++)
        {
            int score = v[ii];
            bool needs_surprise = false;
            bool has_best = false;
            for(int i=0;i<=10;i++)
            {
                for(int j=0;j<=10;j++)
                {
                    for(int k=0;k<=10;k++)
                    {
                        if(i+j+k==score)
                        {
                            if(isValid(i, j, k) && isBest(i, j, k, p))
                            {
                                if(has_best && !needs_surprise)
                                {
                                    break;
                                }
                                else if(has_best && needs_surprise)
                                {
                                    if(!surpriseCheck(i, j, k))
                                    {
                                        needs_surprise = false;
                                        S++;
                                    }
                                }
                                else 
                                {
                                    if(surpriseCheck(i, j, k) && S)
                                    {
                                        has_best = true;
                                        needs_surprise = true;
                                        S--;
                                    }
                                    else if(!surpriseCheck(i, j, k))
                                    {
                                        has_best = true;
                                        needs_surprise = false;
                                    }
                                }
                            }
                        }

                    }
                }
            }
            if(has_best)
                count++;
        }
        cout<<"Case #"<<t<<": "<<count<<endl;
    }

    return 0;
}
