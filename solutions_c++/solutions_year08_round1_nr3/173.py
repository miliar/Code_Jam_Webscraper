#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <iomanip>
#include <cctype>
#include <cassert>

class N{
private:
  std::vector<int> digits;
  static const int base_log=9;
  static const int base=1000000000;
  friend std::ostream& operator<<(std::ostream&,const N&);
  friend std::istream& operator>>(std::istream&,N&);
  N& shift(int);
  N mult(int) const;

  friend const N operator*(const N&,const N&);
  friend const N operator/(const N&,const N&);
  friend bool operator==(const N&,const N&);
  friend bool operator<(const N&,const N&);
public:
  void half();
  N(int=0);
  N& operator+=(const N&);
  N& operator-=(const N&);
  N& operator*=(const N&);
};

const N operator+(const N&,const N&);
const N operator-(const N&,const N&);
N& operator/=(N&,const N&);
const N operator%(const N&,const N&);
bool operator!=(const N& a,const N& b){ return !(a==b); }
bool operator<=(const N& a,const N& b){ return a<b || a==b; }
bool operator>(const N& a,const N& b){ return !(a<=b); }
bool operator>=(const N& a,const N& b){ return !(a<b); }

N::N(int d):digits(1,d){
  if(d>=base){
    digits.push_back(d/base);
    digits[0]%=base;
  }
}

const N operator+(const N& a,const N& b){
  N ret(a);
  return ret+=b;
}

const N operator-(const N& a,const N& b){
  N ret(a);
  return ret-=b;
}

N& operator/=(N& a,const N& b){
  return a=(a/b);
}

const N operator%(const N& a,const N& b){
  return a-(a/b)*b;
}

const N operator/(const N& a,const N& b){
  N low(0),high(a);
  while(low<high){
    N guess=(low+high+1);
    guess.half();
    N prod=guess*b;
    //std::cout<<"  low: "<< low <<"\t high: "<< high << "\t guess: "<< guess <<"\n";
    if(prod==a) return guess;
    if(prod>a)
      high=guess-1;
    else
      low=guess;
  }
  return low;
}

N& N::operator+=(const N& n){
  if(digits.size()<n.digits.size())
    digits.resize(n.digits.size());
  int carry=0,d=0;
  for(;d<n.digits.size();d++){
    digits[d]+=n.digits[d]+carry;
    if(carry= digits[d]>=base)
      digits[d]-=base;
  }
  while(d<digits.size() && carry){
    digits[d]+=carry;
    carry= digits[d]>=base;
    if(carry= digits[d]>=base)
      digits[d]-=base;
  }
  if(d==digits.size() && carry)
    digits.push_back(carry);
  return *this;
}

N& N::operator-=(const N& n){
  //std::cout<<"doing:\n"<<*this<<" -\n "<<n<<'\n';
  assert(*this >= n);
  bool carry=false;
  for(int d=0;d<n.digits.size();d++){
    int n_digit= d<n.digits.size() ? n.digits[d] : 0;
    if(carry) n_digit++;
    carry= (n_digit > digits[d]);
    if(carry)
      digits[d]-= n_digit-base;
    else
      digits[d]-=n_digit;
  }
  if(carry){
    int d=n.digits.size();
    while(digits[d]=='0')
      digits[d++]='9';
    digits[d]--;
  }
  while(digits.size()>1 && digits.back()==0)
    digits.pop_back();
  //std::cout<<"result: "<<*this<<'\n';
  return *this;
}

N& N::operator*=(const N& n){
  return *this= *this* n;
}

const N operator*(const N& a,const N& b){
  N ret=0;
  for(int i=0;i<a.digits.size();i++){
    ret+=b.mult(a.digits[i]).shift(i);
  }
  return ret;
}

const N operator/(const N&,const N&);

bool operator==(const N& a,const N& b){
  return a.digits==b.digits;
}

bool operator<(const N& a,const N& b){
  if(a.digits.size()!=b.digits.size())
    return a.digits.size()<b.digits.size();
  for(int i=a.digits.size()-1;i>=0;i--)
    if(a.digits[i]!=b.digits[i])
      return a.digits[i]<b.digits[i];
  return false;
}

std::ostream& operator<<(std::ostream& out,const N& n){
  out<<n.digits.back();
  char old=out.fill('0');
  int d=static_cast<int>(n.digits.size())-2;
  while(d>=0)
    out<<std::setw(N::base_log)<<n.digits[d--];
  out.fill(old);
  return out;
}

std::istream& operator>>(std::istream& in,N& n){
  std::string s;
  while(std::isspace(in.peek()))
    in.get();
  while(std::isdigit(in.peek()))
    s+=static_cast<char>(in.get());
  if(s.empty()){
    in.setstate(in.rdstate()|std::istream::failbit);
    return in;
  }
  std::vector<int> digits;
  int carry=0,power=1;
  for(int i=s.size()-1;i>=0;i--){
    carry+=power*(s[i]-'0');
    power*=10;
    if(power==N::base){
      digits.push_back(carry);
      power=1;
      carry=0;
    }
  }
  if(digits.size()==0 || carry)
    digits.push_back(carry);
  while(digits.size()>1 && digits.back()==0)
    digits.pop_back();
  n.digits=digits;
  return in;
}

N& N::shift(int n){
  assert(n>=0);
  if(digits.size()==1 && digits[0]==0 || n==0)
    return *this;
  digits.resize(digits.size()+n);
  for(int i=digits.size()-1;i>=n;i--)
    digits[i]=digits[i-n];
  for(int i=0;i<n;i++)
    digits[i]=0;
  return *this;
}

void N::half(){
  for(int i=0;i<digits.size();i++){
    if(i && (digits[i]&1))
      digits[i-1]+=base/2;
    digits[i]/=2;
  }
  while(digits.size()>1 && digits.back()==0)
    digits.pop_back();
}

N N::mult(int p) const{
  N ret;
  if(p==0)
    return ret;
  ret.digits.resize(digits.size());
  int carry=0;
  long long pp=p;
  for(int i=0;i<digits.size();i++){
    long long next=digits[i]*pp+carry;
    carry=next/base;
    ret.digits[i]=next%base;
  }
  if(carry)
    ret.digits.push_back(carry);
  return ret;
}


using namespace std;

string solve();
N root_five();
N sq_five,power_ten=1;
const int Q=100;

int main(){
  for(int i=0;i<Q;i++)
    power_ten*=10;
  sq_five=root_five();
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    cout<<"Case #"<<i+1<<": ";
    cout<<solve();
    cout<<'\n';
  }
}

vector<vector<N> > power(const vector<vector<N> >& m,int p);
vector<vector<N> > mult(const vector<vector<N> >& a,const vector<vector<N> >& b);

N root(const N& n){
  N low=1,high=n;
  while(low<high){
    N guess=(low+high);
    guess.half();
    N square=guess*guess;
    if(square==n)
      return guess;
    if(square<n)
      low=guess+1;
    else
      high=guess-1;
  }
  return low;
}

N root_five(){
  N five=5;
  five*=power_ten*power_ten;
  return root(five);
}

string solve(){
  vector<vector<N> > m(2,vector<N>(2));
  m[0][0]= 3; m[0][1]=5;
  m[1][0]= 1; m[1][1]=3;

  int n;
  cin>>n;
  long double x=3+sqrt((long double)5);
  m=power(m,n);
  N a=m[0][0],b=m[1][0];
  N answer=a*power_ten+b*sq_five;
  ostringstream sout;
  sout<<answer;
  string s=sout.str();
  s=s.substr(0,s.size()-Q);
  while(s.size()<3)
    s="0"+s;
  return s.substr(s.size()-3,3);
}

N add(const N& a,const N& b){
  return a+b;
}

N mult(const N&a,const N& b){
  return a*b;
}

vector<vector<N> > mult(const vector<vector<N> >& a,const vector<vector<N> >& b){
  vector<vector<N> > ret(2,vector<N>(2));
  for(int i=0;i<2;i++)
    for(int j=0;j<2;j++)
      for(int k=0;k<2;k++)
        ret[k][j]=add(ret[k][j],mult(a[k][i],b[i][j]));
  return ret;
}

vector<vector<N> > power(const vector<vector<N> >& m,int p){
  if(p==0){
    vector<vector<N> > ret(2,vector<N>(2));
    ret[0][0]=ret[1][1]=1;
    return ret;
  }
  if(p==1)
    return m;
  vector<vector<N> > ret=power(m,p/2);
  ret=mult(ret,ret);
  if(p&1)
    ret=mult(ret,m);
  return ret;
}
