#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define forn(i,n) forsn(i,0,n)
#define esta(x,c) (c.find(x)!=c.end())
#define all(v) v.begin(),v.end()

int main ()
{
    int T, N, S, p, cnt=0, cond=0, score;
    freopen("Bcodejam.in","r",stdin);
    freopen("Bcodejam.out","w",stdout);
    cin >> T;
    forn(i,T)
    {
        cin>> N;
        cin>> S;
        cin>> p;
        if(p==0)
        {
            forn(j,N)
            {
                cin>> score;
            }
            cout << "Case #"<< i+1 << ": "<< N<<endl;
        }
        else
        {
            if(p==1)
            {
                forn(j,N)
                {
                    cin >> score;
                    if(score!=0)
                    {
                        cnt++;
                    }
                }
                cout << "Case #"<< i+1 << ": "<< cnt<<endl;
            }
            else
            {
                forn(j,N)
                {
                    cin >> score;
                    if(score>=(3*p-2))
                    {
                        cnt++;
                    }
                    if(score==(3*p-3) || score==(3*p-4))
                    {
                        cond++;
                    }
                }
                cnt+=min(S,cond);
                cout << "Case #"<< i+1 << ": "<< cnt<<endl;
            }
            cnt=0;
            cond=0;
        }
    }
}
