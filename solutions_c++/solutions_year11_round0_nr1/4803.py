#include <fstream>
#include <iostream>
#include <queue>
#include <cstdlib>
using namespace std;

struct button
{
  button(int n, int pr) : n(n), pr(pr) {}
  int n;
  int pr;
};

int main()
{
  int T, N;

  ifstream in("data.in");
  ofstream out("data.out");
  in >> T;

  for(int iter = 0;iter < T;++iter)
  {
    in >> N;
    queue<button> q[2];
    int pos[2] = {1,1};
    char R; int P;
    for(int i = 0;i < N;++i)
    {
      in >> R >> P;
      q[R == 'B' ? 0 : 1].push(button(P,i));
    }
    
    int t = 0;
    for(t = 0;!q[0].empty() || !q[1].empty();++t)
    {
      bool pop[2] = {false,false};
      for(int c = 0;c < 2;++c)
      {
        if(q[c].empty()) continue;

        if(q[c].front().n > pos[c]) ++pos[c]; 
        else if(q[c].front().n < pos[c]) --pos[c];
        else if(q[1-c].empty() || q[c].front().pr < q[1-c].front().pr)
          pop[c] = true;
      }
      for(int c = 0;c < 2;++c) if(pop[c]) q[c].pop();
    }
    out << "Case #" << iter+1 << ": " << t << "\n";
  }
  out.close();
  return 0;
}
