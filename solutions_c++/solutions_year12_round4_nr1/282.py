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

const int MAX_N = 10000+200;
const int INF = 1000000001;

Pair num[MAX_N];
int dyna[MAX_N],n,D;

bool cal(int who,int t){
  if (num[who].first+t >= D)
    return(true);

  for (int i=who+1;i<=n && num[i].first <= num[who].first+t;i++)
    if (dyna[i] <= num[i].first-num[who].first)
      return(true);
  return(false);
}

int main(){
  ios_base::sync_with_stdio(false) ;
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    cin>>n;
    for (int i=1;i<=n;i++)
      cin>>num[i].first>>num[i].second;
    cin>>D;

    for (int i=n;i>=1;i--){
      int a = 0,b = num[i].second+1;
      while (a < b){
	int temp = (a+b)/2;
	if (cal(i,temp))
	  b = temp;
	else
	  a = temp+1;
      }
      if (a == num[i].second+1)
	a = INF;
      dyna[i] = a;
    }
//     for (int i=1;i<=n;i++)
//       cout<<dyna[i]<<' ';
//     cout<<endl;
    if (dyna[1] <= min(num[1].second,num[1].first))
      cout<<"Case #"<<ccount<<": "<<"YES"<<endl;
    else
      cout<<"Case #"<<ccount<<": "<<"NO"<<endl;
  }
}
