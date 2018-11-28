#include<iostream>
#include<string>
using namespace std;

long T, N, P;
char rob;

long rpos[2], rbank[2];
long total_time;

long abs(long n){
  return (n<0?-n:n);
}

long max(long n,long m){
  return (m>n?m:n);
}

int main(){
  cin >> T;
  for(int round=0; round<T; round++){
    cin >> N;
    rpos[0] = 1;
    rpos[1] = 1;
    total_time = 0;
    rbank[0] = 0;
    rbank[1] = 0;
    for(int but=0; but<N; but++){
      cin >> rob >> P;
      long botnum = (rob=='O'?0:1);
      long otherbot = 1-botnum;
      long distance = abs(P-rpos[botnum]);
      long time_taken = max(distance-rbank[botnum]+1,1);
      total_time += time_taken;
      rpos[botnum] = P;
      rbank[botnum] = 0;
      rbank[otherbot] += time_taken;
    }
    cout << "Case #" << (round+1) << ": " << total_time << endl;
  }
}
