#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <assert.h>
#include <algorithm>
#include <math.h>
#include <bitset>
#include <ctime>
#include <sys/time.h>

using namespace std;

const long long BASE=100000000;

class BigNum {
	public:
	vector <long long> A;
	vector <BigNum> POW2;
	void clear(void) {
		while (A.size()>1 && A[A.size()-1]==0) A.pop_back();
		}
	BigNum & operator = (const BigNum &rhs) {
		A=rhs.A;
		return *this;
		}
	BigNum & operator = (const long long &rhs) {
		A.resize(1);
		A[0]=rhs;
		return *this;
		}
	BigNum & operator = (const int &rhs) {
		A.resize(1);
		A[0]=rhs;
		return *this;
		}
	BigNum & operator = (string rhs) {
		A.resize(1);
		A[0]=0;
		BigNum D, DIECI;
		D=1;
		DIECI=10;
		for (int i=rhs.size()-1; i>=0; i--) {
			for (char j='0'; j<rhs[i]; j++) *this+=D;
			D*=DIECI;
			}
		return *this;
		}
	BigNum & operator += (const BigNum &rhs) {
		while (A.size()<=rhs.A.size()) A.push_back(0);
		A.push_back(0);
		for (int i=0; i<rhs.A.size(); i++) A[i]+=rhs.A[i];
		long long carry=0;
		for (int i=0; i<A.size(); i++) {
			carry+=A[i];
			A[i]=carry%BASE;
			carry/=BASE;
			}
		assert(carry==0);
		clear();
		return *this;
		}
	BigNum operator + (const BigNum &rhs) {
		BigNum RES=*this;
		RES+=rhs;
		return RES;
		}
	BigNum & operator -= (const BigNum &rhs) {
		while (A.size()<=rhs.A.size()) A.push_back(0);
		for (int i=0; i<rhs.A.size(); i++) A[i]-=rhs.A[i];
		long long carry=0;
		for (int i=0; i<A.size(); i++) {
			carry+=A[i];
			while (carry<0) {
				assert(i+1<A.size());
				A[i+1]--;
				carry+=BASE;
				}
			A[i]=carry%BASE;
			carry/=BASE;
			}
		clear();
		return *this;
		}
	BigNum operator - (const BigNum &rhs) {
		BigNum RES=*this;
		RES-=rhs;
		return RES;
		}
	BigNum & operator *= (const BigNum &rhs) {
		vector <long long> B(A.size()+rhs.A.size()+1, 0);
		for (int i=0; i<A.size(); i++) for (int j=0; j<rhs.A.size(); j++) B[i+j]+=A[i]*rhs.A[j];
		
		A=B;
		
		long long carry=0;
		for (int i=0; i<A.size(); i++) {
			carry+=A[i];
			A[i]=carry%BASE;
			carry/=BASE;
			}
		clear();
		return *this;
		}
	BigNum operator * (const BigNum &rhs) {
		BigNum RES=*this;
		RES*=rhs;
		return RES;
		}
	bool operator < (const BigNum &rhs) const {
		if (A.size()!=rhs.A.size()) return (A.size()<rhs.A.size());
		for (int i=A.size()-1; i>=0; i--) if (A[i]!=rhs.A[i]) return (A[i]<rhs.A[i]);
		return false;
		}
	bool operator <= (const BigNum &rhs) {
		if (A.size()!=rhs.A.size()) return (A.size()<rhs.A.size());
		for (int i=A.size()-1; i>=0; i--) if (A[i]!=rhs.A[i]) return (A[i]<rhs.A[i]);
		return true;
		}
	bool operator == (const BigNum &rhs) {
		if (A.size()!=rhs.A.size()) return false;
		for (int i=A.size()-1; i>=0; i--) if (A[i]!=rhs.A[i]) return false;
		return true;
		}
	BigNum & operator /= (const BigNum &rhs) {	
		BigNum NUM=*this;

		if (POW2.size()<1) {
			POW2.resize(1);
			POW2[0]=(long long)1;
			}
		while (POW2[POW2.size()-1]<=NUM)	POW2.push_back(POW2[POW2.size()-1]+POW2[POW2.size()-1]);
		
		
		BigNum RES;
		RES=0;
		
		for (int i=POW2.size()-1; i>=0; i--) {
			BigNum med=RES+POW2[i];
			if (med*rhs<=NUM) RES=med;
			}
		*this=RES;
		return *this;
		}
	BigNum operator / (const BigNum &rhs) {
		BigNum RES=*this;
		RES/=rhs;
		return RES;
		}
	BigNum & operator %= (const BigNum &rhs) {
		BigNum NUM=*this;
		*this=NUM-((NUM/rhs)*rhs);
		return *this;
		}
	BigNum operator % (const BigNum &rhs) {
		BigNum RES=*this;
		RES%=rhs;
		return RES;
		}
	bool isZero(void) {
		if (A.size()>1) return false;
		return (A[0]==0);
		}
	void stampa(void) const {
		for (int i=A.size()-1; i>=0; i--) cout<<A[i]<<"\t";
		cout<<"\n";
		}
	string ToString(void) {
		if (isZero()) return "0";
		string RES="";
		BigNum A,B,C,D=*this;
		A=1, B=10;
		while (A<=D) {
			C=(*this)/A;
			C=(D/A)%B;
			RES=' '+RES;
			RES[0]='0'+C.A[0];
			A*=B;
			}
		return RES;
		}
	};

BigNum gcd(BigNum a, BigNum b) {
	if (b.isZero()) return a;
	return gcd(b, a%b);
	}

int main (void) {
	fstream IN("B2.in", ios::in);
	fstream OUT("B2.out", ios::out);
	
	int NUM_TEST;
	IN>>NUM_TEST;
		
	for (int test=1; test<=NUM_TEST; test++) {
		int N;
		IN>>N;
		vector <BigNum> V(N);
		for (int i=0; i<N; i++) {
			string S;
			IN>>S;
			V[i]=S;
			}

		sort(V.begin(), V.end());
		
		BigNum GCD=V[1]-V[0];
		for (int i=2; i<V.size(); i++) GCD=gcd(GCD, V[i]-V[i-1]);
		
		OUT<<"Case #"<<test<<": "<<((GCD-V[0]%GCD)%GCD).ToString()<<"\n";
		}
	return 0;	
	}

