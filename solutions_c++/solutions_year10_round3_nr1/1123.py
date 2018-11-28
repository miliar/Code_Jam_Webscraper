#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>

#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

typedef long long lld; 
typedef unsigned long long llu;
typedef pair<int,int> poi;
typedef vector<poi> vpoi;

bool comp(const poi &a,const poi &b){
  return (a.first < b.first); 
}

llu solve(vpoi &v){
  sort(v.begin(),v.end(),comp);
  llu count = 0;
  for(int i=0;i<v.size();++i){
    int right = v[i].second;
    for(int j=i+1;j<v.size();++j){
      if(v[j].second < right){
        count++;
      }
    }
  }
  return count;
}

int main(){
  int n;
  scanf("%d ",&n);
  for(int i=0;i<n;++i){
    int m;
    scanf("%d ",&m);
    vpoi v;
    for(int j=0;j<m;++j){
      int x,y;
      scanf("%d %d",&x,&y);
      poi p(x,y);
      v.push_back(p);
    }
    llu result = solve(v);
    printf("Case #%d: %llu\n",i+1,result);
  }
}
