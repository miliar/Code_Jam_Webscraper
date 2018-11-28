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

int A[1000];
int B[1000];

int gojo(int a, int b){
  int c;
  while(b){
    c=a%b;
    a=b;
    b=c;
  }
  return a;
}

int main(){
  int CN;
  cin >> CN;
  For1(CI,CN){
    clear(A);
    int N;
    cin >> N;
    For(i,N){
      cin >> A[i];
    }
    int minx=INF;
    int mini=-1;
    For(i,N){
      if(A[i]<minx){
        minx=A[i];
        mini=i;
      }
    }
    int N2=0;
    for(int i=0;i<N;i++){
      if(A[i]==minx)
        continue;
      B[N2]=A[i];
      N2++;
    }
    For(i,N2){
      B[i]=B[i]-minx;
    }
    int gcm= (N2==1) ? B[0] : (B[0]<B[1]) ? gojo(B[1],B[0]) : gojo(B[0],B[1]);
    int res= minx%gcm;
    res = res==0 ? 0 : gcm-res;
    cout << "Case #" << CI << ": " << res << endl;
  }
}
