#include <iostream>
#include <fstream>
#include <stdio.h>
#include <iomanip>
#include <algorithm>
#include <string>
#include <cctype>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <functional>
#include <stdarg.h>
#include <stdlib.h>
#include <iterator>
#include <math.h>
#include <complex>
#include <numeric>
using namespace std;

class IntArr
{
      public:
    	  IntArr();
    	  IntArr(const IntArr&);
    	  ~IntArr();
    	  void Read();
    	  IntArr Inverse(IntArr);
    	  IntArr LToIntArr(long long);
    	  long IntArrToL(IntArr);
    	  IntArr SToIntArr(string);
    	  void operator--(int);
    	  IntArr operator-(IntArr);
    	  void operator-=(IntArr);
    	  IntArr operator-(long long);
    	  void operator-=(long long);
    	  void operator++(int); 
    	  IntArr operator+(IntArr);
    	  void operator+=(IntArr);
    	  IntArr operator+(long long);
    	  void operator+=(long long);
    	  IntArr operator*(IntArr);
    	  void operator*=(IntArr);
    	  IntArr operator*(long long);
    	  void operator*=(long long);
    	  IntArr operator/(IntArr);
    	  void operator/=(IntArr);
    	  IntArr operator/(long long);
    	  void operator/=(long long);
    	  IntArr operator%(IntArr);
    	  void operator%=(IntArr);
    	  IntArr operator%(long long);
    	  void operator%=(long long);
    	  IntArr operator^(IntArr);
    	  IntArr operator^(long long);
    	  IntArr operator<<(IntArr);
    	  IntArr operator<<(long long);
    	  void operator=(IntArr);
    	  void operator=(long long);
    	  void operator=(string);
    	  short& operator[](int);
    	  bool operator==(IntArr);
    	  bool operator==(long long);
    	  bool operator!=(IntArr);
    	  bool operator!=(long long);
    	  bool operator>(IntArr);
    	  bool operator>(long long);
    	  bool operator>=(IntArr);
    	  bool operator>=(long long);
    	  bool operator<(IntArr);
    	  bool operator<(long long);
    	  bool operator<=(IntArr);
    	  bool operator<=(long long);
    	  void Print();

      private:
		  static const int MXNR = 64;
	      short * arr;
    	  int size;
    	  char sign;
    	  void Error(int);
    	  IntArr Multiply(IntArr,long long);
};

IntArr::IntArr()
{
      arr=new short[MXNR];
      size=0;
      sign='+';
      arr[0]=0;
}

IntArr::IntArr(const IntArr& arr2)
{
      sign=arr2.sign;
      size=arr2.size;
      arr=new short[MXNR];
      for(int i=0;i<=size;i++)
	     arr[i]=arr2.arr[i];
}

IntArr::~IntArr()
{
      delete []arr;
}

void IntArr::Read()
{
string s;

      arr[0]=0;
      cin>>s;
      if(s[0]=='-') sign='-';
      else { sign='+'; size++; arr[size]=s[0]-'0';}
      
      for(int i=1;i<s.length();i++)
      {
          size++;
          arr[size]=s[i]-'0';
      }
}

IntArr IntArr::Inverse(IntArr x)
{
       IntArr y;
       y.sign=x.sign;
       y.size=x.size;
       for(int i=1;i<=x.size;i++)
	       y[i]=x[x.size-i+1];
	   y[0]=0;
	   
       return y;
}

IntArr IntArr::LToIntArr(long long l)
{
int p=1,now=1,term=0;
IntArr q;

     if(l>=0) q.sign='+';
     else { q.sign='-'; l*=-1; }
     
     if(l==0) {q.size=1; q[1]=0;}
     
     while( (l%p!=l)&&(term==0) )
     {
	  q[q.size]=(l%p)/now;
	  q.size++;
	  if(l%p==l) term=1;
	  now=p;
	  p*=10;
     }
     q[q.size]=(l%p)/now;
     q=Inverse(q);
     
     return q;
}

long IntArr::IntArrToL(IntArr x)
{
long l=0;
     
     x=Inverse(x);
     for(int i=x.size;i>=1;i--)
         { l*=10; l+=x[i]; }
     
     if(x.sign=='-') l*=-1;
     
     return l;
}

IntArr IntArr::SToIntArr(string S)
{
IntArr q;
       
       q.size=S.length();
       
       for(int i=0;i<S.length();i++)
          q[i+1]=S[i]-'0';
          
       return q;
}

void IntArr::operator--(int l)
{
     *this-=1;
}

IntArr IntArr::operator-(IntArr f)
{
int temp,c,s1,s2;
IntArr t=*this,d;

     if(t.sign!=f.sign)
     {
    	 f.sign=t.sign;
    	 t+=f;
    	 return t;
     }
     
     if(t.sign==f.sign)
     {
    	 if(t==f) { t.size=1; t[1]=0; t.sign='+'; return t; }

	     if(t.sign=='-')
    	 {
    	       f.sign='+';
    	       t.sign='+';
    	       s1=t.size-f.size;
    	       s2=f.size-t.size;
    	       
    	       if(t>f)
    	       {
    	    	      for(int i=f.size;i>=1;i--)
	        		      if(t[s1+i]>=f[i]) t[s1+i]-=f[i];
        			      else
        			      {
           	    			  t[s1+i]+=10;
            				  t[s1+i]-=f[i];
            				  c=i;
            				  while(1)
            				  {
	            			       if(t[s1+c-1]!=0)
		                			    {t[s1+c-1]--; break; }
         	    			       else { t[s1+c-1]=9; c--; }
           	    	          }
                          }
           		       t.sign='-';
         		       while(t[1]==0)
	    	           {
	                		  t.size--;
                 			  for(int i=1;i<=t.size;i++)
	                		      t[i]=t[i+1];
	    	           }

    		           return t;
               }
               
               if(f>t)
    	       {
                      d=f-t;
                      d.sign='+';
                      
                      return d;
               }
               
         }
         
         if(t.sign=='+')
         {
               if(t>f)
    	       {
                      t.sign='-';
                      f.sign='-';
                      d=t-f;
                      d.sign='+';
                      
                      return d;
               }     
               
               if(f>t)
    	       {
    	    	      t.sign='-';
                      f.sign='-';
                      d=t-f;
                      d.sign='-';
                      
                      return d;
               }
         }
         
     }
}

void IntArr::operator-=(IntArr g)
{
     *this=*this-g;
}

IntArr IntArr::operator-(long long l)
{
IntArr b,q;

     q=LToIntArr(l);
     b=*this-q;
     
     return b;
}

void IntArr::operator-=(long long l)
{
     *this=*this-l;
}

void IntArr::operator++(int l)
{
     *this+=1;
}

IntArr IntArr::operator+(IntArr p)
{
int temp,remainder=0;
IntArr q=*this,d;

       q[0]=0;

       if(sign==p.sign)
       {
           if(q.size>=p.size)
           {
         	   for(int i=0;i<=q.size;i++)
         	   {
    	              if(i<p.size) { temp=q[q.size-i]+p[p.size-i]+remainder; }
    	              else temp=q[q.size-i]+remainder;

    	              q[q.size-i]=temp%10;
            	      remainder=temp/10;
               }
               if(q[0]!=0) 
               {
                     q.size++;
            	     for(int i=q.size;i>=1;i--)
            	         q[i]=q[i-1]; 
               }
               
            	 return q;
           }
           else  return p+q;
       }
     
       if(sign!=p.sign)
       {
            if(q.sign=='+') { p.sign='+'; q-=p; return q; }
            if(q.sign=='-') { q.sign='+'; p-=q; return p; }
       } 
}

void IntArr::operator+=(IntArr c)
{
     *this=*this+c;
}

IntArr IntArr::operator+(long long l)
{
IntArr b,q;

     q=LToIntArr(l);
     b=*this+q;
     
     return b;
}
void IntArr::operator+=(long long l)
{
     *this=*this+l;
}

IntArr IntArr::operator*(IntArr y)
{
int temp,remainder=0,c;
IntArr t,b,a[10]; 
     
     b.sign='+'; t.sign='+';

     a[0]=0;
     a[1]=*this;
     for(int i=2;i<=9;i++)
         a[i]=Multiply(*this,i);
     
     for(int i=y.size;i>=1;i--)
     {
	     t=a[ y[i] ];
	     c=t.size+1;
	     t.size+=y.size-i;
	     for(int k=c;k<=t.size;k++) t[k]=0;
   	     b+=t;
         t.size=0;
         remainder=0;
     }
     if(sign!=y.sign) b.sign='-';
     
     return b;
}

void IntArr::operator*=(IntArr q)
{
     *this=*this*q;
}

IntArr IntArr::operator*(long long l)
{
IntArr b,q;

     q=LToIntArr(l);
     b=q**this;
     
     return b;
}

void IntArr::operator*=(long long l)
{
     *this=*this*l;
}

IntArr IntArr::operator/(IntArr x)
{
IntArr q=*this,d,temp,max;
char s;
bool term=false;

     if(q.sign==x.sign) s='+';
     else s='-';
     
     if(x==0) Error(0);

     max.sign='+';
     q.sign='+';
     x.sign='+';

     if(q<x)
     {
    	  d.size++;
    	  d[d.size]=0;
    	  d.sign='+';

    	  return d;
     }

     if(q==x)
     {
    	  d.size++;
    	  d[d.size]=1;
    	  d.sign=s;

    	  return d;
     }
     
     max.size=q.size-x.size+1;
     for(int i=1;i<=max.size;i++) 
         max[i]=0;
     
     while(1)
     {
         max[1]=1;
         if(max*x>q) { term=true; break; }
         
         for(int i=1;i<=q.size;i++)
         {   
         	 for(int j=1;j<=10;j++)
        	 {
                 max[i]=j;
                 temp=max*x;
             
                 if(temp>q) { max[i]=j-1; break; }
             }
          }
          break;
     }
     
     if(!term) { max.sign=s; return max; }
     
     max.size--;
     for(int i=1;i<=q.size;i++)
     {
       	 for(int j=1;j<=10;j++)
       	 {
              max[i]=j;
              temp=max*x;       
              if(temp>q) { max[i]=j-1; break; }
         }
     }
     max.sign=s;
          
     return max;
}

void IntArr::operator/=(IntArr x)
{
     *this=*this/x;
}

IntArr IntArr::operator/(long long l)
{
IntArr b,q;
       
       q=LToIntArr(l);
       b=*this/q;
       
       return b;
}

void IntArr::operator/=(long long l)
{
     *this=*this/l;
}

IntArr IntArr::operator%(IntArr x)
{
IntArr q=*this,p;
       
       p=q/x;
       p*=x;
       q-=p;
       
       return q;
}

void IntArr::operator%=(IntArr x)
{
     *this=*this%x;
}

IntArr IntArr::operator%(long long l)
{
IntArr b,q;
       
       q=LToIntArr(l);
       b=*this%l;
       
       return b;
}

void IntArr::operator%=(long long l)
{
     *this=*this%l;
}

IntArr IntArr::operator^(IntArr x)
{
IntArr q,i;
       
       if(x<0) Error(2);
       
       q=1;
       x+=10000;
       
       for(i=10000;i<x;i++)
           q*=*this;
       
       return q;
}

IntArr IntArr::operator^(long long l)
{
IntArr q;
       
       q=LToIntArr(l);
       q=*this^q;
       
       return q;
}

IntArr IntArr::operator<<(IntArr x)
{
IntArr q,t;
       
       t=2;
       q=t^x;
       q*=*this;
       
       return q;
}

IntArr IntArr::operator<<(long long l)
{
IntArr q;
       
       q=LToIntArr(l);
       q=*this<<q;
       
       return q;
}

void IntArr::operator=(IntArr vec2)
{
      sign=vec2.sign;
      size=vec2.size;
      for(int i=0;i<=size;i++)
    	  arr[i]=vec2[i];
}

void IntArr::operator=(long long l)
{
IntArr q;
     
     q=LToIntArr(l);
     *this=q;
}

void IntArr::operator=(string S)
{
     *this=SToIntArr(S);
}

short& IntArr::operator[](int i)
{
      if(i<0||i> MXNR) Error(2);
      
      return arr[i];
}

bool IntArr::operator==(IntArr x)
{
     if(sign!=x.sign) return false;
     if(size!=x.size) return false;
     for(int i=1;i<=size;i++)
       	if(arr[i]!=x[i]) return false;
     
     return true;
}

bool IntArr::operator==(long long l)
{
IntArr q;
     
     q=LToIntArr(l);
     if(*this==q) return true;
     
     return false;
}

bool IntArr::operator!=(IntArr x)
{
     if(*this==x) return false;
     
     return true;
}


bool IntArr::operator!=(long long l)
{
     if(*this==l) return false;
     
     return true;
}

bool IntArr::operator>(IntArr x)
{
     if(*this<x) return false;
     
     if(*this==x) return false;
     
     return true;
}

bool IntArr::operator>(long long l)
{
     if(*this<l) return false;
     
     if(*this==l) return false;
     
     return true;
}

bool IntArr::operator>=(IntArr x)
{
     if(*this<x) return false;
     
     return true;
}

bool IntArr::operator>=(long long l)
{
     if(*this<l) return false;
     
     return true;
}

bool IntArr::operator<(IntArr x)
{
     if(sign!=x.sign)
         if(sign=='+') return false;
         else return true;
     
     if(sign=='+')
         if(size>x.size) return false;
         else  if(size<x.size) return true;
               else 
                    for(int i=1;i<=size;i++)
                    {
                            if(arr[i]>x[i]) return false;
                            if(arr[i]<x[i]) return true;
                    }
     
     if(sign=='-')
         if(size>x.size) return true;
         else  if(size<x.size) return false;
               else 
                    for(int i=1;i<=size;i++)
                    {
                            if(arr[i]>x[i]) return true;
                            if(arr[i]<x[i]) return false;
                    }
     
     return false;
}

bool IntArr::operator<(long long l)
{
IntArr q;

     q=LToIntArr(l);
     if(*this<q) return true;
     
     return false;
}

bool IntArr::operator<=(IntArr x)
{
     if(*this>x) return false;
     
     return true;
}

bool IntArr::operator<=(long long l)
{
     if(*this>l) return false;
     
     return true;
}

void IntArr::Print()
{     
      if(sign=='-') cout<<"-";
      
      for(int i=1;i<=size;i++)
           cout<<arr[i];
      cout<<endl;
}

void IntArr::Error(int nr)
{
     switch(nr)
     {
           case 0: cout<<"Devision by Zero"<<endl; break;
           case 1: cout<<"Wrong Size: "<<size<<" > "<<MXNR<<endl; break;
           case 2: cout<<"Wrong Subscript: "              <<endl; break;
     }
     system("pause");
     exit(1);
}

IntArr IntArr::Multiply(IntArr x,long long l)
{
int temp,remainder=0,c;
IntArr t; 
       
       for(int i=x.size;i>=1;i--)
       {
    		 temp=x[i]*l+remainder;
    		 t.size++;
    		 t[t.size]=temp%10;
    		 remainder=temp/10;
       }
       if(remainder>0)  { t.size++; t[t.size]=remainder%10; }
	   t=Inverse(t);
	   
	   return t;
}


typedef long long LL;
typedef long double LD;
typedef complex<double> point;
typedef complex<double> Vector;
typedef pair<point, point> Segment;
typedef pair<int, int> PII;
typedef pair<int, double> PID;
typedef pair<int, string> PIS;
typedef pair<PII, PII> PPII;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<point> VP;
typedef vector<VI> VVI;
typedef vector<VD> VVD;
typedef vector<VVI> VVVI;
typedef vector<PII> VPII;
typedef vector<string> VS;

#define f(i, n)					for(int i = 0; i < n; i++)
#define fo(i, a, b)				for(int i = a; i <= b; i++)
#define fx(it, x)				for(typeof((x).begin()) it = (x).begin(); it != (x).end();++it)
#define popcount(n)				__builtin_popcount(n)
#define clz(n)					__builtin_clz(n)
#define ctz(n)					__builtin_ctz(n)
#define gcd(a, b)				__gcd(a, b)
#define lcm(a, b)				((a) / gcd(a, b) * b)
#define nom						first
#define den						second
#define sz(a)					(int(a.size()))
#define pb						push_back
#define all(v)					v.begin(), v.end()
#define EQ(a, b)				(abs((a) - (b)) < EPS)
#define sqr(a)					((a) * (a))
#define cl(x, el)				memset(x, el, sizeof(x))
#define wait					system("pause")
#define Get_Time(time)			(double)((double)(clock() - time) / (double)CLOCKS_PER_SEC)

inline LL strtoint(const string &s) {stringstream ss;ss<<s;LL ret;ss>>ret;return ret;}
inline string inttostr(const LL &a) {stringstream ss;ss<<a;string ret;ss>>ret;return ret;}

const double INF = 1e50;
const double EPS = 1e-9;
const double Pi = acos(- 1.0);
const int MAX = 1 << 28;
const int MIN = - MAX;
const int MAX_N = 10000;



int N;
IntArr a[MAX_N], diff[MAX_N], gcd, ans;




void Read()
{
	cin >> N;
	
	f(i, N)
	{
	string s;
		
		cin >> s;
		
		a[i] = s;
	}
	
//	system("pause");
}

IntArr GCD(IntArr a, IntArr b)
{
IntArr t;
	
	if(a == b) return a;
	if(a < b) swap(a, b);
	
	while(b != 0)
	{
		t = b;
		b = a % b;
		a = t;
	}
	
	return a;
}

void Solve()
{
	f(i, N) fo(j, i + 1, N - 1) if(a[j] < a[i]) swap(a[i], a[j]); 
	
	f(i, N - 1) diff[i] = a[i + 1] - a[i];
	
//	cout << "A:\n";
//	f(i, N) a[i].Print();
//	cout << "Diff:\n";
//	f(i, N - 1) diff[i].Print();
	
	gcd = diff[0];
	
	f(i, N - 1) gcd = GCD(gcd, diff[i]);
	
//	cout << "GCD:\n";
//	gcd.Print();
	
	IntArr k = a[0] / gcd;
	
	if(k == 0) k = 1;
	
//	cout << "K:\n";
//	k.Print();
	
	ans = k * gcd;
	if(ans < a[0]) ans += gcd;
	
	ans -= a[0];
	
//	cout << "Ans:\n";
//	ans.Print();
	
	
//	system("pause");
}

void Write(const int test_case)
{
	printf("Case #%d: ", test_case);
	
	ans.Print();
}

int main()
{
int TESTS;
	
	/*while(1)
	{
	string s1, s2;
	IntArr a1, b1, c1;
		
		cin >> s1 >> s2;
		
		a1 = s1;
		b1 = s2;
		
		c1 = GCD(a1, b1);
		
		c1.Print();
		
	}
	*/
	
	scanf("%d", & TESTS);
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve();
		
		Write(i);
	}
	
//	system("pause");
	
	return 0;
}
