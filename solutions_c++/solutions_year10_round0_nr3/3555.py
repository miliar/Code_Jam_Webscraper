#include <iostream>
#include <fstream>
#include <cstdlib>
#include <deque>
using namespace std;
#define ON 0
#define OFF 1
int main()
{
  ifstream cin("C-small-attempt0.in");
  ofstream cout("C-small.out");
  int T,R,k,N,g,M=1;
  cin>>T;
  while(T--)
  {
    int ret=0,psg=0,t,Z,ZZ;
    deque<int> q;
    cin>>R>>k>>N;ZZ=Z=N;
    while(N--) { cin>>g; q.push_back(g); }
    //yi tang:
    while(R--)
    {
      while(psg+q.front() <= k && Z>0)
      { 
        ret+=q.front(); psg+=q.front(); 
        t = q.front(); q.pop_front(); q.push_back(t);
        Z--;
      }
      t=0; psg=0; Z=ZZ;
    }
    cout<<"Case #"<<M++<<":"<<" "<<ret<<endl;
  }
}