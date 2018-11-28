#include <iostream>
#include <queue>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("C:\\C-small-attempt1.in.txt");
    ofstream out("C:\\ouou.txt");
    int r,k,n,g;
    int order = 1;
    int t,i,j,sum,p,b,count;
    queue<int> q;
    in>>t;
    while(t--)
    {
        b = 0;
        in>>r>>k>>n;
        for(i = 1; i <= n;++i)
        {
              in>>g;
              q.push(g);
        }
        while(r--)
        {
              sum = 0;
              count = 0;
              while(sum < k)
              {
                    p = q.front();
                    if(sum + p <= k && count < q.size())
                    {
                           ++count;
                           sum += p;
                           q.pop();
                           q.push(p);
                    }
                    else 
                         break;
              }
              b += sum;
        } 
        while(!q.empty())
              q.pop();
        out<<"Case #"<<order++<<": "<<b<<endl;
    }
    system("pause");
    return 0;
}
                    
                    
              
