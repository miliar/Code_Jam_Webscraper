#include<iostream>
#include<deque>
#include<algorithm>
using namespace std;

int p,n;
deque < pair<char , int> > all , b_set , o_set;
int main(){
  cin>>p;
  for(int i = 0 ; i < p ; i++){
    all.clear();
    b_set.clear();
    o_set.clear();
    
    cin>>n;
    for(int j = 0 ; j < n ; j++){
      char c;
      int t;
      cin>>c>>t;
      all.push_back(pair<char , int>(c,t));
      if(c == 'O'){
	o_set.push_back(pair<char , int>(c,t));
      }
      else{
	b_set.push_back(pair<char , int>(c,t));
      }
    }
    int o = 1;
    int b = 1;

    int n_o = 0;
    int n_b = 0;
    if(!o_set.empty()){
      n_o = abs(o_set[0].second - o);
      o_set.pop_front();
    }

    if(!b_set.empty()){
      n_b = abs(b_set[0].second - b);
      b_set.pop_front();
    }

    int count = 0;
    while(!all.empty()){
      pair<char , int> next = all[0];
      all.pop_front();
      if(next.first == 'O'){
	o = next.second;
	int diff = n_o;
	n_b = n_b-(diff+1);
	if(n_b <0)n_b = 0;
	count += diff;
	count++;

	if(!o_set.empty()){
	  n_o = abs(o_set[0].second - o);
	  o_set.pop_front();
	}
      }
      else{
	b = next.second;
	int diff = n_b;
	n_o = n_o -(diff + 1);
	if(n_o < 0) n_o = 0;
	count+= diff;
	count++;
	if(!b_set.empty()){
	  n_b = abs(b_set[0].second - b);
	  b_set.pop_front();
	}
      }
      //      cout<<count<<" n_o "<<n_o<<" n_b "<<n_b<<endl;
    }
    cout<<"Case #"<<i+1<<": "<<count<<endl;

  }
  
}
