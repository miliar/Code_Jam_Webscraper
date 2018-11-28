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

int IN[50];

int main(){
  int CN;
  cin >> CN;
  For1(CI,CN){
    clear(IN);
    int N;
    cin >> N;
    string str;
    For1(r,N){
      cin >> str;
      int c;
      for(c=N-1;c>=0;c--){
        if(str[c]=='1'){
          IN[r] = c+1;
          break;
        }
      }
      if(c<0) IN[r]=0;
    }
    int res=0;
    for(int r=1;r<N;r++){
      int f;
      for(f=r;IN[f]>r;f++);
      if(f>r){
        for(int i=f;i>r;i--){
          int tmp = IN[i];
          IN[i]=IN[i-1];
          IN[i-1]=tmp;
          res++;
        }
      }
    }

    cout << "Case #" << CI << ": " << res << endl;
  }
}
