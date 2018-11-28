#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <list>
#include <cmath>
#include <deque>
#include <numeric>
#include <algorithm>

using namespace std;

int main(void){
  int T_NumberOfCases,NowCaseNumber;
  cin>>T_NumberOfCases;
  for(NowCaseNumber=1;NowCaseNumber<=T_NumberOfCases;NowCaseNumber++){
    cout<<"Case #"<<NowCaseNumber<<": ";
    int N_numberOfCandies;
    cin>>N_numberOfCandies;
    vector<int> candies(N_numberOfCandies);
    for(int i=0;i<N_numberOfCandies;i++)cin>>candies[i];
    unsigned int exist=0;
    for(int i=0;i<N_numberOfCandies;i++)exist^=candies[i];
    if(exist!=0)cout<<"NO"<<endl;
    else{
      sort(candies.begin(),candies.end());
      cout<<accumulate(candies.begin()+1,candies.end(),0)<<endl;
    }
  }
}

