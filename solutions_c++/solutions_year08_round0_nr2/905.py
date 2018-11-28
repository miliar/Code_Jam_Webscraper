#include <vector>
#include <list>
#include <map>
#include <set>
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

const int M = 24*60;

int n; 
int t; 
int na, nb;
int ansa;
int ansb;

vector< pair<pair<int, int>, int> > vpi;

string as, bs;


int gets(string s)
{
    return ((s[0]-'0')*10+s[1]-'0')*60 + (s[3]-'0')*10+s[4]-'0';
}
 

void solve()
{
    bool f[vpi.size()];
    memset(f, 0, sizeof(f));
    
    for(int i=0; i < vpi.size(); i++) if(!f[i]){
         //cout<<vpi[i].first.second<<"  "<<vpi[i].first.first<<endl;
        //for(int i=0; i<vpi.size(); i++) cout<<f[i]<<endl;
        f[i] = 1;
        
        if(vpi[i].second) ansb++;
        else              ansa++;
        
        int y = vpi[i].first.second;
        int xx = vpi[i].second;
        
        for(int j = i+1; j < vpi.size(); j++) if(!f[j]) {
            
            if(vpi[j].second != xx) {
                
                if(vpi[j].first.first >= y+t) {
                    f[j] = 1; 
                    //cout<<xx<<"  "<<vpi[i].first.second<<"  "<<vpi[j].first.first<<endl;
                    y = vpi[j].first.second;
                    xx = vpi[j].second;
                }   
            }
        }
    }
    
    return;
} 

int main()
{
    freopen("B-large.in", "r+", stdin);
    //freopen("B-small.out", "w+", stdout);
    freopen("B-large.out", "w+", stdout);
    
    cin>>n;
    
    for(int i=0; i<M;i++) vpi.clear();
    
    for(int ii =1; ii <= n; ii++) {
        ansa = 0; 
        ansb = 0; 
        vpi.clear();
        
        cin>>t;
        cin>>na>>nb;
        
        for(int i = 0; i< na; i++) {
            cin>>as>>bs;
            int x = gets(as);
            int y = gets(bs);
             
            vpi.push_back(make_pair(pair<int, int>(x, y), 0));
        }
        
        for(int i = 0; i< nb; i++) {
            cin>>as>>bs;
            int x = gets(as);
            int y = gets(bs);
             vpi.push_back(make_pair(make_pair(x, y), 1));
        }
        
        sort(vpi.begin(), vpi.end());
        solve();
        
        cout<<"Case #"<<ii<<": "<<ansa<<" "<<ansb<<endl;
    }
}
