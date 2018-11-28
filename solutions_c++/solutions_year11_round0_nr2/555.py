/*
 * Author: OldY
 * Created Time:  2011/5/7 12:23:37
 * File Name: B.cpp
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

int T;
int d,c,n,cnt;
char list[200];
string com[50],op[50];
string inp;
bool co;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        cin >> c;
        for(int i = 0 ; i < c ; i++) cin >> com[i];
        cin >> d;
        for(int i = 0 ; i < d ; i++) cin >> op[i];
        cin >> n >> inp;
        cnt = 0;
        for(int i = 0 ; i < n ; i++){
            list[cnt++] = inp[i];
            co = false;
            if(cnt >= 2){
                for(int j = 0 ; j < c ; j++){
                    if((list[cnt-1] == com[j][0] && list[cnt-2] == com[j][1]) || (list[cnt-1] == com[j][1] && list[cnt-2] == com[j][0])){
                        cnt -= 2;
                        list[cnt++] = com[j][2];
                        co = true;
                        break;
                    }
                }
            }
            if(!co){
                for(int j = 0 ; j < cnt-1 ; j++){
                    for(int k = 0 ; k < d ; k++){
                        if((list[cnt-1] == op[k][0] && list[j] == op[k][1]) || (list[cnt-1] == op[k][1] && list[j] == op[k][0])){
                            cnt = 0;
                            break;
                        }
                    }
                }
            }
        }
        //cout << inp << " " << cnt << endl;
        cout << "Case #" << t << ": [";
        for(int i = 0 ; i < cnt-1 ; i++) cout << list[i] << ", ";
        if(cnt >= 1) cout << list[cnt-1];
        cout << "]" << endl;
    }
    return 0;
}

