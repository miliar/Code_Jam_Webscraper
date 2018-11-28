#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
  
    int tests;
    cin>>tests;
    for(int t=0;t<tests;t++)
    {
                  int N;
                  cin>>N;
                  vector <int> Candies;
                  int cons=0;
                  for(int i=0;i<N;i++)
                          {
                                      int x;
                                      cin>>x;
                                      cons^=x;
                                      Candies.push_back(x);            
                          }
                  if(cons!=0)
                  cout<<"Case #"<<t+1<<": NO"<<endl;
                  else
                  {
                      sort(Candies.begin(),Candies.end());
                      int ret=0;
                      for(int i=1;i<Candies.size();i++)
                      ret+=Candies[i];
                      cout<<"Case #"<<t+1<<": "<<ret<<endl;
                  }
                          
    }
    return 0;
}
