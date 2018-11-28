// BigInt
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef long long ll;

const ll BASE=1000000000;

class BigInt { public:
	VI v;
	int siz, sig;
  
	// initialization
	BigInt() { v=VI(1,0); siz=sig=1; }
	BigInt(int x) { 
		if (x>=0) sig=1;
		else { sig=-1; x*=-1; }
		v=VI(1,x);
		siz=1;
	}
	BigInt(string s) { str2bi(s); }
  BigInt(const BigInt &b) { *this=b; }
	
	// misc
  void operator=(const BigInt &b) { v=b.v; siz=b.siz; sig=b.sig; }
	int digit(int pos) { if (pos<siz) return v[pos]; return 0; }
  void zero() { v=VI(1,0); siz=sig=1; }
	void resiz(int nsiz, int val=0) { v.resize(siz=nsiz,val); }
	void unzero() {
		int i;
		for (i=siz-1; i>0 && v[i]==0; --i);
		resiz(i+1);
	}
	void str2bi(string s) {
		if (s[0]=='-') { sig=-1; s=s.substr(1); }
		else sig=1;
		reverse(s.begin(),s.end());
		siz=s.size()/9 + 1;
		v=VI(siz,0);
		for (int i=0, pw; i<s.size(); ++i, pw*=10) {
			if (i%9==0) pw=1;
			v[i/9]+=int(s[i]-'0')*pw;
		}
	}
	
	// comparisons
  //0: ==b  +: >b  -: <b
  inline int compabs(const BigInt &b) const {
    if (siz!=b.siz) return siz-b.siz;
    for (int i=siz-1; i>=0; --i) {
      if (v[i]!=b.v[i]) return v[i]-b.v[i];
    }
    return 0;
  }
  // 0: ==b  +: >b  -: <b
  inline int compare(const BigInt &b) const {
    if (sig!=b.sig) return sig-b.sig;
    return sig*compabs(b);
  }
  inline bool operator==(const BigInt &b) const { return !compare(b); }
  inline bool operator!=(const BigInt &b) const { return compare(b); }
  inline bool operator<(const BigInt &b) const { return compare(b)<0; }
  inline bool operator<=(const BigInt &b) const { return compare(b)<=0; }
  inline bool operator>(const BigInt &b) const { return compare(b)>0; }
  inline bool operator>=(const BigInt &b) const { return compare(b)>=0; }
  // |x| < 10^9
  inline bool operator==(int x) { return siz==1 && sig*v[0]==x; }
	
	// operations
	void add(BigInt &b) {
    if (siz<b.siz) resiz(b.siz,0);
    int ca=0;
    for (int i=0; i<siz; ++i) {
      v[i]+=b.digit(i)+ca;
      ca=v[i]/BASE;
      v[i]%=BASE;
    }
    if (ca) resiz(siz+1,ca);
  }
  // assumes that >=b
  void substract(BigInt &b) {
    int ca=0;
    for (int i=0; i<siz; ++i) {
      v[i]+=BASE-b.digit(i)+ca;
      ca=v[i]/BASE-1;
      v[i]%=BASE;
    }
    unzero();
  }
  
	// operators
  // |x| < 10^9
  void operator+=(int x) {
    v[0]+=x;
    for (int i=0; i<siz && v[i]>=BASE; ++i) {
      v[i+1]+=v[i]/BASE;
      v[i]%=BASE;
    }
    if (v[siz-1]>=BASE) {
      resiz(siz+1,v[siz-1]/BASE);
      v[siz-1]%=BASE;
    }
  }
  void operator+=(BigInt &b) {
    if (sig==b.sig) add(b);
    else if (compabs(b)>=0) substract(b);
    else {
      BigInt aux(b);
      aux.substract(*this);
      *this=aux;
    }
  }
	BigInt operator+(BigInt &x) {
		BigInt ret=*this;
		ret+=x;
		return ret;
	}
  // |x| < 10^9
  void operator-=(int x) {
    v[0]-=x;
    for (int i=0; i<siz && v[i]<0; ++i) {
      v[i+1]+=v[i]/BASE - 1;
      v[i]%=BASE;
      v[i]+=BASE;
    }
    unzero();
  }
  void operator-=(BigInt &b) {
    if (&b==this) zero();
    else {
      b.sig*=-1;
      operator+=(b);
      b.sig*=-1;
    }
  }
	BigInt operator-(BigInt &x) {
		BigInt ret=*this;
		ret-=x;
		return ret;
	}
  // |x| < 10^9
  void operator*=(int x) {
    if (x<0) { sig*=-1; x*=-1; }
    resiz(siz+1,0);
    ll ca=0;
    for (int i=0; i<siz; ++i) {
      ca+=ll(v[i])*ll(x);
      v[i]=ca%BASE;
      ca/=BASE;
    }
    unzero();
  }
	void operator*=(BigInt &b) {
		BigInt c;
		c.resiz(siz + b.siz);
		c.sig=sig*b.sig;
		for (int i=0; i<siz; ++i)
			for (int j=0; j<b.siz; ++j) {
				int k=i+j;
				ll z=ll(digit(i))*ll(b.digit(j)) + c.digit(k);
				for (ll y; y = z/BASE;) {
					c.v[k]=z%BASE;
					z=y + c.v[++k];
				}
				c.v[k]=z;
			}
		c.unzero();
		*this=c;
	}
	BigInt operator*(BigInt &x) {
		BigInt ret=*this;
		ret*=x;
		return ret;
	}
	// |x| < 10^9
  void operator/=(int x) {
    if (x<0) { sig*=-1; x*=-1; }
    ll ca=0;
    for (int i=siz-1; i>=0; --i) {
      ca+=v[i];
      v[i]=ca/x;
      ca%=x;
      ca*=BASE;
    }
    unzero();
  }
  void operator/=(BigInt &b){
    if (compabs(b)<0) zero();
    else if (b.siz==1) *this/=b.sig*b.v[0];
    else {
      int st=sig*b.sig,sb=b.sig;
      sig=b.sig=1;
      vector<BigInt> VB,pot2;
      VB.push_back(b);
      pot2.push_back(1);
      BigInt cur=0;
      while (VB[VB.size()-1]<=*this){
        BigInt last=VB[VB.size()-1];
        last+=last;
        VB.push_back(last);
        last=pot2[pot2.size()-1];
        last+=last;
        pot2.push_back(last);
      }
      cur+=pot2[pot2.size()-2];
      (*this)-=VB[VB.size()-2];
      while ((*this)>=b){
        int i=0;
        while (VB[i]<=(*this)) ++i;
        cur+=pot2[i-1];
        (*this)-=VB[i-1];
      }
      (*this)=cur;
      sig=st;
      b.sig=sb;
    }
  }
	BigInt operator/(BigInt &x) {
		BigInt ret=*this;
		ret/=x;
		return ret;
	}
  // |x| < 10^9
  ll mod(int x) {
    if (x<0) x*=-1;
    ll ca=0;
    for (int i=siz-1; i>=0; --i) { ca*=BASE; ca+=v[i]; ca%=x; }
    return ca;
  }
  void operator%=(BigInt &b) {
    BigInt r(*this); r/=b; r*=b; operator-=(r);
  }
  void mcdrec(BigInt &b, BigInt &c) {
    if (c==0) return *this=b;
    b%=c;
    mcdrec(c,b);
  }
  void mcd(BigInt &b, BigInt& c) { BigInt bb(b),cc(c); mcdrec(bb,cc); }
  void powrec(BigInt &aux, ll p) {
    if (!p) return;
    powrec(aux,p/2);
    aux*=aux;
    if (p%2) aux*=(*this);
  }
  void pow(ll p) { BigInt aux(1); powrec(aux,p); *this=aux; }
	
	// input/output
	friend ostream &operator<<(ostream &os, BigInt &x) {
		x.unzero();
		if (x.sig==-1) os << '-';
		int i=x.siz-1;
		os << x.digit(i);
		for (--i; i>=0; --i) {
			os << setw(9) << setfill('0') << x.digit(i);
    }
		return os;
	}
	friend istream &operator >>(istream &is, BigInt &x) {
		string s;
		is >> s;
		x.str2bi(s);
		return is;
	}
};

// return a mod b
BigInt modulo(BigInt a, BigInt b) {
  BigInt c = a/b;
  BigInt d = c*b;
  BigInt e = a-d;
  return e;
}

int main() {
  int C;
  cin >> C;
  for (int ca = 1; C--; ++ca) {
    int n;
    cin >> n;
    vector<BigInt> v(n);
    for (int i = 0; i < n; ++i) {
      cin >> v[i];
    }
    BigInt gcd = v[0]-v[1];
    if (gcd < 0) gcd *= -1;
    for (int i = 0; i < n; ++i) {
      for (int j = i+1; j < n; ++j) {
        BigInt dif = v[i]-v[j];
        if (dif < 0) dif *= -1;
        BigInt tmp = gcd;
        gcd.mcd(tmp, dif);
      }
    }
    BigInt mn = v[0];
    for (int i = 1; i < n; ++i) {
      if (v[i] < mn) mn = v[i];
    }
    BigInt x = modulo(mn, gcd);
    BigInt z = gcd - x;
    BigInt y = modulo(z, gcd);
    cout << "Case #" << ca << ": " << y << endl;
  }
}
