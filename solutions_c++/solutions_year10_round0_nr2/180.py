#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

typedef unsigned long long digit;

#define MAX_DIGIT 1000000000
#define MAX_LENGTH 9 // MAX_DIGIT=10^MAX_LENGTH

class BigNum {
  vector<digit> data;

  void shrink() {
    while (data.size()>1 && !data[data.size()-1])
      data.resize(data.size()-1);
  }

  public:
    BigNum(digit i=0) { 
      data.resize(1,i%MAX_DIGIT); 
      i/=MAX_DIGIT;
      while (i) {
        data.resize(data.size()+1);
        data.back()=i%MAX_DIGIT;
        i/=MAX_DIGIT;
      }
    }

    explicit BigNum(const char *t) {
      int n=0,i,j,k;
      while (t[n])
        n++;
      for (i=n-1; i>=0; i-=MAX_LENGTH) {
        k=0;
        for (j=MAX_LENGTH-1; j>=0; j--)
          if (i-j>=0)
            k=10*k+t[i-j]-'0';
        data.push_back(k);
      }
      shrink();
    }

    BigNum &operator--() {
      int i=0;
      while (!data[i]) {
        data[i]=MAX_DIGIT-1;
        i++;
      }
      data[i]--;
      return *this;
    }

    BigNum &operator++() {
      int i=0;
      while (data[i]+1==MAX_DIGIT) {
        data[i]=0;
        i++;
      }
      data[i]++;
      return *this;
    }

    BigNum &operator+=(const BigNum &a) {
      digit i=0,p=0;
      while (p || i<data.size() || i<a.data.size()) {
        if (i<data.size())
          p+=data[i];
        if (i<a.data.size())
          p+=a.data[i];
        if (i>=data.size())
          data.resize(i+1);
        if (p>=MAX_DIGIT) {
          data[i]=p-MAX_DIGIT;
          p=1;
        }
        else {
          data[i]=p;
          p=0;
        }
        i++;
      }
      return *this;
    }

    BigNum &operator-=(const BigNum &a) {
      digit p=0;
      for (int i=0; i<data.size() || p; i++) {
        if (i<a.data.size())
          p+=a.data[i];
        if (p<=data[i]) {
          data[i]-=p;
          p=0;
        }
        else {
          data[i]+=MAX_DIGIT-p;
          p=1;
        }
      }
      shrink();
      return *this;
    }

    BigNum operator+(BigNum a) {
      BigNum r=*this;
      
      r+=a;
      return r;
    }

    BigNum operator-(BigNum a) {
      BigNum r=*this;
      
      r-=a;
      return r;
    }

    digit operator%(digit d) {
      digit p=0;
      for (int i=data.size()-1; i>=0; i--)
        p=(p*MAX_DIGIT+data[i])%d;
      return p;
    }

    BigNum operator*(const BigNum &a) {
      BigNum r;
      for (int i=0; i<data.size(); i++) {
        BigNum t=a;
        t*=data[i];
        t.data.resize(t.data.size()+i);
        for (int j=t.data.size()-i-1; j>=0; j--)
          t.data[j+i]=t.data[j];
        for (int j=0; j<i; j++)
          t.data[j]=0;
        r+=t;
      }
      r.shrink();
      return r;
    }

    BigNum operator/(BigNum a) {
      BigNum ans,t=*this,power=1,ta=a;

      while (ta<t) {
        power*=10;
        ta*=10;
      }
      while (!power.zero()) {
        while (ta<t || ta==t) {
          ans+=power;
          t-=ta;
        }
        power/=10;
        ta/=10;
      }
      return ans;
    }

    BigNum operator%(BigNum a) {
      return *this-(*this/a)*a;
    }

    BigNum &operator*=(digit m) {
      digit p=0;
      for (int i=0; p || i<data.size(); i++) {
        if (i<data.size())
          p+=m*data[i];
        if (i>=data.size())
          data.resize(i+1);
        data[i]=p%MAX_DIGIT;
        p/=MAX_DIGIT;
      }
      return *this;
    }

    BigNum &operator/=(digit d) {
      digit p=0;
      for (int i=data.size()-1; i>=0; i--) {
        p=p*MAX_DIGIT+data[i];
        data[i]=p/d;
        p%=d;
      }
      shrink();
      return *this;
    }

    bool operator==(const BigNum &x) const {
      if (data.size()!=x.data.size())
        return false;
      int i=0;
      while (i<data.size() && data[i]==x.data[i])
        i++;
      return i==data.size();
    }

    bool operator<(const BigNum &x) const {
      if (x.data.size()!=data.size())
        return data.size()<x.data.size();
      int i=data.size()-1;
      while (i>=0 && data[i]==x.data[i])
        i--;
      return i>=0 && data[i]<x.data[i];
    }

    bool zero() {
      return data.size()==1 && !data[0];
    }

    friend ostream &operator<<(ostream &out,const BigNum &a) {
      out<<a.data[a.data.size()-1];
      for (int i=a.data.size()-2; i>=0; i--) {
        digit j=a.data[i]+!a.data[i];    
        while (j<MAX_DIGIT/10) {
          out<<0;
          j=j*10;
        }
       out<<a.data[i];
      }
      return out;
    }
};

struct euclid_result {
  BigNum alfa,beta,d;
  bool beta_negative;
  euclid_result(BigNum _alfa,BigNum _beta,BigNum _d,bool _beta_negative) {
    alfa=_alfa; beta=_beta; d=_d; beta_negative=_beta_negative;
  }
};

euclid_result extended_euclid(BigNum a,BigNum b) {
  if (b.zero())
    return euclid_result(1,0,a,true);
  euclid_result r=extended_euclid(b,a%b);
  // d=alfa*b+a%b*beta=a*beta+(-a/b+alfa)*b
  return euclid_result(r.beta,r.alfa+(a/b)*r.beta,r.d,!r.beta_negative);
}

BigNum inverse(BigNum a,BigNum m) {
  euclid_result r=extended_euclid(a,m);
  if (r.beta_negative)
    return r.alfa%m;
  else {
    return (m-r.alfa%m)%m;
  }
}

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

main(){
  int C;cin>>C;
  for(int c=1;c<=C;c++){
    int n;
    vector<BigNum> t;
    cin>>n;
    FOR(i,n){
      string s;
      cin>>s;
      t.push_back(BigNum(s.c_str()));
    }
    sort(t.begin(),t.end());
    t.erase(unique(t.begin(),t.end()),t.end());
    BigNum d=t.back()-t[0];
    for(int i=1;i+1<t.size();i++)d=extended_euclid(d,t.back()-t[i]).d;
    BigNum r=0;
    if(!(t.back()%d).zero())r=d-t.back()%d;
    cout<<"Case #"<<c<<": "<<r<<endl;
  }
}
