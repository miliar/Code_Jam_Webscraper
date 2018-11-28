/*
 * =====================================================================================
 *
 *       Filename:  C.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2010年05月08日 13时10分57秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  xiaoe (Zheng Yi), xiaoe@mail.ustc.edu.cn
 *        Company:  xiaoe.org
 *
 * =====================================================================================
 */

#include <iostream>
#include <vector>
#include <cstring>

using namespace std;
typedef long long llong;

const int Max = 1024;
int g[Max];
int hash[Max];
int acc[Max];


llong Step(int R, int k, int N) ;
int
main() {
    int T = 0;
    int num = 0;
    cin >> T;
    while(T--) {
        int R, k, N;
        cin >> R >> k >> N;
        memset(hash, -1, sizeof hash);
        memset(acc, 0, sizeof acc);
        for(int i = 0; i < N; ++i) {
            cin >> g[i]; 
        }
        llong res = Step(R, k, N);
        cout << "Case #" << ++num << ": " << res << endl;
    }
    return 0;
}
llong
Step(int R, int k, int N) {
   int index = 0; 
    int earn = 0;
    llong res = 0;

   for(int i = 0; i < R; ++i) {
    int cap = 0;
    int backindex = index;
    if(hash[index] != -1) {
        //loop.
        int h = hash[index];
        int loop = (i - h);
        int loopsum = 0; 
        for(int j = 0; j < h; ++j) res += acc[j];
        for(int j = h; j < i; ++j) loopsum += acc[j];
        //cout << "part 1 " << res << endl;
        res += 1LL * loopsum * ((R - h) / loop); 
        int up = (R-h) % loop;
        //cout << "part 2 " << res << endl;
        for(int j = 0; j < up; ++j) res += acc[j+h]; 
        return res;
    }
    earn = 0;
    for(int j = 0; cap + g[index] <= k && j < N; ++j) {
        cap += g[index];
        earn += g[index++];
        if(index == N) {
            index = 0;
        }
     }
        //cout << "--" << index << endl;
     hash[backindex] = i;
     acc[i] = earn;
   }
    for(int i = 0; i < R; ++i) res += acc[i]; 
   return res;
}
