#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<pii,int> piii;
typedef vector<piii> vpiii;
struct fenwick{
  vi T;
  fenwick(int n){T.resize(n,0); }
  void inc(int x,int add){for(;x<T.size();x|=x+1)T[x]+=add; }
  int query(int a,int b){
    if(a==0){
      int sum =0;
      for(;b>=0;b=(b&(b+1))-1)sum+=T[b];
    }
    else return query(0,b) - query(0,a-1);
  }
};
class psums{
public:
  vi vec;
  psums(int n);
  void update(int,int);
  int get(int i);
};
inline int parent(int i){return (i-1)/2;}
inline int rightchild(int i){return 2*i+2;}
inline int leftchild(int i){return 2*i+1;}
psums::psums(int size){
  int l = log2(size);
  vec = vi(1<<(l+2),0);
}
void psums::update(int index,int delta){
  int leaf = index+vec.size()/2 -1;  
  while(leaf){
    vec[leaf]+=delta;    
    leaf = parent(leaf);        
  }
  vec[leaf]+=delta;  
}
int psums::get(int index){
  int last = index+vec.size()/2-1;
  int sum = vec[last];
  int next = parent(last);
  while(last){
    if(rightchild(next)==last) sum+=vec[leftchild(next)];
    last = next;next=parent(next);
  }
  return sum;
}
			  

int main(int argc,char*argv[]){
  int T,N,a,b;
  vi A,B;
  cin >> T;
  for(int i=1;i<=T;++i){
    cin >> N;
    vpiii p;
    for(int j=0;j<N;++j){
      cin >> a >> b;
      //cout << "line " << a << "  " << b << endl;
      p.push_back(piii(pii(a,b),0));
      p.push_back(piii(pii(b,a),1));
    }
    sort(p.begin(),p.end());
    fenwick alive(100002);
    psums al(10002);
    long long res=0;
    for(int j=0;j<p.size();++j){;
      piii cur = p[j];
      if(cur.second==0) {
	//cout << "inserting " << cur.first.second << " " << endl;
	//res = res +((long long) alive.query(cur.first.second,10001));
	res += al.get(10001)-al.get(cur.first.second);
	//cout << "query " << alive.query(cur.first.second,10001);
	//alive.inc(cur.first.second,1);
	al.update(cur.first.second,1);
      }
      else {
	//alive.inc(cur.first.first,-1);	
	//al.update(cur.first.first,-1);

      }
    }
    cout << "Case #" << i << ": " << res << endl;
  }
  return 0;
}
  


