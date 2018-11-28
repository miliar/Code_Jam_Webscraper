#include <iostream>
#include <ctime>

#include <vector>
#include <sstream>
#include <iomanip>

using namespace std;

class integer{
  friend istream& operator>>(istream&,integer&);
  friend ostream& operator<<(ostream&,const integer&);
public:
  integer(int=0);
  integer operator-(const integer&)const;

  bool operator<(const integer&)const;
  bool operator==(const integer& a)const{ return v==a.v; }
  bool operator!=(const integer& a)const{ return v!=a.v; }

  integer operator%(const integer&)const;

  operator bool()const;
  integer operator*(const integer&)const;
  integer operator+(const integer&)const;
private:
  static const int base=1000000000,log=9;
  integer& operator-=(const integer&);
  integer operator/(const integer&)const;
  void normalize();
  vector<int> v;
  int digit(int)const;
  integer& mult10(int);
  integer front(int)const;
  integer last(int)const;
  integer& div2();
};

int get_int(const string& s,int start,int end){
  int ret=0;
  for(int i=0;i<end;i++)
    ret=10*ret+s[start+i]-'0';
  return ret;
}

istream& operator>>(istream& in,integer& n){
  string s;
  in>>s;
  int t=(s.size()+integer::log-1)/integer::log;
  n.v=vector<int>(t);
  for(int i=0;i<t;i++){
    int start=s.size()-integer::log*(i+1);
    int end=integer::log;
    if(i+1==t){
      start=0;
      end=s.size()-(t-1)*integer::log;
    }
    n.v[t-1-i]=get_int(s,start,end);
  }
  return in;
}

ostream& operator<<(ostream& out,const integer& n){
  out<<n.v[0];
  out.fill('0');
  for(int i=1;i<n.v.size();i++)
    cout<<setw(integer::log)<<n.v[i];
  return out;
}

bool integer::operator<(const integer& a)const{
  if(v.size()!=a.v.size())
    return v.size()<a.v.size();
  for(int i=0;i<v.size();i++)
    if(v[i]!=a.v[i])
      return v[i]<a.v[i];
  return false;
}

integer::operator bool()const{
  return v.size()>1 || v[0]!=0;
}

integer integer::operator-(const integer& a)const{
  if(*this<a){
    integer b=a;
    return b-=*this;
  }
  integer b=*this;
  return b-=a;
}

integer& integer::operator-=(const integer& a){
  int carry=0;
  for(int i=0;i<v.size();i++){
    int sn=digit(i);
    int an=a.digit(i);
    an+=carry;
    carry=0;
    int rn=sn-an;
    if(rn<0){
      rn+=base;
      carry=1;
    }
    v[v.size()-1-i]=rn;
  }
  assert(carry==0);
  normalize();
  return *this;
}

void integer::normalize(){
  int k=0;
  while(k+1<v.size() && v[k]==0) k++;
  if(k) v.erase(v.begin(),v.begin()+k);
}

integer integer::operator%(const integer& a)const{
  assert(a);
  integer b=*this/a*a;
  return *this-b;
}

integer integer::operator/(const integer& d)const{
  integer low,high=*this;
  integer one=1;
  while(low<high){
    integer guess=(low+high+one).div2();
    integer m=guess*d;
    if(m==*this){
      return guess;
    }
    if(*this<m)
      high=guess-one;
    else
      low=guess;
  }
  return low;
}

integer integer::operator+(const integer& a)const{
  integer r;
  size_t m=max(a.v.size(),v.size())+1;
  r.v=vector<int>(m);
  int carry=0;
  for(int i=0;i<m;i++){
    int sn=digit(i);
    int an=a.digit(i);
    int rn=carry+an+sn;
    carry=rn/base;
    rn%=base;
    r.v[r.v.size()-1-i]=rn;
  }
  r.normalize();
  return r;
}

int integer::digit(int n)const{
  return n<v.size()?v[v.size()-1-n]:0;
}

integer& integer::div2(){
  for(int i=0;i<v.size();i++){
    int sn=digit(i);
    if(sn&1)
      v[v.size()-i]+=base/2;
    v[v.size()-1-i]=sn/2;
  }
  normalize();
  return *this;
}

integer integer::operator*(const integer& a)const{
  int m=max(a.v.size(),v.size());
  if(m==1){
    integer ret;
    ret.v=vector<int>(2);
    long long r=static_cast<long long>(digit(0))*a.digit(0);
    ret.v[0]=r/base;
    ret.v[1]=r%base;
    ret.normalize();
    return ret;
  }
  m/=2;
  integer af=a.front(m),al=a.last(m);
  integer bf=front(m),bl=last(m);

  integer total=(af+al)*(bf+bl);
  integer fronts=af*bf;
  integer lasts=al*bl;
  integer middles=total-fronts-lasts;
  integer ret=lasts+middles.mult10(m)+fronts.mult10(2*m);
  return ret;
}

integer& integer::mult10(int m){
  v.resize(v.size()+m);
  return *this;
}

integer integer::front(int m)const{
  integer ret;
  if(v.size()<=m)
    ret=0;
  else
    ret.v=vector<int>(v.begin(),v.begin()+(v.size()-m));
  return ret;
}

integer integer::last(int m)const{
  integer ret;
  if(v.size()<=m)
    ret=*this;
  else
    ret.v=vector<int>(v.begin()+(v.size()-m),v.end());
  return ret;
}

integer::integer(int n):v(vector<int>(1,n)){
}

integer answer();

int main(){
  clock_t c=clock();
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<answer()<<'\n';
  clock_t cc=clock();
  cerr<<cc-c<<'\n';
}

integer gcd(integer a,integer b);

integer answer(){
  int n;
  integer now,last;
  cin>>n>>last>>now;
  integer ret=last-now;
  integer m=max(last,now);
  for(int i=2;i<n;i++){
    last=now;
    cin>>now;
    ret=gcd(ret,last-now);
    m=max(m,now);
  }
  return (ret-m%ret)%ret;
}

integer gcd(integer a,integer b){
  if(b) return gcd(b,a%b);
  return a;
}
