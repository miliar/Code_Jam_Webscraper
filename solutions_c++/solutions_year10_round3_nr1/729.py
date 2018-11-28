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

int A[1010];
int B[1010];

int main(){
  int CN;
  cin >> CN;
  For1(CI,CN){
    int N;
    cin >> N;
    For(i,N){
      cin >> A[i] >> B[i];
    }
    int res=0;
    For(i,N){
      For(j,N){
        if(i==j) continue;
        if(A[i]>A[j] && B[i]<B[j]) res++;
      }
    }

    cout << "Case #" << CI << ": " << res << endl;
  }
}
