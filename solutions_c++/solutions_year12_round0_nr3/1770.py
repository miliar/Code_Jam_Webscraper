#include<iostream>
#include<vector>
#include<set>
#include<cmath>
#include<algorithm>

using namespace std;

int cnt;
int A;
int B;
int AA;
int BB;

int solve(int a,int b);
int recycle(int x);

int main(){
  cin>>cnt;
  for(int i=0;i<cnt;i++){
    cin>>A>>B;AA=A;BB=B;
    while(true){
      if(AA<10 && BB<10)break;
      else{AA/=10;BB/=10;}
    }
    cout<<"Case #"<<i+1<<": "<<solve(A,B)<<endl;
  }

  return 0;
}

int solve(int a,int b){
  int res=0;

  for(int j=a;j<=b;j++){
    res+=recycle(j);
  }

  return res;
}

int recycle(int x){
  vector<int>tmp;vector<int>res;int ans=0;int jud=x;set<int>s;
  while(x>0){
    tmp.push_back(x%10);x/=10;
  }

  for(int i=1;i<tmp.size();i++){
    if(tmp[i-1]>=AA && tmp[i-1]<=BB){
      res.clear();
      for(int j=i;j<tmp.size();j++){
        res.push_back(tmp[j]);
      }
      for(int k=0;k<i;k++){
        res.push_back(tmp[k]);
      }
      int f=0;
      for(int l=0;l<res.size();l++){
        f+=(res[l]*pow(10.0,(double)l));
      }
      if(f>jud && f<=B && s.find(f)==s.end()){ans++;s.insert(f);}
    }
  }
  return ans;
}
