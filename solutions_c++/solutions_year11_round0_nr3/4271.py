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
                  vector <int> C;
                  int check=0;
                  for(int i=0;i<N;i++)
                          {
                                      int n;
                                      cin>>n;
                                      check^=n;
                                      C.push_back(n);            
                          }
                  if(check!=0)
                  cout<<"Case #"<<t+1<<": NO"<<endl;
                  else
                  {
                      sort(C.begin(),C.end());
                      int ret=0;
                      for(int i=1;i<C.size();i++)
                      ret+=C[i];
                      cout<<"Case #"<<t+1<<": "<<ret<<endl;
                  }
                          
    }
    return 0;
}
