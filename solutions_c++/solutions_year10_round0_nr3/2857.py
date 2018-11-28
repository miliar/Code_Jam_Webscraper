#include <iostream>
#include <list>
#include <fstream>
using namespace std;
int main()
{
    ofstream out("th.out");
    fstream in("th.in");
    int R;
    in>>R;
    for(int j=0;j<R;j++)
    {
        int k,lim,N;
        in>>k>>lim>>N;
        list<int> groups;
        for(int i=0;i<N;i++)
        {
                int tmp;
                in>>tmp;
                groups.push_back(tmp);
        }
        int wyn=0;
        while(k>0)
        {
                  k--;
                  int people=0;
                  int t=0;
                  while(people<=lim)
                  {
                                    int tmp=groups.front();
                                    t++;
                                    if(tmp+people>lim || t>N)break;
                                    wyn+=tmp;
                                    people+=tmp;
                                    groups.pop_front();
                                    groups.push_back(tmp);
                  
                  }
        
        }
        out<<"Case #"<<j+1<<": "<<wyn<<endl;
    }
}
