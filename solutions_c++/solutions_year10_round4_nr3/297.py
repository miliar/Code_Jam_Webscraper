#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <sstream>
#include <map>
#include <cstring>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <stdarg.h>
//#define NDEBUG
#include <assert.h>
using namespace std;
#ifndef NDEBUG
    #define debug(x) cerr<<#x<<"=\""<<x<<"\""<<" at line#"<<__LINE__<<endl;
    #define hline() cerr<<"-----------------------------------------"<<endl;
	#define Unit_test(fun) class Test_##fun { public: Test_##fun (){ fun ();};}Test_obj_##fun
#else
    #define debug(x)
    #define hline()
	#define Unit_test(fun)
#endif
typedef long long int llint;
typedef unsigned long long int ullint;
#define low(x) ((((x)^((x)-1))&x))
#define two(x)  ((1)<<(x))
#define PB(x) push_back((x))
#define SORT(x) sort(x.begin(),x.end())
// print function
template<typename T1> void print_list(const T1& a){cerr<<a<<endl;}
template<typename T1,typename T2> void print_list(const T1& a,const T2& b){cerr<<a<<" "<<b<<endl;}
template<typename T1,typename T2,typename T3> void print_list(const T1& a,const T2& b,const T3& c){cerr<<a<<" "<<b<<" "<<c<<endl;}
template<typename T1,typename T2,typename T3,typename T4> void print_list(const T1& a,const T2& b,const T3& c,const T4& d){cerr<<a<<" "<<b<<" "<<c<<" "<<d<<endl;}
template<typename T1,typename T2,typename T3,typename T4,typename T5> void print_list(const T1& a,const T2& b,const T3& c,const T4& d,const T5& e){cerr<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<endl;}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6> void print_list(const T1& a,const T2& b,const T3& c,const T4& d,const T5& e,const T6& f){cerr<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<" "<<f<<endl;}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6,typename T7> void print_list(const T1& a,const T2& b,const T3& c,const T4& d,const T5& e,const T6& f,const T7& g){cerr<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<" "<<f<<" "<<g<<endl;}

//************************************************
template<typename A,typename B>
ostream& operator<<(ostream& out,const pair<A,B>& pp)
{
	out<<"("<<pp.first<<","<<pp.second<<")";
	return out;
}
template<typename A,typename B>
istream& operator<<(istream& in,pair<A,B>& pp)
{
	cerr<<"A pair wanted"<<endl;
	in>>pp.first>>pp.second;
	return in;
}

template<typename T>
ostream& operator<<(ostream& out,const vector<T>& vect)
{
	out<<"length = "<<vect.size()<<endl;
	for(int i=0;i<vect.size();i++)out<<vect[i]<<" ";
	out<<endl;
	return out;
}
template<typename T>
istream& operator>>(istream& in,vector<T>& vect)
{
	vect.clear();
	int n;
	cerr<<"A integer of length wanted"<<endl;
	in>>n;
	vect.resize(n);
	cerr<<n<<" elements wanted"<<endl;
	for(int i=0;i<n;i++)in>>vect[i];
	return in;
}

template<typename T>
ostream& operator<<(ostream& out,const vector<vector<T> >& vect)
{
	out<<"row number="<<vect.size()<<endl;
	for(int i=0;i<vect.size();i++)
	{
		out<<"row #"<<i<<":";
		for(int j=0;j<vect[i].size();j++)
			out<<" "<<vect[i][j];
		out<<endl;
	}
	return out;
}
template<typename T>
istream& operator>>(istream& in,vector<vector<T> >& vect)
{
	vect.clear();
	int n,m;
	cerr<<"Two integers wnated"<<endl;
	in>>n>>m;
	vect.resize(n);
	cerr<<"A matrix "<<n<<" X "<<m<<" wanted"<<endl;
	for(int i=0;i<n;i++)
	{
		vect[i].resize(m);
		for(int j=0;j<m;j++)in>>vect[i][j];
	}
	return in;
}

//**************************************************
// Tool functions
template<typename T>
inline void updateMax(T& a,const T& b){a=max(a,b);}
template<typename T>
inline void updateMin(T& a,const T& b){a=min(a,b);}
template<typename T>
inline vector<T> erase(vector<T> table,int ind)
{
	assert(ind<table.size());
	table.erase(table.begin()+ind);
	return table;
}
template<typename T>
vector<T> unique(vector<T> table)
{
	SORT(table);
	return vector<T>(table.begin(),unique(table.begin(),table.end()));
}

//Be carefull for cut into strings!!!!
template<class T>
vector<T> parse(const string& ss,const char* cut=" ")
{
	vector<T> re;
	for(int j=0;j<ss.size();j++)
	{
		string s;
		while(j<ss.size()&&NULL==strchr(cut,ss[j]))
			s+=ss[j++];
		if(!s.empty())
		{
			T tmp;
			istringstream is(s);
			is>>tmp;
			re.push_back(tmp);
		}
	}
	return re;
}
//****************************************8
/************ bitwise functions  ************/
int countBit(int n)
{
	int re=0;
	while(n)re++,n^=low(n);
	return re;
}
// Most significant bit
int MSB(int n)
{
	if(n==0)return 0;
	while(low(n)!=n)n^=low(n);
	return n;
}
void initHash(int n,int hash[])
{
	for(int i=0;i<n;i++)
		hash[two(i)]=i;
}
void initBcnt(int n,int bcnt[])
{
	bcnt[0]=0;
	for(int i=1;i<two(n);i++)
		bcnt[i]=bcnt[i^low(i)]+1;
}


//************************************************
//**********Number functions*****************
template<typename T>
T __gcd(T n,T m,T& a,T& b)
{
	T a1=0,b1=1;
	a=1,b=0;
	// a*n+b*m=n;  a1*n+b1*m=m;
	while(m)
	{
		T c=n/m;
		T r=n-m*c;
		T t;
		t=a;a=a1;a1=t-c*a1;
		t=b;b=b1;b1=t-c*b1;
		n=m;m=r;
	}
	return n;
}

//*******************************************
struct Node
{
	int r,c,d;
	int v;
	Node(int x,int y,int z,int v1):r(x),c(y),d(z),v(v1){};
	bool operator<(const Node& other)const
	{
		return v>other.v;
	};
};
// A small heap
priority_queue<Node> heap;

///*******************************************
const int dir[][2]={{-1,0},{0,1},{1,0},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
const char dname[]="NWSE";
//**********************************************


#define Mset(array,v,n)  memset(array,v,sizeof(array[0])*n)
template<typename T>
class point2D
{
	public:
	T _x,_y;
	T x()const{return _x;};
	T& x(){return _x;};
	T y()const{return _y;};
	T& y(){return _y;};
	point2D(){};
	point2D(T x,T y):_x(x),_y(y){};
	point2D(T x):_x(x),_y(0){};
	point2D(const point2D& other):_x(other._x),_y(other._y){};
	const point2D& operator=(const point2D<T>& other){_x=other._x,_y=other._y;return *this;};
	bool operator==(const point2D<T>& other)const{return _x==other._x&&_y==other._y;};
	double length()const {return sqrt(1.0*_x*_x+1.0*_y*_y);};
	double dnorm()const {return 1.0*_x*_x+1.0*_y*_y;};
	T norm()const
	{
		return	_x*_x+_y*_y;
	};
	bool operator<(const point2D& other)const
	{
		return x()<other.x()||(x()==other.x()&&y()<other.y());
	}
	point2D operator+=(const point2D& other)
	{
		_x+=other._x;
		_y+=other._y;
		return *this;
	};
	point2D operator+(const point2D& other)const
	{
		point2D res=*this;
		res+=other;
		return res;
	};
	
	point2D operator-=(const point2D& other)
	{
		_x-=other._x;
		_y-=other._y;
		return *this;
	};
	point2D operator-(const point2D& other)const
	{
		point2D res=*this;
		res-=other;
		return res;
	};

	point2D operator*=(const point2D& other)
	{
		point2D res=(*this)*other;
		*this=res;
		return *this;
	};
	point2D operator*(const point2D& other)const
	{
		point2D res;
		res._x=_x*other._x-_y*other._y;
		res._y=_x*other._y+_y*other._x;
		return res;
	};
	point2D conjugate()const
	{
		return point2D(_x,-_y);
	}
	point2D negate()const
	{
		return point2D(-_x,-_y);
	}
	point2D<double> operator/(const point2D<T>& other)const
	{
		assert(other.dnorm()>0.0);
		point2D<double> res=*this;
		res*=other.conjugate();
		res._x/=other.dnorm();
		res._y/=other.dnorm();
		return res;
	}
	point2D<double> operator/=(const point2D<T>& other)
	{
		*this=(*this)/other;
		return *this;
	}
	point2D<double> operator/(const T& other)
	{
		assert(fabs(1.0*other)>0.0);
		point2D res=*this;
		res._x/=other;
		res._y/=other;
		return res;
	}
	point2D<double> operator/=(T& other)
	{
		*this=(*this)/other;
		return *this;
	}
};
template<typename T>
ostream& operator<<(ostream& out,const point2D<T>& other)
{
	out<<"("<<other.x()<<","<<other.y()<<")";
	return out;
}
template<typename T>
istream& operator>>(istream& in,point2D<T>& other)
{
	in>>other.x()>>other.y();
	return in;
}


typedef point2D<int> point;

struct rect_t
{
	int x1,x2,y1,y2;
	rect_t(){};
	rect_t(int a,int b,int c,int d):x1(a),x2(b),y1(c),y2(d){};
	bool operator<(const rect_t& other)const
	{
		return y1<other.y1;
	}
	const rect_t& operator=(const rect_t& other)
	{
		x1=other.x1;
		x2=other.x2;
		y1=other.y1;
		y2=other.y2;
		return *this;
	};
};
const int N=2100;
//int XX[N][N],YY[N][N];
bool have[N][N];
int dp[N][N];
rect_t rec[1000];
vector<int> allx,ally;
int get_X(int x,int y){assert(x+1<allx.size());assert(y+1<ally.size());return allx[x+1]-allx[x];}
int get_Y(int x,int y){assert(x+1<allx.size());assert(y+1<ally.size());return ally[y+1]-ally[y];}
//Corner case!!!
bool bra[100][100],tmp[100][100];
int brute()
{
	int ans=0;
	bool have=false;
	for(int i=0;i<100;i++)
	for(int j=0;j<100;j++)
		if(bra[i][j])have=true;
	if(!have)return false;
	for(;;)
	{
		int cc=0;
		for(int i=0;i<100;i++)
		for(int j=0;j<100;j++)
		{

			tmp[i][j]=bra[i][j]||(i&&bra[i-1][j]&&j&&bra[i][j-1]);
			if((i==0||!bra[i-1][j])&&(j==0||!bra[i][j-1]))tmp[i][j]=false;
			if(tmp[i][j])cc++;
		}
		memcpy(bra,tmp,sizeof(tmp));
		ans++;
		if(0==cc)break;
	}
	for(int i=0;i<100;i++)
	for(int j=0;j<100;j++)
	{
		dp[i][j]=0;
		if(!bra[i][j])continue;
		dp[i][j]=1;
		if(i)dp[i][j]=max(dp[i][j],dp[i-1][j]+1);
		if(j)dp[i][j]=max(dp[i][j],dp[i][j-1]+1);
		ans=max(ans,dp[i][j]);
	}
	hline();
	cerr<<"brute"<<endl;
	for(int i=0;i<100;i++,cerr<<endl)
	for(int j=0;j<100;j++)cerr<<(bra[i][j]?1:0);
	cerr<<"brute = "<<ans<<endl;
	return ans;

}
int main()
{
	int ca=1,tt;
	for(cin>>tt;tt--;ca++)
	{
		allx.clear();
		ally.clear();
		memset(bra,false,sizeof(bra));
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>rec[i].x1>>rec[i].y1>>rec[i].x2>>rec[i].y2;
			rec[i].x1--;rec[i].y1--;
			int x1=rec[i].x1;
			int x2=rec[i].x2;
			int y1=rec[i].y1;
			int y2=rec[i].y2;
			allx.push_back(x1);
			allx.push_back(x2);
			ally.push_back(y1);
			ally.push_back(y2);
			for(int x=x1;x<x2;x++)
			for(int y=y1;y<y2;y++)bra[x][y]=true;
		}
		sort(rec,rec+n);
		debug(allx.size());debug(ally.size());
		allx=unique(allx);
		ally=unique(ally);
		debug(allx.size());debug(ally.size());
		const int nx=allx.size()-1;
		const int ny=ally.size()-1;
		assert(nx>0);assert(ny>0);
		for(int i=0;i<nx;i++)
		{
			int x1=allx[i],x2=allx[i+1];
			vector<rect_t> all;
			for(int j=0;j<n;j++)
			{
				if(rec[j].x1<=x1&&rec[j].x2>=x2)
				{
					all.push_back(rec[j]);
				}
			}
			cerr<<x1<<" to "<<x2<<" contain "<<all.size()<<" rects"<<endl;
			for(int j=0;j<all.size();j++)cerr<<all[j].y1<<" "<<all[j].y2<<endl;
			for(int j=1;j<all.size();j++)assert(all[j].y1>=all[j-1].y1);
			for(int j=0;j<ny;j++)
			{
				have[i][j]=false;
			}
			vector<point> seg;
			if(all.empty())continue;
			int head=all[0].y1,tail=all[0].y2;
			for(int j=1;j<all.size();j++)
			{
				if(all[j].y1<=tail)
				{
					assert(all[j].y1>=head);
					tail=all[j].y2;
				}
				else seg.push_back(point(head,tail)),
					head=all[j].y1,tail=all[j].y2;
			}
			seg.push_back(point(head,tail));
			cerr<<x1<<" to "<<x2<<" contains "<<seg.size()<<" segs"<<endl;
			for(int j=0;j<seg.size();j++)cerr<<seg[j]<<endl;
			for(int j=0,p=0;j<ny;j++)
			{
				while(p<seg.size()&&seg[p].y()<=ally[j])p++;
				if(p<seg.size()&&seg[p].x()<=ally[j])
				{
					assert(seg[p].y()>=ally[j+1]);
					have[i][j]=true;
				}
			}
		}

		hline();
		for(int j=0;j<ny;j++,cerr<<endl)
		for(int i=0;i<nx;i++)
			cerr<<(have[i][j]?1:0);

		for(int i=0;i<nx;i++)
		for(int j=0;j<ny;j++)
		{
			if(i&&j&&have[i-1][j]&&have[i][j-1])have[i][j]=true;
		}
		
		for(int i=0;i<nx;i++)cerr<<allx[i+1]-allx[i]<<" ";cerr<<endl;
		for(int i=0;i<ny;i++)cerr<<ally[i+1]-ally[i]<<" ";cerr<<endl;
		hline();
		for(int i=0;i<nx;i++,cerr<<endl)
		for(int j=0;j<ny;j++)cerr<<(have[i][j]?1:0);

		int ans=0;
		for(int i=0;i<nx;i++)
		for(int j=0;j<ny;j++)
		{
			dp[i][j]=0;
			if(!have[i][j])continue;
			int dx=get_X(i,j);
			int dy=get_Y(i,j);
			dp[i][j]=max(dx,dy);
			if(i)dp[i][j]=max(dp[i][j],dp[i-1][j]+dx);
			if(j)dp[i][j]=max(dp[i][j],dp[i][j-1]+dy);
			ans=max(ans,dp[i][j]);
			cerr<<i<<" "<<j<<"="<<dp[i][j]<<endl;
		}
		ans=brute();
		cerr<<"Case #"<<ca<<": "<<ans<<endl;
		cout<<"Case #"<<ca<<": "<<ans<<endl;

		//assert(ans==brute());
	}
	return 0;
}
