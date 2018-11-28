#include <iostream>
#include <vector>

using namespace std;

int delete_cost,insert_cost,smooth_limit;
vector<int> v;
const int most=256;
const int infinity=999999999;
int key;

int cost();
inline int dist(int a,int b);

inline int insert_modify_cost(int value,int new_value,int item);

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    key++;
    int n;
    cin>>delete_cost>>insert_cost>>smooth_limit>>n;
    v=vector<int>(n);
    for(int j=0;j<n;j++)
      cin>>v[j];
    cout<<"Case #"<<i+1<<": "<<cost()<<'\n';
    //cout<<"d="<<delete_cost<<" i="<<insert_cost<<" M="<<smooth_limit<<" : ";
    //for(int j=0;j<v.size();j++) cout<<v[j]<<' '; cout<<'\n';
  }
}

int memo(int position,int value);
int brute_force(const vector<int>& v);

int cost(){
  int ret=v.size()*delete_cost;
  for(int i=0;i<v.size();i++)
    for(int j=0;j<most;j++){
      int now=i*delete_cost+dist(v[i],j)+memo(i+1,j);
      ret=min(ret,now);
    }
  //assert(ret==brute_force(v));
  return ret;
}

const int N=100;
int cache[N][most],cached[N][most];

int memo(int position,int value){
  if(position==v.size()) return 0;
  if(cached[position][value]==key)
    return cache[position][value];
  cached[position][value]=key;
  int& ret=cache[position][value]=delete_cost+memo(position+1,value);
  for(int new_value=0;new_value<most;new_value++){
    int now=insert_modify_cost(value,new_value,v[position])+memo(position+1,new_value);
    ret=min(ret,now);
  }
  return ret;
}

int dist(int a,int b){
  return abs(a-b);
}

inline int insert_modify_cost(int value,int new_value,int item){
  int modify_cost=dist(new_value,item);
  int d=dist(value,new_value);
  int insert_costs=0;
  if(d>smooth_limit){
    if(smooth_limit==0) return infinity;
    d--;
    insert_costs=d/smooth_limit*insert_cost;
  }
  return modify_cost+insert_costs;
}

int brute(const vector<int>& v){
  if(v.size()<=1) return 0;
  int ret=infinity;
  if(v.size()==2){
    for(int a=0;a<most;a++)
      for(int b=0;b<most;b++){
        int now=dist(v[0],a)+dist(v[1],b)+insert_modify_cost(a,b,b);
        ret=min(now,ret);
      }
  }
  if(v.size()==3){
    for(int a=0;a<most;a++)
      for(int b=0;b<most;b++)
        for(int c=0;c<most;c++){
          int now=dist(v[0],a)+dist(v[1],b)+insert_modify_cost(a,b,b)+dist(v[2],c)+insert_modify_cost(b,c,c);
          ret=min(now,ret);
        }
  }
  return ret;
}

int brute_force(const vector<int>& v){
  int ret=infinity;
  for(int n=0;n<(1<<v.size());n++){
    vector<int> now;
    int c=0;
    for(int i=0;i<v.size();i++)
      if(n&(1<<i))
        now.push_back(v[i]);
      else
        c+=delete_cost;
    c+=brute(now);
    ret=min(ret,c);
  }
  return ret;
}
