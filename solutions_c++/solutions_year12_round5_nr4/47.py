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

int e[50][50];

Pair gt(char x){
  Pair res;
  res.first = res.second = x-'a';
  if (x == 'o')
    res.second = 40;

  if (x == 'i')
    res.second = 41;

  if (x == 'e')
    res.second = 42;

  if (x == 'a')
    res.second = 43;

  if (x == 's')
    res.second = 44;

  if (x == 't')
    res.second = 45;

  if (x == 'b')
    res.second = 46;

  if (x == 'g')
    res.second = 47;

  return(res);
}

int next[50],prev[50];

int find(int s,int t){
  int sum = 1;
  for (int i=0;i<50;i++)
    sum+=next[i];

//   cout<<"here "<<sum<<endl;

  for (int i=0;i<50;i++){
    int a = prev[i], b = next[i];
    if (s == i)
      a++;
    if (t == i)
      b++;
    if (a > b)
      sum+=a-b;
   
  }
  return(sum);
}

const int INF = 1000000000000000000ll+10;

#undef int
int main(){
#define int long long
  ios_base::sync_with_stdio(false) ;
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    int k;
    cin>>k;
    string st;
    cin>>st;
    for (int i=0;i<50;i++)
      for (int j=0;j<50;j++)
	e[i][j] = 0;

    for (int i=0;i<50;i++)
      next[i] = prev[i] = 0;

    for (int i=0;i+1<st.size();i++){
      Pair a = gt(st[i]);
      Pair b = gt(st[i+1]);
//       cout<<a<<' '<<b<<endl;
      e[a.first][b.first]++;
      if (a.first != a.second){
	e[a.second][b.first]++;
	if (b.first != b.second)
	  e[a.second][b.second]++;
      }
      if (b.first != b.second)
	e[a.first][b.second]++;
    }

    for (int i=0;i<50;i++)
      for (int j=0;j<50;j++)
	if (e[i][j] && e[i][j] > 1)
	  e[i][j] = 1;

    for (int i=0;i<50;i++)
      for (int j=0;j<50;j++){
	next[i]+=e[i][j];
	prev[j]+=e[i][j];
      }

    int ans = INF;
//     cout<<find(1,2)<<endl;
    for (int i=0;i<50;i++)
      for (int j=0;j<50;j++){
	ans = min(ans,find(i,j));
// 	  if (find(i,j) == 0)
// 	    cout<<i<<' '<<j<<endl;
	}
    cout<<"Case #"<<ccount<<": "<<ans<<endl;
  }
}
