#include <iostream>
#include <vector>

using namespace std;

const int infinity=999999999;

int bits(int n);
bool satisfy(pair<int,int>,int);

int main(){
  int t;
  cin>>t;
  for(int x=0;x<t;x++){
    cout<<"Case #"<<x+1<<":";
    int milkshakes,customers;
    cin>>milkshakes>>customers;
    int malted_answer=0,most_malts=infinity;
    vector<pair<int,int> > customer;
    for(int i=0;i<customers;i++){
      int malted=0,unmalted=0;
      int options;
      cin>>options;
      for(int j=0;j<options;j++){
        int flavor,maltedness;
        cin>>flavor>>maltedness;
        if(maltedness)
          malted|= (1<<(flavor-1));
        else
          unmalted|= (1<<(flavor-1));
      }
      customer.push_back(make_pair(malted,unmalted));
    }
    for(int set=0;set< (1<<milkshakes);set++){
      bool good=true;
      for(int i=0;i<customers;i++)
        if(!satisfy(customer[i],set)){
          good=false;
          break;
        }
      int malts=bits(set);
      if(good && malts<most_malts){
        most_malts=malts;
        malted_answer=set;
      }
    }
    if(most_malts==infinity)
      cout<<" IMPOSSIBLE\n";
    else{
      for(int i=0;i<milkshakes;i++)
        if(malted_answer & (1<<i))
          cout<<" 1";
        else
          cout<<" 0";
      cout<<'\n';
    }
  }
}

int bits(int n){
  int ret=0;
  while(n){
    if(n&1) ret++;
    n/=2;
  }
  return ret;
}

bool satisfy(pair<int,int> customer,int malted){
  if(customer.first & malted)
    return true;
  if(customer.second & ~malted)
    return true;
}
