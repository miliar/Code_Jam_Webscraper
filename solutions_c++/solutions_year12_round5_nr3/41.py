#include <cstdio>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>
#define int long long

using namespace std;

typedef pair<int,int> Pair;

template<class t>
ostream & operator << (ostream & tout,const vector<t> &s){
  tout<<'[';
  for (int i=0;i<s.size();i++)
    if (i+1 == s.size())
      tout<<s[i];
    else
      tout<<s[i]<<',';
  tout<<']';
  return(tout);
}

template<class a,class b>
ostream & operator << (ostream & tout,const pair<a,b> &c){
  return(tout<<'('<<c.first<<','<<c.second<<')');
}

template<class T> struct __set__print{
  __set__print(ostream& out) : tout(out), count(0) {}
  void operator() (T x) { 
    if (count > 0)
      tout<<',';
    tout<<x;
    ++count; 
  }
  ostream& tout;
  int count;
};

template<class T>
ostream & operator << (ostream & tout,const set<T> &s){
  tout<<'{';
  for_each(s.begin(),s.end(),__set__print<T>(tout));
  return(tout<<'}');
}

template<class T,class Q> struct print_map{
  print_map(ostream& out) : tout(out), count(0) {}
  void operator() (const pair<T,Q> &x) { 
    if (count > 0)
      tout<<',';
    tout<<'('<<x.first<<" => "<<x.second<<')';
    ++count; 
  }
  ostream& tout;
  int count;
};

template<class T,class Q>
ostream & operator << (ostream & tout,map<T,Q> s){
  tout<<'{';
  for_each(s.begin(),s.end(),print_map<T,Q>(tout));
  return(tout<<'}');
}

template<class T>
string to_string(T s){
  stringstream tin;
  tin<<s;
  string res;
  getline(tin,res);
  return(res);
}


template<class T>
vector<T> to_vector(T *s,int n){
  vector<T> result;
  for (int i=0;i<n;i++)
    result.push_back(s[i]);
  return(result);
}

// *********************************** MY CODE ***************************

const int MAX_N = 2000000+20;
const int INF = 1ll<<60;

int price[MAX_N],d[MAX_N],n,dyna[MAX_N],m,f,t[MAX_N];


#undef int
int main(){
#define int long long
  ios_base::sync_with_stdio(false) ;
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    cin>>m>>f>>n;
    for (int i=1;i<=n;i++)
      cin>>price[i]>>d[i];
    for (int i=0;i<MAX_N;i++)
      dyna[i] = INF;
    for (int i=1;i<=n;i++)
      dyna[d[i]+1] = min(dyna[d[i]+1],price[i]);
    int last = (*max_element(d+1,d+n+1))+1;
    for (int i=last;i>1;i--)
      dyna[i-1] <?= dyna[i];
    for (int i=2;i<=last;i++)
      dyna[i]+=dyna[i-1];

    int ans = 0;
    for (int i=0;i<=m;i++)
      t[i] = 0;
    for (int i=1;i<=last;i++)
      if (dyna[i] <= m)
	t[dyna[i]] >?= i;
    for (int i=1;i<=m;i++)
      t[i] >?= t[i-1];

//     for (int i=1;i<=10;i++)
//       cout<<dyna[i]<<' ';
//     cout<<endl;

    for (int i=1;f*i<=m;i++){
      int money = m-f*i;
      int q = money/i;
      int p = money-i*dyna[t[q]];
      if (p < 0)
	continue;
      int d = dyna[t[q]+1]-dyna[t[q]];
      ans = max(ans,i*t[q]+p/d);
    }
    cout<<"Case #"<<ccount<<": "<<ans<<endl;
  }
}

#undef int
