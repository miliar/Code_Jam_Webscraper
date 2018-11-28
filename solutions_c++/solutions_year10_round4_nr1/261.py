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

//Corner case!!!
char grid[60][60];
bool good(int r,int c,int n)
{
	return r>=0&&c>=0&&r<n&&c<n;
}
int check(int r,int c,int n,int k)
{
	const complex<int> org(r,c);
	int res=10000000;
	int ss=0;
	for(int i=0;i<n;i++)
	for(int j=0;j<n;j++)
	{
		if(!isdigit(grid[i][j]))continue;
		complex<int> pos(i,j);
		const char dd=grid[i][j];
		for(int cc=0;cc<4;cc++)
		{
			if(good(pos.real(),pos.imag(),n))
			{
				//cerr<<r<<" "<<c<<" "<<i<<" "<<j<<" "<<pos<<endl;
				//assert(grid[pos.real()][pos.imag()]!=' ');
				if(grid[pos.real()][pos.imag()]!=dd&&
				isdigit(grid[pos.real()][pos.imag()]))return res;
			}
			if(cc==0||cc==2)pos.real()=2*r-pos.real();
			else pos.imag()=2*c-pos.imag();
			//pos=(pos-org)*complex<int>(0,1)+org;
		}
		ss=max(ss,abs(i-r)+abs(j-c)+1);
		//if(abs(i-r)+abs(j-c)+1==6)cerr<<i<<" XX "<<j<<" "<<grid[i][j]<<endl;
	}
//	debug(r);
//	debug(c);
//	debug(ss);
	return ss*ss-k*k;
}
int main()
{
	int ca=1,tt;
	for(cin>>tt;tt--;ca++)
	{
		int k;
		scanf("%d",&k);
		while(getchar()!='\n');

		memset(grid,'.',sizeof(grid));
		for(int i=0;i<2*k-1;i++)gets(grid[i]),grid[i][strlen(grid[i])]='.';
		const int n=2*k-1;
		debug(n);
		for(int i=0;i<n;i++,cerr<<endl)
		for(int j=0;j<n;j++)cerr<<grid[i][j];

		int ans=100000000;
		for(int x=-1;x<=n;x++)
		for(int y=-1;y<=n;y++)
		{
			ans=min(check(x,y,n,k),ans);
		}
end:
		debug(ans);
		debug(n);
		cout<<"Case #"<<ca<<": "<<ans<<endl;
//		assert(ans<n*n);
	}
	return 0;
}
