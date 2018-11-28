#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <memory>
#include <cctype>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define FOR( i , a , n ) for (int i = (a); i <= (n) ; i++ )
#define REP( i , n ) for (int i = 0; i < (n) ; i++ )
#define debug(x) cout << #x" = " << x << "\n"
#define FORIT( i , c ) for ( __typeof((c).begin())  i  = (c).begin() ; (i) != (c).end() ; (i)++ )
#include <cstdio>
#include <cmath>
#define MAXD 1000

class bignum{
public:
	int sz;
	int sign;
	int dig[MAXD];
	void set(int v){
		int i;
		for(i=0;i<MAXD;i++) dig[i] = 0;
		sz = 1;
		if(v >= 0){
			dig[0] = v;
			sign = 1;
			}
		else{
			dig[0] = -v;
			sign = -1;
			}
		}
	void set(char *c){
		int i,q,k,v,pw;
		for(i=0;i<MAXD;i++) dig[i] = 0;
		k = strlen(c);
		if(c[0] == '-') sign = -1;
		else sign = 1;
		sz = 0;
		v = 0;
		q = 0;
		pw = 1;
		for(i=k-1;i>=0;i--){
			if(c[i] == '-') break;
			v += pw*(c[i] - '0');
			q++;
			pw *= 10;
			if(q >= 9){
				pw = 1;
				q = 0;
				dig[sz++] = v;
				v = 0;
				}
			}
		dig[sz++] = v;
		this->justify();
		}
	bignum(){
		int i;
		for(i=0;i<MAXD;i++) dig[i] = 0;
		sz = 1;
		sign = 1;
		}
	bignum(int v){
		set(v);
		}
	bignum(char *c){
		set(c);
		}
	void justify(){
		int i;
		for(i=sz-1;i>=0;i--){
			if(dig[i]) break;
			}
		sz = 1+i;
		if(!sz) sz = 1;
		if(sz == 1 && dig[0] == 0) sign = 1;
		}
	void shift(int k){
		int i;
		if(sz == 1 && dig[0] == 0) return ;
		for(i=sz-1;i>=0;i--) dig[i+k] = dig[i];
		for(i=k-1;i>=0;i--) dig[i] = 0;
		sz += k;
		}
	void negate(){
		if(*this == 0) return ;
		this->sign = -this->sign;
		}
	void print(){
		int i;
		if(sign < 0) printf("-");
		printf("%d",dig[sz-1]);
		for(i=sz-2;i>=0;i--) printf("%.9d",dig[i]);
		}
	//<0 se this < b
	int cmp(bignum &b){
		int i;
		if(sign > 0 && b.sign < 0) return 1;
		if(sign < 0 && b.sign > 0) return -1;
		if(sz > b.sz) return sign;
		if(sz < b.sz) return -sign;
		for(i=sz-1;i>=0;i--){
			if(dig[i] > b.dig[i]) return sign;
			if(dig[i] < b.dig[i]) return -sign;
			}
		return 0;
		}
	bool operator<(bignum &b){
		return (cmp(b) < 0);
		}
	bool operator<=(bignum &b){
		return (cmp(b) <= 0);
		}
	bool operator>(bignum &b){
		return (cmp(b) > 0);
		}
	bool operator>=(bignum &b){
		return (cmp(b) >= 0);
		}
	bool operator==(bignum &b){
		return (cmp(b) == 0);
		}
	bool operator==(int v){
		if(this->sz > 1) return false;
		if(v < 0 && sign > 0 || v < 0 && sign > 0) return false;
		return v == dig[0];
		}
	bignum operator+(bignum &b){
		bignum ret;
		int i,c;
		if(sign == b.sign){
			ret.sign = sign;
			}
		else{
			if(sign == -1){
				sign = 1;
				ret = b - *this;
				sign = -1;
				}
			else if(b.sign == -1){
				b.sign = 1;
				ret = *this - b;
				b.sign = -1;
				}
			return ret;
			}
		ret.sz = 1 + max(sz,b.sz);/*no máximo, depois se precisar a
								  gente corrige*/
		c = 0;
		for(i=0;i<ret.sz;i++){
			ret.dig[i] = c + dig[i] + b.dig[i];
			c = 0;
			if(ret.dig[i] >= 1000000000){
				c = 1;
				ret.dig[i] -= 1000000000;
				}
			}
		ret.justify();
		return ret;
		}

	bignum operator-(bignum &b){
		bignum ret;
		int i,k,brw;
		/*se um for negativo, trocamos o sinal de b e somamos*/
		if((sign < 0) || (b.sign < 0)){
			b.sign = -b.sign;
			ret = *this+b;
			b.sign = -b.sign;
			return ret;
			}
		if(*this<b){
			ret = b-*this;
			ret.sign = -1;
			return ret;
			}
		ret.sign = 1;
		ret.sz = max(sz,b.sz);
		brw = 0;
		for(i=0;i<ret.sz;i++){
			k = dig[i] - b.dig[i] - brw;
			if(k < 0){/*emprestando...o borrow vai descontar*/
				k += 1000000000;

				brw = 1;
				}
			else{
				brw = 0;
				}
			ret.dig[i] = k;
			if(ret.dig[i] >= 1000000000) ret.dig[i] -= 1000000000;
			}
		ret.justify();
		return ret;
		}

	bignum operator*(bignum &b){
		bignum ret,buf;
		int i,j,c;
		long long hlp;
		for(i=0;i<b.sz;i++){
			buf.sz = 1+sz;
			c = 0;
			for(j=0;j<buf.sz;j++){
				hlp = ((long long)b.dig[i])*((long long)dig[j])+((long long)c);
				c = (int) (hlp/1000000000);
				buf.dig[j] = (int) (hlp - ((long long)c)*((long
					long)1000000000));
				}
			buf.shift(i);
			ret = ret + buf;
			}
		ret.sign = sign*b.sign;
		ret.justify();
		return ret;
		}
	
	friend bignum operator*(int v,bignum &b){
		return b*v;
		}


	bignum operator*(int v){
		bignum ret;
		int i,c;
		long long hlp;
		ret.sz = 1+sz;
		c = 0;
		for(i=0;i<ret.sz;i++){
			hlp = ((long long) abs(v))*((long long) dig[i])+c;
			c = (int) (hlp/1000000000);
			ret.dig[i] = (int) (hlp - ((long long) c)*((long
				long)1000000000));
			}
		ret.justify();
		return ret;
		}
	
	bignum operator/(bignum &b){
		int as,bs;
		bignum ret,row;
		int i;
		int x,y,z;
		ret.sign = sign*b.sign;
		as = sign;
		bs = b.sign;
		sign = 1;
		b.sign = -1;
		ret.sz = sz;
		for(i=sz-1;i>=0;i--){
			row.shift(1);
			row.dig[0] = dig[i];
			x = 0;
			y = 1000000000-1;
			while(1){
				z = (1+x+y)/2;
				if(x == y) break;
				if(b*z <= row){
					x = z;
					}
				else{
					y = z-1;
					}
				}
			ret.dig[i] = z;
			row = b*z - row;
			row.negate();
			//if(!(row == 0)) row.sign = -row.sign;
			}
		sign = as;
		b.sign = bs;
		ret.justify();
		return ret;
		}
	};

bignum t[1005];
bignum T,N,y;

bignum big_mdc(bignum a, bignum b){
	if(a<b) return big_mdc(b,a);
	if(a==b) return a;
	if(b==0) return a;
	return big_mdc(b,a-(a/b)*b);
	}

void doProblemB(){
	int C;
	cin>>C;
	for(int tcase = 1 ; tcase<= C; tcase++){
		cout<<"Case #"<<tcase <<": ";
		int n;
		cin>>n;
		N.set("0");
		REP(i,n)
			{
			string s;
			cin>>s;
			t[i].set((char*)s.c_str());
			if(t[i]>N)
				N=t[i];
			}
		REP(i,n)
			t[i]=N-t[i];
		T=t[0];
		REP(i,n-1)
		 T=big_mdc(T,t[i+1]);
		y = T - (N - (N/T)*T);
		if(y==T)
			y=0;
		y.print();
		cout<<"\n";

		
		
		}




	}




int main() {
	doProblemB();
	return 0;
	}
