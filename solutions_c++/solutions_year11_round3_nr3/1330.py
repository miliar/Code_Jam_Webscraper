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
    int n;
    long long l,h;
    cin>>n;
    cin>>l;
    cin>>h;
    vector<int> note(n);
    for(int i=0;i<n;i++)cin>>note[i];
    for(int i=l;i<=h;i++){
      int j=0;
      for(j=0;j<n;j++){
	int a=min(i,note[j]);
	int b=max(i,note[j]);
	if(b%a==0)continue;
	else break;
      }
      if(j==n){
	cout<<i<<"\n";
	goto skip;
      }
    }
    cout<<"NO\n";
  skip:
    continue;
  }
  return 0;
}


