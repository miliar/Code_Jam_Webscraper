#include<stdio.h>

#define MAXD 100
#define BASE 10

class Bignum
{
public:
       int digit[MAXD],digits; bool sign;
       Bignum() {for (int i=0;i<MAXD;i++) digit[i]=0;digits=1;digit[0]=0;sign=0;}
       Bignum(int x) {
               for (int i=0;i<MAXD;i++) digit[i]=0;
               sign=0;
               if(x<0){sign=1;x=-x;}
               if (x==0) {digits=1; digit[0]=0;}
               else {
                       digits=0;
                       while (x!=0) {
                               digit[digits]=x%BASE;
                               digits++; x/=BASE;
                       }
               }
       }
       Bignum abs() {Bignum tmp=*this;tmp.sign = 0;return tmp;}
       Bignum div2()
       {
               Bignum tmp=*this;
               int i;
               for(i=tmp.digits-1;i>0;i--){tmp.digit[i-1]+=(tmp.digit[i]&1?BASE:0);tmp.digit[i]>>=1;}
               tmp.digit[0]>>=1;
               if(tmp.digit[tmp.digits-1]==0)tmp.digits--;
               return tmp;
       }
       bool operator == (Bignum right) {
               if(sign!=right.sign) return false;
               if(digits!=right.digits) return false;
               int i;
               for(i=digits-1;i>=0;i--) if(digit[i]!=right.digit[i]) return false;
               return true;
       }
       bool operator < (Bignum right) {
               if(sign!=right.sign) return sign;
               if(digits!=right.digits) return (digits<right.digits)!=sign;
               int i;
               for(i=digits-1;i>=0;i--) if(digit[i]!=right.digit[i]) return
(digit[i]<right.digit[i])!=sign;
               return false;
       }
       bool operator > (Bignum right) {return !(*this < right) && !(*this == right);}
       bool operator >= (Bignum right) {return !(*this < right);}
       bool operator <= (Bignum right) {return !(*this > right);}
       bool operator != (Bignum right) {return !(*this == right);}
       void operator *= (Bignum right) {
               int i,j;
               sign^=right.sign;
               if(digits==1&&digit[0]==0) return;
               if(right.digits==1&&right.digit[0]==0) { digits=1;
for(i=0;i<MAXD;i++)digit[i]=0; return;}
               digits+=right.digits-1;
               for (i=digits-1;i>=0;i--) {
                       digit[i]*=right.digit[0];
                       for (j=0;j<i;j++)
                               digit[i]+=right.digit[i-j]*digit[j];
               }
               for (i=0;i<digits-1;i++) {if (digit[i]>=BASE)
{digit[i+1]+=digit[i]/BASE; digit[i]%=BASE;}}
               while (digit[digits-1]>=BASE) {digit[digits]+=digit[digits-1]/BASE;
digit[digits-1]%=BASE; digits++;}
       }
       void operator += (Bignum right) {
               int i;
               bool ds;
               if(sign==right.sign) {
                       if (right.digits>digits) digits=right.digits;
                       for (i=0;i<right.digits;i++) digit[i]+=right.digit[i];
                       for (i=0;i<digits-1;i++) {if (digit[i]>=BASE) {digit[i]-=BASE;
digit[i+1]++;}}
               }
               else {
                       ds = sign;
                       right.sign = sign = 0;
                       if(*this>=right)
                       {
                               for (i=0;i<right.digits;i++) digit[i]-=right.digit[i];
                               for (i=0;i<digits-1;i++) {if (digit[i]<0) {digit[i]+=BASE; digit[i+1]--;}}
                               sign = ds;
                       }
                       else
                       {
                               for (i=0;i<digits;i++) digit[i]=right.digit[i]-digit[i];
                               digits = right.digits;
                               for (i=0;i<digits-1;i++) {if (digit[i]<0) {digit[i]+=BASE; digit[i+1]--;}}
                               sign = !ds;
                       }
               }
               if (digit[digits-1]>=BASE) {digit[digits-1]-=BASE; digit[digits]=1; digits++;}
               while (digits>1 && digit[digits-1]==0) {digits--;}
       }
       void operator -= (Bignum right) {right.sign^=1;*this+=right;}
       void operator = (Bignum right) {
               int i;
               for (i=0;i<MAXD;i++) digit[i]=0;
               digits=right.digits;
               for (i=0;i<digits;i++) digit[i]=right.digit[i];
               sign=right.sign;
       }
       Bignum operator + (Bignum right) {Bignum tmp=*this;tmp+=right;return tmp;}
       Bignum operator - (Bignum right) {Bignum tmp=*this;tmp-=right;return tmp;}
       Bignum operator * (Bignum right) {Bignum tmp=*this;tmp*=right;return tmp;}
       Bignum operator / (Bignum right) {
               Bignum absthis=*this;
               absthis.sign=0;
               Bignum st=1, en=absthis, mid, mxr;
               while(st<=en) {
                       mid=(st+en).div2();
                       mxr=mid*right;
                       mxr.sign=0;
                       if(mxr==absthis) break;
                       else if(mxr<absthis) st=mid+1;
                       else en=mid-1;
               }
               if(mxr>absthis) mid-=1;
               if(sign!=right.sign) mid.sign=1;
               return mid;
       }
       Bignum operator % (Bignum right) {return *this - (*this / right)*right;}
       void operator /= (Bignum right) {*this = *this / right;}
       void operator %= (Bignum right) {*this = *this % right;}
       Bignum sqrt() {
               if(*this<0) return -1;
               Bignum st=1, en=*this, mid, sqm;
               while(st<=en) {
                       mid=(st+en).div2();
                       sqm=mid*mid;
                       if(sqm==*this) break;
                       else if(sqm>*this) en=mid-1;
                       else st=mid+1;
               }
               if(sqm>*this) mid-=1;
               return mid;
       }
       void printout(void) {
               int i;
               if(sign)printf("-");
               printf("%i",digit[digits-1]);
               for (i=digits-2;i>=0;i--) printf("%i",digit[i]);
               printf("\n");
       }
       void readin(void) {
				int i;
               char c;
               while(1) {
					c=fgetc(stdin);
					if(c>32) break;
				}
				sign = (c=='-');
				digits = 0;
				do {
					if(c>='0'&&c<='9') {
						for(i=digits;i>0;i--) digit[i] = digit[i-1];
						digit[0] = c-'0';
						digits++;
					}
					c=fgetc(stdin);
				} while(c>='0'&&c<='9');
       }
};

Bignum x, gcd, a, b, zero(0);

int main() {
	int T, t, N, i;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d",&N);N--;
		
		x.readin();
		gcd = zero;
		for(i=0;i<N;i++) {
			b.readin();
			if(b>x) b=b-x;
			else b=x-b;
			a = gcd;gcd = b;
			while(a!=0) {
				gcd = a;
				a = b%a;
				b = gcd;
			}
		}
		x %= gcd;
		printf("Case #%d: ",t);
		if(x>0) x=gcd-x;
		x.printout();
	}
	return 0;
}
