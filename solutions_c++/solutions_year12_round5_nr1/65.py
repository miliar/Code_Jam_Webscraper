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

const int MAX_N = 1000+20;

int l[MAX_N],p[MAX_N];

const double EPS = 1e-7;

double e(int s,double before){
  double p = ((double)::p[s])/100;
  double l = ::l[s];
  // result = l+(1-p)*(before+result);
  // result*(1-(1-p)) = l+(1-p)*before
  double result = ((l+(1-p)*before)/(1-(1-p)));
//   cout<<result<<' '<<l+(1-p)*(before+result)<<" here "<<endl;
  return(result);
}

double cal(int first,int second){
  double res = e(first,0);
  return(res+e(second,res));
}

bool df(int s,int t){
  double x = cal(s,t);
  double y = cal(t,s);
  if (abs(x-y) < EPS)
    return(s < t);
  else
    return(x < y);
}

int main(){
  ios_base::sync_with_stdio(false) ;
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    int n;
    cin>>n;
    for (int i=1;i<=n;i++)
      cin>>l[i];
    for (int i=1;i<=n;i++){
      cin>>p[i];
      p[i] = 100-p[i];
    }
//     cout<<"hi "<<e(1,0)<<' '<<e(2,0)<<endl;

//     cout<<cal(1,2)<<endl;
//     cout<<cal(2,1)<<endl;

    vector<int> sorted;
    for (int i=1;i<=n;i++)
      sorted.push_back(i);
    sort(sorted.begin(),sorted.end(),df);
    cout<<"Case #"<<ccount<<": ";
    for (int i=0;i<sorted.size();i++)
      cout<<sorted[i]-1<<' ';
    cout<<endl;
  }
}
