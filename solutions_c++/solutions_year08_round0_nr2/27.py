#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

using namespace std;

struct ruta
{
    bool st;
    int t1, t2;
    ruta(int a, int b, int c)
    {
        st = a;
        t1 = b;
        t2 = c;
    }
};

bool operator <(ruta a, ruta b)
{
    return a.t1 < b.t1;
}

struct bus
{
    bool pos;
    int t;
    bus(int a, int b)
    {
        pos = a;
        t = b;
    }
};

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int N;
    cin>>N;
    
    for(int caso=0; caso<N; caso++)
    {
        int t;
        cin>>t;
        
        int na, nb;
        cin>>na>>nb;
        
        vector <ruta> V;
        for(int i=0; i<na; i++)
        {
            int h1, m1, h2, m2;
            scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
            V.push_back(ruta(0,h1*60 + m1, h2*60 + m2));
        }
        for(int i=0; i<nb; i++)
        {
            int h1, m1, h2, m2;
            scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
            V.push_back(ruta(1, h1*60 + m1, h2*60 + m2));
        }
        
        int minN = 1<<30;
        int xx = -1, yy = -1;
        
        sort(all(V));
        
        for(int x=0; x<=na; x++)
        {
            for(int y=0; y<=nb; y++)
            {
                vector <bus> B;
                
                for(int i=0; i<x; i++)
                    B.push_back(bus(0, 0));
                for(int i=0; i<y; i++)
                    B.push_back(bus(1, 0));
                
                bool ok = true;
                for(int i=0; i<V.size(); i++)
                {
                    bool done = false;
                    for(int j=0; j<B.size(); j++)
                    {
                        if(V[i].st == B[j].pos && V[i].t1 >= B[j].t)
                        {
                            B[j].pos = !B[j].pos;
                            B[j].t = V[i].t2 + t;
                            done = true;
                            break;
                        }
                    }
                    if(!done) ok = false;
                }
                if(ok)
                {
                    if(x + y < minN)
                    {
                        minN = x + y;
                        xx = x;
                        yy = y;
                    }
                    break;
                }
            }
        }
        cout<<"Case #"<<caso + 1<<": "<<xx<<" "<<yy<<endl;
    }
    return 0;
}

