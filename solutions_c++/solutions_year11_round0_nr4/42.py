#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
  int T,t=1;
  cin>>T;
  while(T--){
    int N,tmp;
    vector<int> nums;
    cin>>N;
    for (int i=0;i<N;i++){
      cin>>tmp;
      nums.push_back(tmp);
    }
    vector<int> sorted = nums;
    sort(sorted.begin(),sorted.end());
    int wrong=0;
    for (int i=0;i<N;i++)
      if (sorted[i]!=nums[i]) wrong++;
    cout<<"Case #"<<t++<<": "<<wrong<<endl;
  }
}
      

      
