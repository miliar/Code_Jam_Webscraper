using namespace std;

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#define forNF(I,F,C) for(int32_t I=(F); I<int32_t(C); ++I)
#define forN(I,C) forNF(I,0,C)
#define vi vector<int>
#define pb push_back
#define sumMod(a,b) a=(a+b)%1000003
#define mulMod(a,b) a=(a*b)%1000003
#define toZero(a) forN(kk,sizeof(a)) ((char*)a)[kk]=0
//#define local

vector< pair<int,int> > lanes;
vector< pair<int,int> > dist;



int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    long long nrT;
    //string st;
    //cin >> st;
    cin >> nrT;

    forN(test,nrT)
    {
        cout << "Case #"<<test+1<<": ";
        bool poss=true;
        char c;
        int n,a,b,final;
        lanes.clear();
        dist.clear();
        cin >> n;
        forN(i,n)
        {
            cin >> a >> b;
            lanes.push_back(make_pair(a,b));
            if (i == 0)
            {
                dist.push_back(make_pair(a,2*a));
            }
            else
            {
                while (dist.size()>0)
                {
                    if (dist[0].second>=a)
                    {
                        dist.push_back(make_pair( a ,min( (a-dist[0].first) + a, max(a+b,0) ) ) );
                        break;
                    }
                    else
                    dist.erase(dist.begin());
                }

                if (dist.size()==0)
                {
                    poss=false;
                }
            }
        }
        cin >> final;
        if (poss)
        {


        while (dist.size()>0)
        {
        if (dist[0].second>=final)
        {
            break;
        }
        else
            dist.erase(dist.begin());
        }
        poss = (dist.size()>0);
        }

    if (poss)
        cout << "YES"<<endl;
    else
        cout << "NO"<<endl;
    }
    return 0;
}
