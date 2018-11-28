#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

bool compare(pair<int,int> a,pair<int,int> b){
  return (a.first<b.first);
}

int compare2(pair<int,int> a,pair<int, int> b){
  if(a.second<b.second)
    return 1;
  else
    return 0;
}

int main(void){
  int num_cases,curr_case,n,temp,inter;
  vector< pair<int,int> > array;
  vector<pair<int,int> >::iterator it1,it2;
  pair<int,int> temp_input;
  cin>>num_cases;
  for(curr_case=1;curr_case<=num_cases;curr_case++){
    inter=0;
    cin>>n;
    array.resize(0);
    array.resize(n);
    for(temp=0;temp<n;temp++){
      cin>>temp_input.first>>temp_input.second;
      array.push_back(temp_input);
    }
    sort(array.begin(),array.end(),compare);
    for(it1=array.begin();it1!=array.end();it1++){
      for(it2=it1;it2!=array.begin();it2--)
	inter+=compare2(*it1,*it2);
      inter+=compare2(*it1,*it2);
    }
    cout<<"Case #"<<curr_case<<": "<<inter<<endl;
    array.clear();
  }
  return 0;
}
