#include <iostream>
#include <vector>
#include <set>
#include <fstream>
#include <cstring>
using namespace std;

int main(){

  ifstream in;
  ofstream out;
  
  in.open("c.in");
  out.open("c.out");
  int T;
  in >> T;
  
  int powers[10];
  
  powers[0] = 1;
  for(int i=1; i<10; i++)
    powers[i] = 10*powers[i-1];
  
  for(int t=1; t<=T; t++){
    bool used[2000010];
    memset(used,false,sizeof(used));
    int A,B;
    in >> A >> B;
    int c = 0;
    for(int v=A; v<=B; v++){
      if(used[v])
        continue;
      set<int> seen;
      int digs[10];
      int tmp = v;
      int p = 0;
      while(tmp>0){
        digs[p] = tmp%10;
        p++;
        tmp/=10;
      }
      
      for(int i=0; i<p; i++){
        if(digs[i] == 0)
          continue;
        int n = 0;
        for(int j=0; j<p; j++){
          n+=digs[(i-j + p)%p]*powers[p-1-j];
        }
        if(A<=n && n<=B){
          seen.insert(n);
          used[n] = true;  
        }
      }
      
      int n = seen.size();
      c += n*(n-1)/2;
    }
    out << "Case #" << t << ": " << c << endl;
  }
  return 0;
}
