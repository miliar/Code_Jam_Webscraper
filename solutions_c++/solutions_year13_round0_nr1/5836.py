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
#include<fstream>
#include<cstring>
#define ll long long
using namespace std;


int main () {
    freopen("A-large.in", "r", stdin);
freopen("output.txt", "w", stdout);
    ll t,c,flag;
    cin >>t;
    getchar();
    for(ll i = 0;i < t;i++){
        flag=0;
        ll e =0;
        vector<vector <char> > vv;
        vector<char>v(4);
        for(ll j = 0;j<4;j++){
            for(ll k = 0;k<4;k++){
                cin>>v[k];
                if(v[k] == '.')
                    e++;
            }
            vv.push_back(v);
        }
        cout<<"Case #"<<i+1<<": ";
        c=0;
        char ch;
        //left dia
         if(vv[0][0] != '.' && vv[2][2] !='.')
         {
            ch = vv[0][0];
            if(vv[0][0] == 'T')
                    ch = vv[3][3];

        for(ll j = 0;j<4;j++){
            for(ll k = 0;k<4;k++){
                if(j == k){
                    if(vv[j][k] == ch || vv[j][k] == 'T')
                        c++;
                }
            }
        }
        if(c == 4){
            cout<<ch << " won"<<endl;
            continue;
        }
    }
        c=0;

        //right dia
         if(vv[3][0] != '.' && vv[2][1] !='.')
         {
             ch = vv[3][0];
                if(vv[3][0] == 'T')
                    ch = vv[0][3];

        for(ll j = 0;j<4;j++){
            for(ll k = 0;k<4;k++){
                if(j+k == 3){
                    if(vv[j][k] == ch || vv[j][k] == 'T')
                        c++;
                }
            }
        }
         }
          if(c == 4){
            cout<<ch << " won"<<endl;
            continue;
        }
        c = 0;
        for(ll j = 0;j<4;j++){
            for(ll k = 0;k<4;k++){
                if(vv[j][k] == '.')
                    continue;
                c=0;

                //col
                for(ll l = 0;l<4;l++){
                    if(vv[l][k] == vv[j][k] || vv[l][k] == 'T')
                    c++;
                }
                  if(c == 4){
                    cout<<vv[j][k] << " won"<<endl;
                    flag = 1;
                    break;
                }
                c=0;
                //row
                for(ll l = 0;l<4;l++){
                    if(vv[j][l] == vv[j][k] || vv[j][l] == 'T')
                    c++;
                }
                  if(c == 4){
                    cout<<vv[j][k] << " won"<<endl;
                    flag = 1;
                    break;
                }


            }
            if(flag==1)
                break;

        }
        if(e == 0 &&flag==0)
        cout<<"Draw"<<endl;
        else if(e!=0 &&flag==0)
        cout<<"Game has not completed"<<endl;
    }

  return 0;
}
