#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

int main()
{
    ifstream inp;
    ofstream op;
    inp.open("C-small-attempt0.in");
    op.open("C-small.out");
    
    int T,R,k,N;
    inp >> T;
    
    for (int i=0;i<T;i++)
    {
        queue<int> people;
        queue<int> roller;
        inp >> R >> k >> N;
        int gr,cap=0,profit=0;
        for (int j=0;j<N;j++)
        {
            inp >> gr;
            people.push(gr);
        }
        for (int j=0;j<R;j++)
        {
            while(!people.empty() && (cap + people.front())<=k)
            {
                gr=people.front();
                people.pop();
                cap+=gr;
                roller.push(gr);
            }
            while (!roller.empty())
            {
                gr=roller.front();
                roller.pop();
                people.push(gr);
            }
            profit+=cap;
            cap=0;
        }
        op << "Case #" << i+1 << ": " << profit << "\n";
        
    }
    
    inp.close();
    op.close();
    return 0;
}