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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits.h>
#include <string.h>
 
#define repx(i,x,n) for(int i=x;i<n;i++)
#define rep(i,n) repx(i,0,n)
#define pb push_back
#define full(v)  v.begin(),v.end()
#define np next_permutation
#define VI vector<int>
#define VS vector<string>
#define VC vector<char>
#define VD vector<double>
#define VF vector<float>
#define SI set<int>
#define SC set<char>
#define SS set<string>
#define MII map<int,int>
#define MSI map<string,int>
#define MIS map<int,string>
#define MIC map<int,char>
#define MCI map<char,int>
#define LL long long
using namespace std;


int main()
{
    ofstream cout ("Abig.out");
    ifstream cin ("Abig.in");
    int test,cas;
    cin>>test;
    cas = 0;
    while(test-- && ++cas)
    {
    VS b;
    bool xwin,owin,empty;
    xwin = owin = false;
    empty = false;
    rep(i,4)
    {
            string temp;
            cin>>temp;
            b.pb(temp);
            rep(j,4)
             if(temp[j] == '.')
              empty = true;
    }
    bool tx,to;
            
    rep(i,4)
    {
            tx = true;
            rep(j,4)
            {
             if(b[i][j] == 'O' || b[i][j] == '.')
             {
                            tx = false;
                            break;
             }
            }
            if(tx)
            {
                  xwin = true;
                  break;
            }
            tx = true;
            rep(j,4)
            {
             if(b[j][i] == 'O' || b[j][i] == '.')
             {
                            tx = false;
                            break;
             }
            }
            if(tx)
            {
                     
                  xwin = true;
                  break;
            }
    }
    if(!xwin)
    {
             tx = true;
             rep(i,4)
             {
                     if(b[i][i] == 'O' ||b[i][i] == '.')
                     {
                                tx = false;
                                break;
                     }
             }
             if(tx)
             {
              xwin = true;
             }
             else
             {
             tx = true;
             rep(i,4)
             {
                     if(b[i][3-i] == 'O' || b[i][3-i] == '.')
                     {
                                tx = false;
                                break;
                     }
             }
             if(tx)
             {
              xwin = true;
             }
             }
    }
    
    // OWIN CHECK STARTS HERE
    
   if(!xwin)
   {
    rep(i,4)
    {
            to = true;
            rep(j,4)
            {
             if(b[i][j] == 'X' || b[i][j] == '.')
             {
                            to = false;
                            break;
             }
            }
            if(to)
            {
                  owin = true;
                  break;
            }
            to = true;
            rep(j,4)
            {
             if(b[j][i] == 'X' || b[j][i] == '.')
             {
                            to = false;
                            break;
             }
            }
            if(to)
            {
                  owin = true;
                  break;
            }
    }
    if(!owin)
    {
             to = true;
             rep(i,4)
             {
                     if(b[i][i] == 'X' ||b[i][i] == '.')
                     {
                                to = false;
                                break;
                     }
             }
             if(to)
             {
              owin = true;
             }
             else
             {
             to = true;
             rep(i,4)
             {
                     if(b[i][3-i] == 'X' ||b[i][3-i] == '.')
                     {
                                to = false;
                                break;
                     }
             }
             if(to)
             {
              owin = true;
             }
             }
    }
   }
    
    cout<<"Case #"<<cas<<": ";
    if(xwin)
    cout<<"X won\n";
    else if(owin)
    cout<<"O won\n";
    else if(empty)
    cout<<"Game has not completed\n";
    else
    cout<<"Draw\n";
    } 
    return 0;
}
