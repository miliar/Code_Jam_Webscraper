#include <iostream>
#include <queue>
#include <fstream>
using namespace std;
int num[1005];
int main()
{
    int cas,cnt,R,K,N,i,j,k,ans;
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small.out");
    fin>>cas;
    for(cnt=1;cnt<=cas;cnt++)
    {     queue<int> q,p;
          fin>>R>>K>>N;
          for(i=0;i<N;i++)
          {
              fin>>k;
              q.push(k);
          }
          ans=0;
          for(i=0;i<R;i++)
          {   j=0;
              while(!q.empty())
              {
                  k=q.front();
                  if(j+k>K)
                    break;
                  q.pop();
                  p.push(k);
                  j+=k;
              }
              while(!p.empty())
              {
                   k=p.front();
                   p.pop();
                   q.push(k);
              }
              ans+=j;
          }
          fout<<"Case #"<<cnt<<":"<<" "<<ans<<endl;

    }
}
