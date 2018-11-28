#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<map>
#include<vector>
#include<string>

using namespace std;

int solve(vector<int> v1, vector<int> v2);

int main()
{

  int iter;
  cin>>iter;

  for(int r=1;r<=iter;r++){

    vector<int> v1;
    vector<int> v2;
    int n;
    cin>>n;
    int d;
    for(int i=0;i<n;i++){
      cin>>d;
      v1.push_back(d);
    }

    for(int i=0;i<n;i++){
      cin>>d;
      v2.push_back(d);
    }



    cout<<"Case #"<<r<<": "<<solve(v1,v2);
    if(r < iter)
      cout<<endl;



  }

}

int solve(vector<int> v1, vector<int> v2){
  
  if(v1.size()==1)
    return v1[0]*v2[0];
  else{

    sort(v1.begin(),v1.end());
    sort(v2.begin(),v2.end());

    
    int sum1=v1[0]*v2[v2.size()-1];
    int sum2=v2[0]*v1[v1.size()-1];

    
    if(sum1 < sum2){
      v1.erase(v1.begin());
      v2.erase(v2.begin()+ v2.size()-1);
      
      return sum1 + solve(v1,v2);
    }
    else{ 
      v2.erase(v2.begin());
      v1.erase(v1.begin()+v1.size() -1);
      
      return sum2 + solve(v1,v2);
    }

  }
}
