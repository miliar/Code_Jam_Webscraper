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


int n; 
int s, t;
int ans; 
int dp[110][1010];

string ssin;
string qin;
map<string, int> mti;

const int M = 1010;


int main()
{
    freopen("in.cpp", "r+", stdin);
    freopen("A-large.out", "w+", stdout);
    
    cin>>n;
    
    for(int ii =1; ii <= n; ii++) {
        
        mti.clear();
        ans = M;
        
        cin>>s;
        getline(cin, ssin);
        for(int i = 0; i< s; i++) {
            getline(cin, ssin);
            
            mti[ssin] = i;
            
        }
        
        cin>>t;
        
        getline(cin, ssin);
        for(int i=0; i< t; i++) {
           getline(cin, qin);
            //cout<<qin<<endl;
            int x = mti[qin];
            if(i == 0) {
                
                for(int j = 0; j < s; j++) {
                    if(j == x) {
                        dp[j][i] = M;
                    } else {
                        dp[j][i] = 0;
                    }
                }
            } else {
                for(int j = 0; j < s; j++) {
                    if(j == x) {
                        dp[j][i] = M;
                    } else {
                        dp[j][i] = M;
                        for(int k = 0; k < s; k++) {
                            dp[j][i] = min(dp[k][i-1] + (k!=j), dp[j][i]);
                        }
                    }
                }   
                
            }
            
        }
        
        
        for(int i = 0; i < s; i++) {
            ans = min(ans, dp[i][t-1]);
        }
        
        
        cout<<"Case #"<<ii<<": "<<ans<<endl;
    }
    
    //system("pause");
    return 0;
    
}
