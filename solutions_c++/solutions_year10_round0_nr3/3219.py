
#include <cmath>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;



    
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("o.txt","w",stdout);
    int N=0,T;
    cin>>T;
    while(T--)
    {
              N++;
              int r,k,n,euro=0;
              cin>>r>>k>>n;
              queue<int> st;
              for(int i=0;i<n;i++)
              {
                      int temp;
                      cin>>temp;
                      st.push(temp);
              }
              for(int i=0;i<r;i++)
              {
                      int tempk=k,temp;
                      queue<int> stemp;
                      while(tempk && !st.empty())
                      {
                                  
                                  if(tempk>=st.front())
                                  {
                                           temp=st.front();
                                           st.pop();
                                           stemp.push(temp);
                                           euro+=temp;
                                           tempk-=temp;
                                  }
                                  else
                                  tempk=0;
                      }
                      while(!stemp.empty())
                      {
                                  int t=stemp.front();
                                  stemp.pop();
                                  st.push(t);
                      }
              }
              cout<<"Case #"<<N<<": "<<euro<<"\n";
    }
    getchar();
}
