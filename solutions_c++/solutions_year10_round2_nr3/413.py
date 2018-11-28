#include<fstream>
#include<iostream>
#include<bitset>
#include<deque>
#include<cstdlib>
#include<vector>
#include<cmath>
using namespace std;

bitset<30> works;
vector<int> shiz;
bool worksy()
{
     int loc=shiz.size()-1;
     bool was;
     while(loc>0)
     {
                 was=true;
                  for(int i=0;i<loc;i++)
                  {
                          if(shiz[i]==loc+1)
                          {
                                          was=false;
                                          loc=i;
                          }
                  }
                  if(was)
                  {
                         return false;
                  }
     }
     return true;
}
                  
int main()
{
    ifstream fin("C-small-attempt1.in");
    ofstream fout("C-small-attempt1.out");
    int n,T,ans;
    fin>>T;
    for(int cas=1;cas<=T;cas++)
    {
            fin>>n;
            ans=0;
            int x=int(pow(2.0,n-2)+0.1);
            fout<<"Case #"<<cas<<": ";
            for(int i=0;i<x;i++)
            {
                    works=bitset<30>(i);
                    shiz.clear();
                    
                    for(int j=0;j<n-2;j++)
                    {
                            if(works[j])
                            {
                                        shiz.push_back(j+2);
                            }
                    }
                    shiz.push_back(n);
                   /* for(int j=0;j<shiz.size();j++)
                    {
                            fout<<shiz[j]<<" \n";
                    }
                    fout<<"\n";*/
                    if(worksy())
                    { ans++;
                  //  fout<<"TICK\n";
                    }  
            }
            fout<<ans%100003<<"\n";
            
            
            
    }
    fin.close();
    fout.close();
}
