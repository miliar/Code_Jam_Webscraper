#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <hash_map>
#include <iostream>
#include <iomanip>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <stack>
#include <sstream>
#include <string.h>
#include <utility>
#include <vector>

using namespace stdext; // 用hash_map需要加上这一句
using namespace std;

//BEGINTEMPLATE_BY_ACRUSH_TOPCODER
#define SIZE(X) ((int)(X.size()))//NOTES:SIZE(
#define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(
typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64
#define two(X) (1<<(X))//NOTES:two(
#define twoL(X) (((int64)(1))<<(X))//NOTES:twoL(
#define contain(S,X) (((S)&two(X))!=0)//NOTES:contain(
#define containL(S,X) (((S)&twoL(X))!=0)//NOTES:containL(

const double pi=acos(-1.0);//NOTES:pi
const double eps=1e-11;//NOTES:eps
class bigint;

template<class T> inline void checkmin(T &a,T b)  //将a,b中的较小数存在a中
{
	if(b<a) 
		a=b;
}

template<class T> inline void checkmax(T &a,T b)  //将a,b中的较大数存在a中
{
	if(b>a) 
		a=b;
}

template<class T> inline T sqr(T x)  //返回x的平方
{
	return x*x;
}

template<class T> inline T pow(T x, int n)  //返回x^n
{
	T count = 1;
	for(int i = 0; i < n; i++)
	{
		count *= x;
	}
	return count;
}

int mulsqrt(int n, int p) //返回p^(1/n) 如果没有，则取最接近的较小的值。
{
	int mulsqrt;
	int low;
	int high;
	int med;
	if(n == 1)
		mulsqrt = p;	
	else if(n > 1)
	{
		low = 1;
		high = 10;
		while(pow(high, n) < p)
		{
			high *= 10;
		}
		low = high / 10;

		while(high - low > 1)
		{
			med = (high + low) / 2;
			if(pow(med, n) == p)
			{
				return med;
			}
			else if(pow(med, n) < p)
			{
				low = med;
			}
			else
			{
				high = med;
			}
		}
		
		if(pow(high, n) == p)
		{
			mulsqrt = high;
		}
		else
		{
			mulsqrt = low;
		}
	}
	return mulsqrt;
}

typedef pair<int,int> ipair;//NOTES:ipair
template<class T> inline T lowbit(T n)  //返回n的最低位
{
	return (n^(n-1))&n;
}

template<class T> inline int countbit(T n)   //返回位为1的个数
{
	return (n==0)?0:(1+countbit(n&(n-1)));
}

//Numberic Functions
template<class T> inline T gcd(T a,T b)		//返回a,b的最大公约数
{
	if(a<0)
		return gcd(-a,b);
	if(b<0)
		return gcd(a,-b);
	return (b==0)?a:gcd(b,a%b);
}

template<class T> inline T lcm(T a,T b)		//返回a,b的最小公倍数
{
	if(a<0)
		return lcm(-a,b);
	if(b<0)
		return lcm(a,-b);
	return a*(b/gcd(a,b));
}

template<class T> inline T euclide(T a,T b,T &x,T &y)//NOTES:euclide(
{
	if(a<0)
	{
		T d=euclide(-a,b,x,y);
		x=-x;
		return d;
	}
	if(b<0)
	{
		T d=euclide(a,-b,x,y);
		y=-y;
		return d;
	}
	if(b==0)
	{
		x=1;
		y=0;
		return a;
	}
	else
	{
		T d=euclide(b,a%b,x,y);
		T t=x;
		x=y;
		y=t-(a/b)*y;
		return d;
	}
}

template<class T> inline vector<pair<T,int> > factorize(T n)//NOTES:factorize(
{
	vector<pair<T,int> > R;
	for (T i=2;n>1;)
	{
		if (n%i==0)
		{
			int C=0;
			for(;n%i==0;C++,n/=i);
			R.push_back(make_pair(i,C));
		}
		i++;
		if (i>n/i) 
			i=n;
	}
	if (n>1) 
		R.push_back(make_pair(n,1));
	return R;
}

template<class T> inline bool isPrimeNumber(T n) //验证是否为素数
{
	if(n<=1)
		return false;
	for(T i=2;i*i<=n;i++) 
		if (n%i==0) 
			return false;
	return true;
}

template<class T> inline T eularFunction(T n)//NOTES:eularFunction(
{
	vector<pair<T,int> > R=factorize(n);
	T r=n;
	for(int i=0;i<R.size();i++)
		r=r/R[i].first*(R[i].first-1);
	return r;
}

//Matrix Operations
const int MaxMatrixSize=40;//NOTES:MaxMatrixSize
template<class T> inline void showMatrix(int n,T A[MaxMatrixSize][MaxMatrixSize])//NOTES:showMatrix(
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
			cout<<A[i][j];
		cout<<endl;
	}
}

template<class T> inline T checkMod(T n,T m) //返回n除以m后的余数
{
	return (n%m+m)%m;
}

template<class T> inline void identityMatrix(int n,T A[MaxMatrixSize][MaxMatrixSize])//使A为单位矩阵
{
	for(int i=0;i<n;i++) 
		for(int j=0;j<n;j++) 
			A[i][j]=(i==j)?1:0;
}

template<class T> inline void addMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//两矩阵相加，C=A+B
{
	for(int i=0;i<n;i++) 
		for(int j=0;j<n;j++) 
			C[i][j]=A[i][j]+B[i][j];
}

template<class T> inline void subMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//两矩阵相减，C=A-B
{
	for(int i=0;i<n;i++) 
		for(int j=0;j<n;j++) 
			C[i][j]=A[i][j]-B[i][j];
}

template<class T> inline void mulMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T _A[MaxMatrixSize][MaxMatrixSize],T _B[MaxMatrixSize][MaxMatrixSize])//两矩阵相乘，C=A*B
{ 
	T A[MaxMatrixSize][MaxMatrixSize],B[MaxMatrixSize][MaxMatrixSize];
	for(int i=0;i<n;i++) 
		for(int j=0;j<n;j++) 
			A[i][j]=_A[i][j],B[i][j]=_B[i][j],C[i][j]=0;
	
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++) 
			for(int k=0;k<n;k++) 
				C[i][j]+=A[i][k]*B[k][j];
}

template<class T> inline void addModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//两矩阵相加后取模，C=(A+B)%m
{
	for(int i=0;i<n;i++) 
		for(int j=0;j<n;j++) 
			C[i][j]=checkMod(A[i][j]+B[i][j],m);
}

template<class T> inline void subModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//两矩阵相减后取模，C=(A-B)%m
{
	for(int i=0;i<n;i++) 
		for(int j=0;j<n;j++) 
			C[i][j]=checkMod(A[i][j]-B[i][j],m);
}

template<class T> inline T multiplyMod(T a,T b,T m) //相乘后取模 (a*b)%m
{
	return (T)((((int64)(a)*(int64)(b)%(int64)(m))+(int64)(m))%(int64)(m));
}

template<class T> inline void mulModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T _A[MaxMatrixSize][MaxMatrixSize],T _B[MaxMatrixSize][MaxMatrixSize])//矩阵的元素对应相乘，再加上C的对应元素，取模
{ 
	T A[MaxMatrixSize][MaxMatrixSize],B[MaxMatrixSize][MaxMatrixSize];
	for(int i=0;i<n;i++) 
		for(int j=0;j<n;j++) 
			A[i][j]=_A[i][j],B[i][j]=_B[i][j],C[i][j]=0;
	
	for(int i=0;i<n;i++) 
		for(int j=0;j<n;j++) 
			for (int k=0;k<n;k++) 
			C[i][j]=(C[i][j]+multiplyMod(A[i][k],B[k][j],m))%m;
}

template<class T> inline T powerMod(T p,int e,T m)//返回(p^e)%m
{
	if(e==0)
		return 1%m;
	else if(e%2==0)
	{
		T t=powerMod(p,e/2,m);
		return multiplyMod(t,t,m);
	}
	else 
		return multiplyMod(powerMod(p,e-1,m),p,m);
}

//Point&Line
double dist(double x1,double y1,double x2,double y2) //返回(x1,y1),(x2,y2)的距离
{
	return sqrt(sqr(x1-x2)+sqr(y1-y2));
}

double distR(double x1,double y1,double x2,double y2) //返回(x1,y1),(x2,y2)的距离的平方
{
	return sqr(x1-x2)+sqr(y1-y2);
}

template<class T> T cross(T x0,T y0,T x1,T y1,T x2,T y2) //(x1,y1)减去(x0,y0) 点乘 (x2,y2)减去(x0,y0)
{
	return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);
}

int crossOper(double x0,double y0,double x1,double y1,double x2,double y2)//判断两向量点乘后的符号
{
	double t=(x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);
	if (fabs(t)<=eps) 
		return 0;
	return (t<0)?-1:1;
}

bool isIntersect(double x1,double y1,double x2,double y2,double x3,double y3,double x4,double y4)//NOTES:isIntersect(
{
	return crossOper(x1,y1,x2,y2,x3,y3)*crossOper(x1,y1,x2,y2,x4,y4)<0 && crossOper(x3,y3,x4,y4,x1,y1)*crossOper(x3,y3,x4,y4,x2,y2)<0;
}

//Translator
bool isUpperCase(char c) //判断是否为大写字母
{
	return c>='A' && c<='Z';
}

bool isLowerCase(char c) //判断是否为小写字母
{
	return c>='a' && c<='z';
}

bool isLetter(char c) //判断是否为字母
{
	return c>='A' && c<='Z' || c>='a' && c<='z';
}

bool isDigit(char c) //判断是否为数字
{
	return c>='0' && c<='9';
}

char toLowerCase(char c) //变为小写字母
{
	return (isUpperCase(c))?(c+32):c;
}

char toUpperCase(char c) //变为大写字母
{
	return (isLowerCase(c))?(c-32):c;
}

template<class T> string toString(T n) //转化为字符串
{
	ostringstream ost;ost<<n;
	ost.flush();
	return ost.str();
}

int toInt(string s) //字符串转化为数字
{
	int r=0;
	istringstream sin(s);
	sin>>r;
	return r;
}

int64 toInt64(string s) //字符串转化为int64
{
	int64 r=0;
	istringstream sin(s);
	sin>>r;
	return r;
}

double toDouble(string s) //字符串转化为double
{
	double r=0;
	istringstream sin(s);
	sin>>r;
	return r;
}

template<class T> void stoa(string s,int &n,T A[]) //字符串转化为数组(空格为分界)
{
	n=0;
	istringstream sin(s);
	for(T v;sin>>v;A[n++]=v);
}

template<class T> void atos(int n,T A[],string &s) //数组转化为字符串(空格分界)
{
	ostringstream sout;
	for(int i=0;i<n;i++)
	{
		if(i>0)
			sout<<' ';
		sout<<A[i];
	}
	s=sout.str();
}

template<class T> void atov(int n,T A[],vector<T> &vi) //数组转化为向量
{
	vi.clear();
	for(int i=0;i<n;i++) 
		vi.push_back(A[i]);
}

template<class T> void vtoa(vector<T> vi,int &n,T A[]) //向量转化为数组
{
	n=vi.size();
	for(int i=0;i<n;i++)
		A[i]=vi[i];
}

template<class T> void stov(string s,vector<T> &vi) //字符串转化为向量
{
	vi.clear();
	istringstream sin(s);
	for(T v;sin>>v;vi.push_bakc(v));
}

template<class T> void vtos(vector<T> vi,string &s) //向量转化为字符串
{
	ostringstream sout;
	for(int i=0;i<vi.size();i++)
	{
		if(i>0)
			sout<<' ';
		sout<<vi[i];
	}
	s=sout.str();
}

list<string> split(string s, char cut = ' ') //字符串转化为链表
{
	list<string> input;
	s.append(1, ' '); //尾部加一个空格
	string tmp = "";
	for(unsigned int i = 0; i < s.length(); i++)
	{
		if(s[i] == ' ' || s[i] == 0)
		{
			if(tmp != "")
			{
				input.push_back(tmp);
				tmp = "";
			}
			continue;
		}
		else
		{
			tmp.append(1, s[i]);
		}
	}
	return input;
}
//Fraction
template<class T> struct Fraction
{
	T a,b;
	Fraction(T a=0,T b=1);
	string toString();
};

template<class T> Fraction<T>::Fraction(T a,T b)
{
	T d=gcd(a,b);
	a/=d;
	b/=d;
	if (b<0) 
	{
		a=-a;
		b=-b;
	}
	this->a=a;
	this->b=b;
}

template<class T> string Fraction<T>::toString()
{
	ostringstream sout;
	sout<<a<<"/"<<b;
	return sout.str();
}

template<class T> Fraction<T> operator+(Fraction<T> p,Fraction<T> q)
{
	return Fraction<T>(p.a*q.b+q.a*p.b,p.b*q.b);
}

template<class T> Fraction<T> operator-(Fraction<T> p,Fraction<T> q)
{
	return Fraction<T>(p.a*q.b-q.a*p.b,p.b*q.b);
}

template<class T> Fraction<T> operator*(Fraction<T> p,Fraction<T> q)
{
	return Fraction<T>(p.a*q.a,p.b*q.b);
}

template<class T> Fraction<T> operator/(Fraction<T> p,Fraction<T> q)
{
	return Fraction<T>(p.a*q.b,p.b*q.a);
}

template<class T> bool operator>(Fraction<T> p,Fraction<T> q)
{
	return p.a*q.b > p.b*q.a;
}

template<class T> bool operator<(Fraction<T> p,Fraction<T> q)
{
	return p.a*q.b < p.b*q.a;
}

template<class T> bool operator>=(Fraction<T> p,Fraction<T> q)
{
	return !(p.a*q.b < p.b*q.a);
}

template<class T> bool operator<=(Fraction<T> p,Fraction<T> q)
{
	return !(p.a*q.b > p.b*q.a);
}

template<class T> bool operator>(Fraction<T> p,bigint q)
{
	return p.a > p.b * q;
}

template<class T> bool operator<(Fraction<T> p,bigint q)
{
	return p.a < p.b * q;
}

template<class T> bool operator>=(Fraction<T> p,bigint q)
{
	return !(p.a < p.b * q);
}

template<class T> bool operator<=(Fraction<T> p,bigint q)
{
	return !(p.a > p.b * q);
}

class group
{
public:
	string dic;
	int val;
	group(string dic = "", int val = 0);
};

group::group(string dic, int val)
{
	this->dic = dic;
	this->val = val;
}
//ENDTEMPLATE_BY_ACRUSH_TOPCODER


//LINE
int compare(double a,double b)	//a等于b，则为0。a小于b，则为-1。a大于b，则为1。
{
	return(fabs(a-b)<=eps)?0:((a<b)?-1:1);
}

struct Point
{
	double x,y;
	Point(double _x=0,double _y=0)
	{
		x=_x;
		y=_y;
	}
	int compareTo(const Point &other)
	{
		int c=compare(x,other.x);
		if (c!=0) 
			return c;
		return compare(y,other.y);
	}
};

struct Line
{
	double a,b,c;
	Line(double _a=0,double _b=0,double _c=0)
	{
		a=_a;
		b=_b;
		c=_c;
		double d=sqrt(sqr(a)+sqr(b));
		a/=d;
		b/=d;
		c/=d;
		if (a<-eps || a<=eps && b<0) 
		{
			a=-a;
			b=-b;
			c=-c;
		}
	}
	int compareTo(const Line &other)
	{
		int c1=compare(a,other.a);
		if (c1!=0) 
			return c1;
		int c2=compare(b,other.b);
		if (c2!=0) 
			return c2;
		return compare(c,other.c);
	}
};

struct Circle
{
	double x,y,r;
	Circle(double _x=0,double _y=0,double _r=0)
	{
		x=_x;
		y=_y;
		r=_r;
	}
	int compareTo(const Circle &other)
	{
		int c1=compare(x,other.x);
		if (c1!=0) 
			return c1;
		int c2=compare(y,other.y);
		if (c2!=0) 
			return c2;
		return compare(r,other.r);
	}
};

Line getLineByTwoPoints(const Point &p1,const Point &p2) //两点式
{
	double a=+(p1.y-p2.y);
	double b=-(p1.x-p2.x);
	double c=p1.x*p2.y-p2.x*p1.y;
	return Line(a,b,c);
}

double ppDistance(const Point &a,const Point &b) //两点距离
{
	return dist(a.x,a.y,b.x,b.y);
}

double plDistance(const Point &p,const Line &l) //点线距离
{
	return fabs(l.a*p.x+l.b*p.y+l.c)/sqrt(sqr(l.a)+sqr(l.b));
}

double cross(const Point &a,const Point &b,const Point &c) //见cross功能
{
	return cross(a.x,a.y,b.x,b.y,c.x,c.y);
}

int crossop(const Point &a,const Point &b,const Point &c)
{
	return compare(cross(a,b,c),0);
}

bool isMiddle(double a,double m,double b) //m在a和b中间，返回true
{
	return fabs(a-m)<=eps || fabs(b-m)<=eps || (a<m)!=(b<m);
}

bool isMiddle(const Point &a,const Point &m,const Point &b) //如果m在a,b的线上，并且在a,b中间，返回true
{
	return crossop(a,m,b)==0 && isMiddle(a.x,m.x,b.x) && isMiddle(a.y,m.y,b.y);
}

bool isTouchIntersect(const Point &a,const Point &b,const Point &c,const Point &d)
{
	return isMiddle(a,c,d) || isMiddle(a,d,b) || isMiddle(c,a,d) || isMiddle(c,b,d);
}

bool isCrossIntersect(const Point &a,const Point &b,const Point &c,const Point &d)
{
	return (crossop(a,b,c)*crossop(a,b,d)<0 && crossop(c,d,a)*crossop(c,d,b)<0);
}

bool isIntersect(const Point &a,const Point &b,const Point &c,const Point &d)
{
	return isCrossIntersect(a,b,c,d) || isTouchIntersect(a,b,c,d);
}

double psDistance(const Point &p,const Point &a,const Point &b)
{
	double sab=sqr(a.x-b.x)+sqr(a.y-b.y);
	double spa=sqr(p.x-a.x)+sqr(p.y-a.y);
	double spb=sqr(p.x-b.x)+sqr(p.y-b.y);
	if (fabs(spa-spb)<=sab)
		return fabs(cross(p,a,b))/sqrt(sab);
	else
		return sqrt(min(spa,spb));
}

int getIntersect(const Line &A,const Line &B,Point &P)
{
	double a1=A.a;
	double b1=A.b;
	double c1=A.c;
	double a2=B.a;
	double b2=B.b;
	double c2=B.c;
	double t=a1*b2-a2*b1;
	if (fabs(t)<=eps) 
		return 0;
	double X0=+(b1*c2-b2*c1)/t;
	double Y0=-(a1*c2-a2*c1)/t;
	P.x=X0;
	P.y=Y0;
	return 1;
}

int getIntersect(const Line &A,const Circle &C,Point &P,Point &Q)
{
	double a=A.a;
	double b=A.b;
	double c=A.c;
	double CX=C.x,CY=C.y;
	double R=C.r;
	//ax+by+c=0
	//(+by+c+aCX)^2+(ay-aCY)^2=(aR)^2
	double x1,y1,x2,y2;
	if (fabs(a)>fabs(b))
	{
		double A=sqr(a)+sqr(b);
		double B=2.0*b*(c+a*CX)-2.0*sqr(a)*CY;
		double C=sqr(c+a*CX)+sqr(a)*(sqr(CY)-sqr(R));
		double delta=sqr(B)-4*A*C;
		if (delta<-eps) 
			return 0;
		if (delta<0) delta=0;
		delta=sqrt(delta);
		y1=(-B+delta)/(2*A);
		x1=(-c-b*y1)/a;
		y2=(-B-delta)/(2*A);
		x2=(-c-b*y2)/a;
		P.x=x1;
		P.y=y1;
		Q.x=x2;
		Q.y=y2;
	}
	else
	{
		swap(a,b);
		swap(CX,CY);
		double A=sqr(a)+sqr(b);
		double B=2.0*b*(c+a*CX)-2.0*sqr(a)*CY;
		double C=sqr(c+a*CX)+sqr(a)*(sqr(CY)-sqr(R));
		double delta=sqr(B)-4*A*C;
		if (delta<-eps) 
			return 0;
		if (delta<0) delta=0;
		delta=sqrt(delta);
		y1=(-B+delta)/(2*A);
		x1=(-c-b*y1)/a;
		y2=(-B-delta)/(2*A);
		x2=(-c-b*y2)/a;
		swap(x1,y1);
		swap(x2,y2);
		swap(a,b);
		swap(CX,CY);
		P.x=x1;
		P.y=y1;
		Q.x=x2;
		Q.y=y2;
	}
	return 2;
}

int getIntersect(const Circle &A,const Circle &B,Point &P,Point &Q)
{
	double X1=A.x,Y1=A.y,X2=B.x,Y2=B.y;
	double R1=A.r,R2=B.r;
	double dst=dist(X1,Y1,X2,Y2);
	if (dst>R1+R2+eps || dst<fabs(R1-R2)-eps) 
		return 0;
	if (dst<=eps) 
		return 0;
	//(x-X1)^2+(y-Y1)^2=sqr(R1)=x^2-2*X1*x+X1^2+y^2-2*Y1*y+Y1^2 (1)
	//(x-X2)^2+(y-Y2)^2=sqr(R2)=x^2-2*X2*x+X2^2+y^2-2*Y2*y+Y2^2 (2)
	//(2)-(1):  sqr(R2)-sqr(R1)=2*(X1-X2)*x+2*(Y1-Y2)*y+sqr(X2)-sqr(X1)+sqr(Y2)-sqr(Y1)
	//	 :  (X1-X2)*x+(Y1-Y2)*y-(sqr(X1)-sqr(X2)+sqr(Y1)-sqr(Y2)-sqr(R1)+sqr(R2))/2.0;
	double a=X1-X2;
	double b=Y1-Y2;
	double c=-(a*(X1+X2)+b*(Y1+Y2)-sqr(R1)+sqr(R2))/2.0;
	double CX=X1,CY=Y1;
	//ax+by+c=0
	//(+by+c+aCX)^2+(ay-aCY)^2=(aR)^2
	double x1,y1,x2,y2;
	if (fabs(a)>fabs(b))
	{
		double A=sqr(a)+sqr(b);
		double B=2.0*b*(c+a*CX)-2.0*sqr(a)*CY;
		double C=sqr(c+a*CX)+sqr(a)*(sqr(CY)-sqr(R1));
		double delta=sqr(B)-4*A*C;
		if (delta<-eps) 
			return 0;
		if (delta<0) 
			delta=0;
		delta=sqrt(delta);
		y1=(-B+delta)/(2*A);
		x1=(-c-b*y1)/a;
		y2=(-B-delta)/(2*A);
		x2=(-c-b*y2)/a;
		P.x=x1;
		P.y=y1;
		Q.x=x2;
		Q.y=y2;
	}
	else
	{
		swap(a,b);
		swap(CX,CY);
		double A=sqr(a)+sqr(b);
		double B=2.0*b*(c+a*CX)-2.0*sqr(a)*CY;
		double C=sqr(c+a*CX)+sqr(a)*(sqr(CY)-sqr(R1));
		double delta=sqr(B)-4*A*C;
		if (delta<-eps) 
			return 0;
		if (delta<0) 
			delta=0;
		delta=sqrt(delta);
		y1=(-B+delta)/(2*A);
		x1=(-c-b*y1)/a;
		y2=(-B-delta)/(2*A);
		x2=(-c-b*y2)/a;
		swap(x1,y1);
		swap(x2,y2);
		swap(a,b);
		swap(CX,CY);
		P.x=x1;
		P.y=y1;
		Q.x=x2;
		Q.y=y2;
	}
	return 2;
}

//END OF LINE

//BIGINT
const int maxlength=200;

class bigint
{
public:
	int oper;			//负数时，oper = -1;非负数时，oper = 1
	int length;			//4位一段，段数
	int* a;	//每段的内容。下标从1到length
	bigint(int=0);
	bigint(const bigint& m); //拷贝构造函数
	~bigint();
	int max(int a,int b);
	void check();
	void operator=(bigint m);
	void operator=(int m);
	void operator=(char *s);
	bool operator<(bigint m) const;
	bool operator<=(bigint m) const;
	bool operator>(bigint m) const;
	bool operator>=(bigint m) const;
	bool operator==(bigint m) const;
	bool operator!=(bigint m) const;
	bigint operator-() const;
	bigint operator+(bigint m);
	void operator+=(bigint m);
	bigint operator-(bigint m);
	void operator-=(bigint m);
	bigint operator*(bigint m);
	bigint operator*(int m);
	void operator*=(bigint m);
	void operator*=(int m);
	bigint operator/(bigint m);
	bigint operator/(int m);
	void operator/=(bigint m);
	void operator/=(int m);
	bigint operator%(bigint m);
	bigint operator%(int m);
	void operator%=(bigint m);
	void operator%=(int m);
};

std::ostream& operator<<(std::ostream& result, const bigint& a); //输出
std::istream& operator>>(std::istream& result, bigint& a); //输入
bigint abs(bigint m);
bool read(bigint &m);
void write(bigint m);
void swrite(char *s,bigint m);
void writeln(bigint m);
bigint sqr(bigint m);
bigint pow(bigint m, int e);
bigint sqrt(bigint m);
bigint gcd(bigint a,bigint b);
bigint lcm(bigint a,bigint b);

string int2str_big(int m)
{
	stack<int> st;
	string s = "";
	int i = 0;
	while(i < 4)
	{
		st.push(m%10);
		m /= 10;
		i++;
	}
	while(!st.empty())
	{
		s.append(1, char('0' + st.top()));
		st.pop();
	}
	return s;
}

int str2int(string s)
{
	int m = 0;
	int option = 0; //0时表示还没开始找到第一位有效数字，1时表示已经找到有效数字
	unsigned int i = 0;
	while(i < s.length())
	{

		if(option == 0)
		{
			if(s[i] == '0')
			{		
				i++;
			}
			else
			{
				option = 1;
				m = 10*m + (s[i] - '0');
				i++;
			}
			continue;
		}
		if(option == 1)
		{
			m = 10*m + (s[i] - '0');
			i++;
		}
	}
	return m;
}

string check(string s)
{
	string tmpstr = "";
	int zerocount = 0;
	int oper = 1;
	if (s[0] == '-')
	{
		oper = -1;
		zerocount++;//负号占了一位，故偏移量加1，消完0后再补上
	}
	while(true)
	{
		if(s[zerocount] != '0')
			break;
		zerocount++;
	}
	if(oper == -1)
	{
		tmpstr = "-";
	}
	tmpstr += s.substr(zerocount, s.length());
	return tmpstr;
}

int bigint::max(int a,int b)
{
	return (a>b)?a:b;
}

bigint::bigint(int v)
{
	a = new int[maxlength];
	(*this)=v;
	this->check();
}

bigint::bigint(const bigint& m) //拷贝构造函数
{
	a = new int[maxlength];
	memcpy(a,m.a,maxlength*sizeof(int));
	oper = m.oper;
	length = m.length;
}

bigint::~bigint()
{
	delete[] a;
}

void bigint::check()
{
	for(;length>0 && a[length]==0;length--);
	if(length==0)
		oper=1;
}

void bigint::operator=(bigint m)
{
	oper=m.oper;
	length=m.length;
	memcpy(a,m.a,maxlength*sizeof(int));
	this->check();
}

void bigint::operator=(int m)
{
	oper=(m>0)?1:-1;
	m=abs(m);
	memset(a,0,maxlength*sizeof(int));
	for (length=0;m>0;m=m/10000)
		a[++length]=m%10000;
	this->check();
}

void bigint::operator=(char *s)
{
	int i,L;
	(*this)=0;
	if(s[0]=='-' || s[0]=='+')
	{
		if(s[0]=='-')
			oper=-1;
		L=strlen(s);
		for(i=0;i<L;i++)
			s[i]=s[i+1];
	}
	L=strlen(s);
	length=(L+3)/4;
	for (i=0;i<L;i++)
		a[(L-i+3)/4]=a[(L-i+3)/4]*10+(s[i]-48);
	this->check();
}

bool bigint::operator<(bigint m) const
{
	if (oper!=m.oper)
		return oper<m.oper;
	if (length!=m.length)
		return oper*length<m.length*oper;
	for (int i=length;i>=1;i--)
		if (a[i]!=m.a[i])
			return a[i]*oper<m.a[i]*oper;
	return false;
}

bool bigint::operator<=(bigint m) const
{
	return !(m<(*this));
}

bool bigint::operator>(bigint m) const
{
	return m<(*this);
}

bool bigint::operator>=(bigint m) const
{
	return !((*this)<m);
}

bool bigint::operator==(bigint m) const
{
	return (!((*this)<m)) && (!(m<(*this)));
}

bool bigint::operator!=(bigint m) const
{
	return ((*this)<m) || (m<(*this));
}

bigint bigint::operator-() const
{
	bigint c=(*this);
	c.oper=-c.oper;
	c.check();
	return c;
}

bigint abs(bigint m)
{
	bigint c=m;
	c.oper=abs(c.oper);
	c.check();
	return c;
}


bigint pow(bigint m, int e) //返回m^e
{
	if(e == 0)
		return bigint(1);
	if(e%2 == 0)
	{
		return pow(sqr(m), e/2);
	}
	else
		return pow(m,e-1) * m;
}

bigint mulsqrt(int n, bigint p) //返回p^(1/n) 如果没有，则取最接近的较小的值。
{
	bigint mulsqrt;
	bigint low;
	bigint high;
	bigint med;
	if(n == 1)
		mulsqrt = p;	
	else if(n > 1)
	{
		low = 1;
		high = 10;
		while(pow(high, n) < p)
		{
			high *= 10;
		}
		low = high / 10;

		while(high - low > 1)
		{
			med = (high + low) / 2;
			if(pow(med, n) == p)
			{
				return med;
			}
			else if(pow(med, n) < p)
			{
				low = med;
			}
			else
			{
				high = med;
			}
		}
		
		if(pow(high, n) == p)
		{
			mulsqrt = high;
		}
		else
		{
			mulsqrt = low;
		}
	}
	return mulsqrt;
}

bigint bigint::operator+(bigint m)
{
	if (m.length==0)
		return (*this);
	if (length==0)
		return m;
	if (oper==m.oper)
	{
		bigint c;
		c.oper=oper;
		c.length=max(length,m.length)+1;
		for (int i=1,temp=0;i<=c.length;i++)
			c.a[i]=(temp=(temp/10000+a[i]+m.a[i]))%10000;
		c.check();
		return c;
	}
	return (*this)-(-m);
}

bigint bigint::operator-(bigint m)
{
	if (m.length==0)
		return (*this);
	if (length==0)
		return (-m);
	if (oper==m.oper)
	{
		bigint c;
		if (abs(*this)>=abs(m))
		{
			c.oper=oper;
			c.length=length;
			for (int i=1,temp=0;i<=length;i++)
				c.a[i]=((temp=(-int(temp<0)+a[i]-m.a[i]))+10000)%10000;
			c.check();
			return c;
		}
		return -(m-(*this));
	}
	return (*this)+(-m);
}

bool read(bigint &m) //读入
{
	char s[maxlength*4+10];
	if (scanf("%s",&s)==-1)
		return false;
	for (int i=0;s[i];i++)
		if (!(s[i]>='0' && s[i]<='9' || (s[i]=='+' || s[i]=='-') && i==0))
			return false;
	m=s;
	return true;
}

void swrite(char *s,bigint m) //将m写在s里，并加一个空格
{
	int L=0;
	if (m.oper==-1)
		s[L++]='-';
	sprintf(s+L,"%d",m.a[m.length]);
	for(;s[L]!=0;L++);
	for(int i=m.length-1;i>=1;i--)
	{
		sprintf(s+L,"%04d",m.a[i]);
		L+=4;
	}
	s[L]=0;
}

string bigint2str(bigint m)
{
	string s = "";
	m.check();
	if(m.oper == -1)
		s += "-";
	for(int i = 0; i < m.length; i++)
	{
		s += int2str_big(m.a[m.length - i]);
	}
	s = check(s);
	return s;
}

bigint str2bigint(string s)
{
	bigint m;
	if(s[0] == '-')
	{
		m.oper = -1;
		s = s.substr(1, s.length()); //注意substr的用法。
	}
	
	m.length = (s.length() - 1)/4 + 1;
	m.a[0] = 0;
	int tmp = s.length()%4;
	if(tmp == 0)
		tmp += 4;
	m.a[m.length] = str2int(s.substr(0, tmp));
	for(int i = 1; i < m.length; i++)
	{
		m.a[i] = str2int(s.substr(s.length() - 4*i, 4));
	}
	m.check();
	return m;
}

void write(bigint m) //输出
{
	if (m.oper==-1)
		printf("-");
	printf("%d",m.a[m.length]);
	for(int i=m.length-1;i>=1;i--)
		printf("%04d",m.a[i]);
}

void writeln(bigint m) //输出换行
{
	write(m);
	printf("\n");
}

bigint bigint::operator*(bigint m)
{
	bigint c;
	c.oper=oper*m.oper;
	c.length=length+m.length;
	for(int i=1;i<=m.length;i++)
	{
		int number=m.a[i],j,temp=0;
		for(j=1;j<=length;j++)
			c.a[i+j-1]+=number*a[j];
		if(i%10==0 || i==m.length)
		{
			for(j=1;j<=c.length;j++)
				c.a[j]=(temp=(temp/10000)+c.a[j])%10000;
		}
	}
	c.check();
	return c;
}

bigint bigint::operator*(int m)
{
	if (m<0)
		return -((*this)*(-m));
	if (m>100000)
		return (*this)*bigint(m);
	bigint c;
	c.length=length+2;
	c.oper=oper;
	int t=0;
	for (int i=1;i<=c.length;i++)
		c.a[i]=(t=(t/10000+a[i]*m))%10000;
	c.check();
	return c;
}

bigint bigint::operator/(bigint m)
{
	if (m.length==0)
	{
		printf("Division by zero.\n");
		exit(0);
	}
	if (abs(*this)<abs(m))
		return 0;
	bigint c,left;
	c.oper=oper/m.oper;
	m.oper=1;
	c.length=length-m.length+1;
	left.length=m.length-1;
	memcpy(left.a+1,a+length-left.length+1,left.length*sizeof(int));
	for(int i=c.length;i>=1;i--)
	{
		left=left*10000+a[i];
		int head=0,tail=10000,mid;
		while (head+1<tail)
		{
			mid=(head+tail)/2;
			if (m*mid<=left)
				head=mid;
			else
				tail=mid;
		}
		c.a[i]=head;
		left-=m*head;
	}
	c.check();
	return c;
}

bigint bigint::operator/(int m)
{
	if (m<0)
		return -((*this)/(-m));
	if (m>100000)
		return (*this)/bigint(m);
	bigint c;
	c.oper=oper;
	c.length=length;
	int t=0;
	for (int i=c.length;i>=1;i--)
		c.a[i]=(t=(t%m*10000+a[i]))/m;
	c.check();
	return c;
}

bigint bigint::operator %(bigint m)
{
	return (*this)-((*this)/m)*m;
}

bigint bigint::operator%(int m)
{
	if (m<0)
		return -((*this)%(-m));
	if (m>100000)
		return (*this)%bigint(m);
	int t=0;
	for (int i=length;i>=1;i--)
		t=(t*10000+a[i])%m;
	return t;
}

bigint sqr(bigint m)
{
	return m*m;
}

bigint sqrt(bigint m)
{
	if (m.oper<0 || m.length==0)
		return 0;
	bigint c,last,now,templast;
	c.length=(m.length+1)/2;
	c.a[c.length]=int(sqrt((double)m.a[c.length*2]*10000+m.a[c.length*2-1])+1e-6);
	templast.length=c.length*2;
	templast.a[c.length*2-1]=(c.a[c.length]*c.a[c.length])%10000;
	templast.a[c.length*2]=(c.a[c.length]*c.a[c.length])/10000;
	templast.check();
	for (int i=c.length-1;i>=1;i--)
	{
		last=templast;
		int head=0,tail=10000,mid,j,temp;
		while (head+1<tail)
		{
			mid=(head+tail)/2;
			now=last;
			now.a[2*i-1]+=mid*mid;
			for (j=i+1;j<=c.length;j++)
				now.a[i+j-1]+=mid*c.a[j]*2;
			now.length++;
			for (j=2*i-1,temp=0;j<=now.length;j++)
				now.a[j]=(temp=(temp/10000+now.a[j]))%10000;
			now.check();
			if (now<=m)
			{
				templast=now;
				head=mid;
			}
			else
				tail=mid;
		}
		c.a[i]=head;
	}
	c.check();
	return c;
}

bigint gcd(bigint a,bigint b)
{
	return (b==0)?a:gcd(b,a%b);
}

bigint lcm(bigint a,bigint b)
{
	return a*b/gcd(a,b);
}

void bigint::operator+=(bigint m)
{
	(*this)=(*this)+m;
}

void bigint::operator-=(bigint m)
{
	(*this)=(*this)-m;
}

void bigint::operator*=(bigint m)
{
	(*this)=(*this)*m;
}

void bigint::operator/=(bigint m)
{
	(*this)=(*this)/m;
}

void bigint::operator%=(bigint m)
{
	(*this)=(*this)%m;
}

void bigint::operator*=(int m)
{
	(*this)=(*this)*m;
}

void bigint::operator/=(int m)
{
	(*this)=(*this)/m;
}

void bigint::operator%=(int m)
{
	(*this)=(*this)%m;
}

std::ostream& operator<<(std::ostream& result, const bigint& a) //输出
{
	write(a);
	return result;
}

std::istream& operator>>(std::istream& result, bigint& a) //输入
{
	read(a);
	return result;
}
//END OF BIGINT

//BIGDOUBLE
class bigdouble
{
public:
	bigint ori;
	int e;
	bigdouble(bigint m = 0, int e = 0);
	~bigdouble();
	int max(int a,int b);
	int min(int a,int b);
	void check();
	void operator=(bigdouble m);
	void operator=(bigint m);
	void operator=(char *s);
	bool operator<(bigdouble m);
	bool operator<=(bigdouble m);
	bool operator>(bigdouble m);
	bool operator>=(bigdouble m);
	bool operator==(bigdouble m);
	bool operator!=(bigdouble m);
	bigdouble operator-();
	bigdouble operator+(bigdouble m);
	void operator+=(bigdouble m);
	bigdouble operator-(bigdouble m);
	void operator-=(bigdouble m);
	bigdouble operator*(bigdouble m);
	bigdouble operator*(int m);
	void operator*=(bigdouble m);
	void operator*=(int m);
	bigdouble operator/(bigdouble m);
	bigdouble operator/(int m);
	void operator/=(bigdouble m);
	void operator/=(int m);
};

bigdouble abs(bigdouble m);
string bigdouble2str(bigdouble m); //写入字符串
bigdouble str2bigdouble(string s);
bool read(bigdouble &m);
void write(bigdouble m);
void swrite(char *s,bigdouble m);
void write2str(bigdouble m,char *s);
void writeln(bigdouble m);
bigdouble sqr(bigdouble m);
bigdouble pow(bigdouble m, int e);
bigdouble sqrt(bigdouble m);

int bigdouble::max(int a,int b)
{
	return (a>b)?a:b;
}

int bigdouble::min(int a,int b)
{
	return (a<b)?a:b;
}

bigdouble::bigdouble(bigint m, int e)
{
	(*this).ori = m;
	(*this).e = e;

	this->check();
}

bigdouble::~bigdouble()
{
}

void bigdouble::check()
{
	if((*this).ori.length == 0)
		return;
	ori.check();
	string s = bigint2str(ori);
	int countzero = 0;
	while(s[s.length() - 1 - countzero] == '0')
	{
		countzero++;
	}
	s.resize(s.length() - min(countzero, e));
	ori = str2bigint(s);
	e -= min(countzero, e);
}

void bigdouble::operator=(bigdouble m)
{
	ori.oper=m.ori.oper;
	ori.length=m.ori.length;
	e = m.e;
	memcpy(ori.a,m.ori.a,maxlength*sizeof(int));
	this->check();
}

void bigdouble::operator=(bigint m)
{
	ori.oper=(m>0)?1:-1;
	m=abs(m);
	e=0;
	memset(ori.a,0,maxlength*sizeof(int));
	string s;
	for (ori.length=0;m>0;m=m/10000)
	{
		ori.a[++ori.length] = (m%10000).a[1];	
	}
	this->check();
}

void bigdouble::operator=(char *s)
{
	(*this).ori = s;
	(*this).e = 0;
	this->check();
}

bool bigdouble::operator<(bigdouble m)
{
	if(e < m.e) //后面的数有小数位
		ori *= pow(bigint(10), m.e - e);
	else
		m.ori *=  pow(bigint(10), e - m.e);

	if (ori.oper!=m.ori.oper)
		return ori.oper<m.ori.oper;
	if (ori.length!=m.ori.length)
		return ori.oper*ori.length<m.ori.length*ori.oper;
	for (int i=ori.length;i>=1;i--)
		if (ori.a[i]!=m.ori.a[i])
			return ori.a[i]*ori.oper<m.ori.a[i]*ori.oper;
	return false;
}

bool bigdouble::operator<=(bigdouble m)
{
	return !(m<(*this));
}

bool bigdouble::operator>(bigdouble m)
{
	return m<(*this);
}

bool bigdouble::operator>=(bigdouble m)
{
	return !((*this)<m);
}

bool bigdouble::operator==(bigdouble m)
{
	return (!((*this)<m)) && (!(m<(*this)));
}

bool bigdouble::operator!=(bigdouble m)
{
	return ((*this)<m) || (m<(*this));
}

bigdouble bigdouble::operator-() //负号
{
	bigdouble c=(*this);
	c.ori.oper=-c.ori.oper;
	c.check();
	return c;
}

bigdouble abs(bigdouble m)
{
	bigdouble c=m;
	c.ori.oper=abs(c.ori.oper);
	c.check();
	return c;
}

bigdouble pow(bigdouble m, int e)
{
	if(e == 0)
		return bigdouble(1);
	else
	{
		m.e *= e; //指数相乘
		m.ori = pow(m.ori, e);
		m.check();
	}
	return m;
}

bigdouble bigdouble::operator+(bigdouble m)
{
	bigdouble c;
	if(e < m.e) //后面的数有小数位
		ori *= pow(bigint(10), m.e - e);
	else if(e > m.e)
		m.ori *= pow(bigint(10), e - m.e);
	
	c.ori = ori + m.ori;
	c.e = max(e, m.e);
	c.check();
	return c;
}

bigdouble bigdouble::operator-(bigdouble m)
{
	bigdouble c;
	if(e < m.e) //后面的数有小数位
		ori *= pow(bigint(10), m.e - e);
	else if(e > m.e)
		m.ori *= pow(bigint(10), e - m.e);
	
	c.ori = ori - m.ori;
	c.e = max(e, m.e);
	c.check();
	return c;
}

bool read(bigdouble &m) //读入
{
	string s;
	cin>>s;
	m = str2bigdouble(s);

	return true;
}

void swrite(char *s,bigdouble m) //将m写在s里，并加一个空格
{
	m.e = 0;
	swrite(s, m.ori);
}

string bigdouble2str(bigdouble m) //写入字符串
{
	m.check();
	string s = bigint2str(m.ori);
	int reallength = s.length(); //去掉正负号的数字长度
	if(m.ori.oper == -1)
		reallength--;

	if(reallength <= m.e) //小数位数不够，前面补零
	{
		string tmp = "";//符号
		if(m.ori.oper == -1)
			tmp = "-";

		for(int i = 0; i <m.e - reallength + 1; i++) //补零
			tmp += "0";

		if(m.ori.oper == -1) //补上数字
			s = tmp + s.substr(1,s.length());
		else
			s = tmp + s;
	}
	if(m.e != 0) //补上小数点
	{
		s = s.substr(0, s.length() - m.e) + "." + s.substr(s.length() - m.e, s.length());
	}
	return s;
}

bigdouble str2bigdouble(string s)
{
	bigdouble m;
	if(s[0] == '-')
	{
		m.ori.oper = -1;
		s = s.substr(1, s.length());
	}
	bool isdouble = false;
	unsigned int pos = 0;
	for(pos = 0; pos < s.length(); pos++)
	{
		if(s[pos] == '.')
		{
			isdouble = true;
			break;
		}
	}

	if(!isdouble) //整数
	{
		if(m.ori.oper == -1)
			s = "-" + s;
		m.ori = str2bigint(s);
		m.e = 0;
	}
	else //小数
	{
		s = s.substr(0, pos) + s.substr(pos+1, s.length()); //去掉小数点
		if(m.ori.oper == -1)
			s = "-" + s;
		m.ori = str2bigint(s);
		m.e = s.length() - pos; //确定小数点位置
	}
	return m;
}

void write(bigdouble m) //输出
{
	cout<<bigdouble2str(m);
}

void writeln(bigdouble m) //输出换行
{
	write(m);
	printf("\n");
}

bigdouble bigdouble::operator*(bigdouble m)  //乘法
{
	bigdouble c;
	c.e = e + m.e;
	c.ori = ori * m.ori;
	c.check();	
	return c;
}

bigdouble bigdouble::operator*(int m) //乘法
{
	bigdouble c;
	c.ori *= m;	
	c.check();
	return c;
}

bigdouble bigdouble::operator/(bigdouble m) //除法
{
	bigdouble c;
	c.e = e - m.e;
	c.ori = ori / m.ori;
	c.check();
	return c;
}

bigdouble bigdouble::operator/(int m) //除法
{
	bigdouble c;
	c.ori /= m;	
	c.check();
	return c;
}

bigdouble sqr(bigdouble m)  //取平方
{
	return m*m;
}

bigdouble sqrt(bigdouble m)  //取平方根
{
	bigdouble c;
	if(m.e%2 == 1)
	{
		m.e++;
		m.ori *= 10;
	}
	c.ori = sqrt(m.ori);
	c.e /= 2;
	c.check();
	return c;
}

void bigdouble::operator+=(bigdouble m)
{
	(*this)=(*this)+m;
}

void bigdouble::operator-=(bigdouble m)
{
	(*this)=(*this)-m;
}

void bigdouble::operator*=(bigdouble m)
{
	(*this)=(*this)*m;
}

void bigdouble::operator/=(bigdouble m)
{
	(*this)=(*this)/m;
}

void bigdouble::operator*=(int m)
{
	(*this)=(*this)*m;
}

void bigdouble::operator/=(int m)
{
	(*this)=(*this)/m;
}

std::ostream& operator<<(std::ostream& result, const bigdouble& a) //输出
{
	write(a);
	return result;
}

std::istream& operator>>(std::istream& result, bigdouble& a) //输入
{
	read(a);
	return result;
}
//END OF BIGDOUBLE

int least[519]; //储存最小块数

void solve()
{
	int start = 1;
	int cardcount = 1;
	Fraction<bigint> current(100, 2);
	while(cardcount <= 273)
	{
		while(current >= start)
		{
			least[start] = cardcount;
			start++;
		}
		cardcount++;
		Fraction<bigint> now(100, cardcount+1);
		current = current + now;
	}
}

int main()
{
	unsigned int C;
	cin>>C;
	for(int c = 0; c < C; c++)
	{
		int N;
		cin>>N;
		bigint *time = new bigint[N];
		for(int i = 0; i < N; i++)
		{
			cin>>time[i];
		}
		
		bigint T;
		bigint *time2 = new bigint[N];
		for(int i = 1; i < N; i++)
		{
			time2[i] = abs(time[i] - time[0]);
		}
		T = time2[1];
		for(int i = 2; i < N; i++)
		{
			T = gcd(T, time2[i]);
		}
//		cout<<T<<endl;
		delete[] time2;

		time[0] = time[0] % T;
		if(time[0] == 0)
		{
			cout<<"Case #"<<c+1<<": "<<0<<endl;
		}
		else
		{
			cout<<"Case #"<<c+1<<": "<<T-time[0]<<endl;
		}
		delete[] time;
	}
	return 0;
}
