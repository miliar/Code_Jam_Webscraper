//assumption: every character is variable
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

#define all(x) (x).begin(),(x).end()
#define forn(i,s,e) for(int i=(s),_e=(e);i<_e;i++)
#define rep(i,n) forn(i,0,n)
#define pb push_back 
#define db(i) cout<<#i<<"= "<<i<<endl; 

ifstream fin("A-large.in");
ofstream fout("output.out");

int main()
{
    int ntests;
    fin>>ntests;
    rep(i,ntests)
    {
        string num;
        fin>>num;
        map<char,int>mymap;
        bool used[40]={0};
        int place=0;
        rep(j,num.size())
        {
            //assign first symbol
            if(j==0)
            {
                if(mymap.count(num[j])==0)
                {
                    used[1]=true;
                    mymap[ num[j] ]=1;
                }
            }
            else
            {
                if(mymap.count(num[j])==0)
                {
                    while(used[place])
                    {
                        place++;
                    }
                    mymap[num[j]]=place;
                    used[place]=true;
                }
                
            }
        }
        //find unique symbols
        set<char>symbols;
        rep(j,num.size())
            symbols.insert(num[j]);
        int nsymbols=symbols.size();
        //change
        long long base=(nsymbols>1)?nsymbols:2;
        //db(base);
        //process 
        long long ans=0;
        long long prod=1;
        for(int j=num.size()-1;j>=0;j--)
        {
            //db(num[j]);
            //db(mymap[num[j]]);
            //db(prod);
            ans+=prod*mymap[ num[j] ];
            prod*=base;
            //db(ans);
        }
        fout<<"Case #"<<i+1<<": "<<ans<<endl;
    }                
    printf("done\n");
    int z;
    scanf("%d",&z);
    return 0;
}
