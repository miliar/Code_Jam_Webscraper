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

const int MAX_N = 1000+200;

int n,w,h,r[MAX_N];
Pair num[MAX_N],pl[MAX_N];

template<class a,class b>
pair<a,b> operator + (pair<a,b> x,pair<a,b> y){
  return(pair<a,b>(x.first+y.first,x.second+y.second));
}

template<class a,class b>
pair<a,b> operator - (pair<a,b> x,pair<a,b> y){
  return(pair<a,b>(x.first-y.first,x.second-y.second));
}

const double EPS = 1e-7;

bool ok(int s,Pair t){
//   cout<<"hi "<<s<<' '<<t<<endl;
  if (t.first > w || t.second > h)
    return(false);

  for (int i=1;i<s;i++){
    Pair p = t-pl[num[i].second];
//     cout<<p<<" this is p"<<endl;
    if (sqrt((long long)p.first*p.first+(long long)p.second*p.second) < 
	r[num[i].second]+r[num[s].second]-EPS)
      return(false);
//     else
//       cout<<sqrt((long long)p.first*p.first+(long long)p.second*p.second)<<" next"<<' '<<r[num[i].second]+r[num[s].second]-EPS<<endl;
  }
//   cout<<"here"<<endl;
  return(true);
}

int main(){
  ios_base::sync_with_stdio(false) ;
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    cin>>n>>w>>h;
    for (int i=1;i<=n;i++){
      cin>>num[i].first;
      r[i] = num[i].first;
      num[i].second = i;
    }
    sort(num+1,num+n+1);
    reverse(num+1,num+n+1);
    bool bad = false;
    do{
      bad = false;
      for (int i=1;i<=n;i++){
	if (bad)
	  continue;
	pl[num[i].second] = Pair(0,0);
	if (ok(i,Pair(0,0)))
	  continue;
	pl[num[i].second] = Pair(w+1,w+1);
	for (int j=1;j<i;j++){
// 	  cout<<i<<' '<<j<<' '<<pl[num[j].second]<<endl;
	  if (ok(i,pl[num[j].second]+Pair(r[num[j].second]+r[num[i].second],0)))
	    pl[num[i].second]=min(pl[num[i].second],pl[num[j].second]+Pair(r[num[j].second]+r[num[i].second],0));
	  if (ok(i,pl[num[j].second]+Pair(0,r[num[j].second]+r[num[i].second])))
	    pl[num[i].second]=min(pl[num[i].second],pl[num[j].second]+Pair(0,r[num[j].second]+r[num[i].second]));
	}
	if (pl[num[i].second].first > w)
	  bad = true;
      }
//       cout<<bad<<endl;
//       for (int i=1;i<=n;i++)
// 	cout<<pl[i]<<' ';
//       cout<<endl;
//       bad = false;
      if (bad)
	random_shuffle(num+1,num+n+1);
    }while (bad);
    cout<<"Case #"<<ccount<<": ";
    for (int i=1;i<=n;i++)
      cout<<pl[i].first<<' '<<pl[i].second<<' ';
    cout<<endl;
  }
}
