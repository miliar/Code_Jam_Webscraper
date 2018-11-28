/* 
 * 
 * File:   C.cpp
 * Author: Andy Huang
 * Created on April 13, 2012, 7:47 PM
 */

#include <stdio.h>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <stack>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <fstream>
#include <set>
#include <map>
#include <sstream>
#include <deque>

#define forl(a,b,c) for (int a=b;a<c;a++)
#define ford(a,b,c) for (int a=b;a>=c;a--)
#define gl(s) getline(cin,s)
#define pln(x) cout << (x) << '\n'
#define ve(x) vector<x>
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define ms(x,n) memset(x,n,sizeof(x))

using namespace std;

int f[2000005];
//bool moi[2000005];
const int ten[7] = {1,10,100,1000,10000,100000,1000000};
int num[10];

int rot(int len){
  int fd = num[0];
  forl(i,0,len){
    num[i] = num[i+1];
  }
  num[len] = fd;
  int ans = 0;
  forl(i,0,len+1){
    ans *= 10;
    ans += num[i];
  }
  return ans;
}

void solve() {
  int a,b;
  cin >> a >> b;
  int cnt = 0;
  forl(i,a,b+1){
    int cur = i;
    int len = 0;
    while(cur){
      len++;
      cur /= 10;
    }
    cur = i;
    ms(num,0);
    len--;
    ford(j,len,0){
      num[j] = cur % 10;
      cur /= 10;
    }
    //cout << "i:"<<i<<","<<len<<endl;   
    forl(k,0,len){
      int aft = rot(len);
      //pln(aft);
      if (a <= i && i < aft && aft <=b){
        //cout << i << "," << aft << endl;
        cnt++;
      }
    }
  }
  pln(cnt);
}


int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.out", "w", stdout);
  ms(f,0);
  //ms(moi,0);

  int t;
  cin >> t;
  forl(i,1,t+1){
    printf("Case #%d: ",i);
    solve();
  }
  return 0;
}

