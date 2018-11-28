#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <limits.h>

#define  F first
#define  S second

using namespace std;

int ntest,n,m;
string s[55];
int dem1(int x,int y){
    if (x == n-1) return -1;
    if (y == m-1) return -1;
    if (s[x][y+1] == '#' && 
    s[x+1][y] == '#' && 
    s[x+1][y+1] == '#')
    return 1; else return -1;
}
void solve(){
        int cnt = 0;
        
        cin >> n >> m;
        for(int i = 0;i<n;i++) {    
            cin >> s[i];
            for(int j = 0;j<m;j++) if (s[i][j] == '#')
              cnt ++;
        }
        
        if (cnt % 4 != 0) {
            cout << "Impossible" << endl;
            return;
        }
        
        while(""){
            bool found = false;
            for(int i = 0;i<n;i++)   {
                for(int j = 0;j<m;j++)
                 if (s[i][j] == '#')  {
                    found = true;    
                    int cur = dem1(i,j);
                    if (cur ==-1) {
                        cout << "Impossible" << endl;
                        return;   
                    }         
                    s[i].replace(j,1,1,'/');
                    s[i].replace(j+1,1,1,'\\');                    
                    s[i+1].replace(j,1,1,'\\');                    
                    s[i+1].replace(j+1,1,1,'/');                                        
                    
                }
            }
            if (!found) break;
        }

        for(int i = 0;i<n;i++) cout << s[i] << endl;        
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);    
    cin >> ntest;
    for(int r = 0;r<ntest;r++){
        cout << "Case #"<< r+1 <<":" << endl; ; 

        solve();
        
    }

//    system("pause");
    return 0;
}

