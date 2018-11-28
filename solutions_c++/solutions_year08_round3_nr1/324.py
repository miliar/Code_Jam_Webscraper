#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

#define pb push_back

int main(){

  int N;
  cin>>N;
  for(int no=1;no<=N;no++){
    
    int max_letters,key_count,letter_count;
    cin>>max_letters>>key_count>>letter_count;
    
    vector<int> freq;freq.clear();
    int temp;
    for(int i=0;i<letter_count;i++){
      cin>>temp;
      if(temp!=0)
	freq.pb(temp);
    }

    sort(freq.begin(),freq.end());

    int count=0;
    int fac=1;
    int key_used=0;
    bool chck=false;
    for(int i=freq.size()-1;i>=0;i--){
      
      count+=fac*freq[i];
      key_used++;
      if(key_used==key_count){
	key_used=0;
	fac++;
	if(fac>max_letters)chck=true;
      }
    }

    if(chck)cout<<"Case #"<<no<<": "<<count<<endl;
    else
      cout<<"Case #"<<no<<": "<<count<<endl;
  }

}
