#include <iostream>

using namespace std;


int fill_s(int N, int* s){
  
}


int main(){
  
  int T;
  cin >> T;

  
  
  for(int t=0; t<T; t++){
    int R, k, N;
    cin >> R >> k >> N;
    int g[N];
    for(int n=0; n<N; n++)
      cin >> g[n];

    long long a[N];
    int s[N];
    int p[N];
    for(int n=0; n<N; n++){
      a[n] = s[n] = -1;
      p[n]=0;
    }

    int cumul=0;
    int j=0;
    for(int i =0; i<N; i++){
      for(;j<i+N; j++){
        if(cumul+g[j%N]>k)
          break;
        cumul += g[j%N];
      }
      s[i] = j%N;
      a[i] = cumul;
      cumul -= g[i];
    }
    
    long long W=0;
    for(int r=0, c=0; r<R; r++){
      /*if(p[c]==0)
        p[c] = -r;
      else if(p[c]<0){
        p[c] += r;
        int rl = (R-r)/p[c];
        W += a[c] * (rl-1);
        r += rl;
      }*/
      W += a[c];
      c=s[c];
    }

    cout << "Case #"<< t+1 <<": " << W << endl;

}
  
  return 0;
}


