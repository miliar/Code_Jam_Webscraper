#include <iostream>
#include <stdio.h>
using namespace std;

int T, A, B, length;

void recycleStep(int a[]){
  int last=a[length-1];
  for(int i=length-1;i>=1;i--){
    a[i]=a[i-1];
  }
  a[0]=last;
}

int main(){
freopen("C-small-attempt0.in", "r", stdin);
freopen("output.txt", "w", stdout);

cin >> T;

for(int i=0;i<T;i++){
  cin >> A >> B;
  int ans = 0;

  length = 0;
  int power = 1;
  for(int j=A;j>0;j/=10){
    length++;
    power *= 10;
  }

  int m[length];
  for(int j=A;j<B;j++){
    int x=j;
    for(int k=length-1;k>=0;k--){
      m[k] = x % 10;
      x /= 10;
    }

    bool tried[power];
    for(int k=0;k<power;k++)
      tried[k]=false;

    for(int k=0;k<length-1;k++){
      recycleStep(m);

      int m2 = m[0];
      for(int l=1;l<length;l++)
        m2 = m2*10 + m[l];

      if(m2>j && m2<=B && tried[m2]==false){
        ans++;
        tried[m2]=true;
      }
    }

  }
  cout << "Case #" << i+1 << ": " << ans << endl;
}

return 0;
}
