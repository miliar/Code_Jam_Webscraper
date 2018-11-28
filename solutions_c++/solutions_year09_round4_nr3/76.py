#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<vector<int> > input();
vector<int> top_sort(const vector<vector<int> >& less_than);
vector<vector<int> > permute(const vector<int>& order,const vector<vector<int> >& matrix);
vector<int> lis(const vector<vector<int> >& less_than);
int answer_small(vector<vector<int> >& less_than);
void print(const vector<vector<int> >& v);
void print(const vector<int>& v);

int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    vector<vector<int> > less_than=input();
    //print(less_than);
    vector<int> v=top_sort(less_than);
    //cout<<"topsorted: "; print(v);
    less_than=permute(v,less_than);
    //print(less_than);
    cout<<"Case #"<<i<<": "<<answer_small(less_than)<<'\n';
  }
}

vector<vector<int> > permute(const vector<int>& order,const vector<vector<int> >& matrix){
  vector<vector<int> > ret(order.size(),vector<int>(order.size()));
  for(int i=0;i<ret.size();i++)
    for(int j=0;j<ret[i].size();j++)
      ret[i][j]=matrix[order[i]][order[j]];
  return ret;
}

bool smaller(const vector<int>& a,const vector<int>& b){
  for(int i=0;i<a.size();i++)
    if(a[i]>=b[i])
      return false;
  return true;
}

vector<vector<int> > input(){
  int n,k;
  cin>>n>>k;
  vector<vector<int> > stocks(n,vector<int>(k));
  for(int i=0;i<n;i++)
    for(int j=0;j<k;j++)
      cin>>stocks[i][j];
  vector<vector<int> > ret(n,vector<int>(n));
  for(int i=0;i<ret.size();i++)
    for(int j=0;j<ret.size();j++)
      ret[i][j]=smaller(stocks[i],stocks[j]);
  return ret;
}

void dfs(int node,const vector<vector<int> >& less_than,vector<int>& visited,vector<int>& ret){
  visited[node]=true;
  for(int i=0;i<less_than[node].size();i++)
    if(!visited[i] && less_than[i][node])
      dfs(i,less_than,visited,ret);
  ret.push_back(node);
}

vector<int> top_sort(const vector<vector<int> >& less_than){
  vector<int> ret;
  vector<int> visited(less_than.size());
  for(int i=0;i<less_than.size();i++)
    if(!visited[i])
      dfs(i,less_than,visited,ret);
  return ret;
}

/*
vector<int> lis(const vector<vector<int> >& less_than){
  vector<int> best(less_than.size());
  vector<int> parent(less_than.size(),-1);
  int bp=0;
  for(int a=0;a<less_than.size();a++){
    best[a]=1;
    for(int b=0;b<a;b++)
      if(less_than[b][a] && best[b]+1>best[a]){
        parent[a]=b;
        best[a]=best[b]+1;
      }
    if(best[a]>best[bp])
      bp=a;
  }
  vector<int> ret;
  while(bp!=-1){
    ret.push_back(bp);
    bp=parent[bp];
  }
  reverse(ret.begin(),ret.end());
  return ret;
}

vector<int> invert(const vector<int>& v,int n){
  int vp=0;
  vector<int> ret;
  for(int i=0;i<n;i++)
    if(vp>=v.size() || i!=v[vp])
      ret.push_back(i);
    else if(vp<v.size() && i==v[vp])
      vp++;
  return ret;
}

int answer(vector<vector<int> >& less_than){
  int ret=0;
  while(less_than.size()){
    ret++;
    vector<int> v=lis(less_than);
    cout<<"lis: "; print(v);
    vector<int> save=invert(v,less_than.size());
    cout<<"save: "; print(save);
    //print(less_than);
    less_than=permute(save,less_than);
    //print(less_than);
  }
  return ret;
}
*/

void print(const vector<vector<int> >& v){
  for(int i=0;i<v.size();i++){
    for(int j=0;j<v[i].size();j++)
      cout<<v[i][j]<<' ';
    cout<<'\n';
  }
}

void print(const vector<int>& v){
  for(int j=0;j<v.size();j++)
    cout<<v[j]<<' ';
  cout<<'\n';
}

const int N=16,S=1<<N,infinity=999999999;
int key=0;
int cache[S],cached[S];

bool works(const vector<vector<int> >& less_than,int set){
  int prev=-1;
  for(int i=0;i<less_than.size();i++)
    if(set&(1<<i)){
      if(prev>=0 && !less_than[prev][i]) return false;
      prev=i;
    }
  //cout<<set<<": works!\n";
  return true;
}

int memo(const vector<vector<int> >& less_than,const int set){
  if(cached[set]==key)
    return cache[set];
  cached[set]=key;
  int& ret=cache[set]=infinity;
  if(works(less_than,set))
    return ret=1;
  for(int subset=(set-1)&set;subset!=0;subset=(subset-1)&set){
    int now=memo(less_than,subset)+memo(less_than,set&~subset);
    ret=min(ret,now);
  }
  //cout<<set<<": "<<ret<<'\n';
  return ret;
}

int answer_small(vector<vector<int> >& less_than){
  key++;
  return memo(less_than,(1<<less_than.size())-1);
}
