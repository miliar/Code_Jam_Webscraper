#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <algorithm>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)
#define ll long long
#define clear(d) memset(d,0,sizeof(d))
#define INF 2000000000

using namespace std;

int main(){
  int CN;
  cin >> CN;
  For1(CI,CN){
    int N,K;
    cin >> N >> K;
    bool on = ((K+1)%(1 << N)==0);

    cout << "Case #" << CI << ": " << (on ? "ON" : "OFF") << endl;
  }
}
