/*
 * Author: OldY
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
const int maxint = -1u>>1;
const double pi = acos(-1.0);


int T,r,c;
char map[55][55];

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        cin >> r >> c;
        bool can = true;
        for(int i = 0 ; i < r ; i++) scanf("%s",map[i]);
        for(int i = 0 ; i < r ; i++){
           for(int j = 0 ; j < c ; j++){
               if(map[i][j] == '#'){
                   if(i+1 < r && j+1 < c){
                       if(map[i+1][j] == '#' && map[i][j+1] == '#' && map[i+1][j+1] == '#'){
                           map[i][j] = '/';
                           map[i+1][j] = '\\';
                           map[i][j+1] = '\\';
                           map[i+1][j+1] = '/';
                           continue;
                       }
                       can = false;
                   }
                   //cout << "i = " << i << " j = " << j << " " << can << endl;
                   can = false;
               }
           }
        }
        cout << "Case #" << t << ":" << endl;
        if(!can) cout << "Impossible" << endl;
        else{
           for(int i = 0 ; i < r ; i++) printf("%s\n",map[i]);
        } 
    }
    return 0;
}

