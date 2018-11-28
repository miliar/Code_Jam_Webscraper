/*
 * Author: OldY
 * Created Time:  2011/5/7 10:36:06
 * File Name: A.cpp
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

struct node{
    int c,p,w;
} arr[100+10];
char tmp;
int T,n;
bool f0,f1;
int c0,c1;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("Alo.txt","w",stdout);
    cin >> T;
    for(int t = 0 ; t < T ; t++){
        arr[0].c = 0;arr[0].p = 1;arr[0].w = 0;
        arr[1].c = 1;arr[1].p = 1;arr[1].w = 0;
        cin >> n;
        for(int i = 2;i < n+2; i++){           
            cin >> tmp >> arr[i].p;
            if(tmp == 'O')
                arr[i].c = 0;
            else
                arr[i].c = 1;
        }
        for(int i = 2 ; i < n + 2 ; i++){
            f0 = f1 = false;
            for(int j = i-1 ; !f0 || !f1 ; j--){
                if(arr[j].c == 0){
                    if(!f0){
                        f0 = true;
                        c0 = j;
                    }
                }
                if(arr[j].c == 1){
                    if(!f1){
                        f1 = true;
                        c1 = j;
                    }
                }
            }
            if(arr[i].c == 0)
                arr[i].w = max(abs(arr[c0].p - arr[i].p) + 1+arr[c0].w , arr[c1].w+1);
            else
                arr[i].w = max(abs(arr[c1].p - arr[i].p) + 1+arr[c1].w, arr[c0].w+1);
        }
        //for(int i = 2 ; i < n+2 ; i++){
            //cout << arr[i].c <<" " << arr[i].w << endl;
        //}
        cout << "Case #" << t+1 << ": ";
        cout << arr[n+1].w << endl;
    }
    return 0;
}

