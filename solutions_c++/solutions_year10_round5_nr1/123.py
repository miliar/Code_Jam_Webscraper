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
// Convert anything to string
template<class T>
string convert(T vv)
{
	ostringstream re;
	re<<vv;
	return re.str();
}
template<typename T>
T convert(const string& ss)
{
	istringstream is(ss);
	T tmp;
	is>>tmp;
	return tmp;
}
//convert vector to string
template<class T>
string convert(vector<T> vv)
{
	ostringstream re;
	for(int i=0;i<vv.size();i++)
	{
		if(i)re<<" ";
		re<<vv[i];
	}
	return re.str();
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

//clear current line from  stdin
void clear_line()
{
	string tmp;
	getline(cin,tmp);
}
//Will read whitespace
void read_grid(int n,vector<string>& grid)
{
	grid.clear();
	grid.resize(n);
	for(int i=0;i<n;i++)
	{
		getline(cin,grid[i]);
	}
}
//Corner case!!!
vector<string> grid;
//Linear priem numbers sieve. The array factor[] store a prime factor of a composite number.
int primeSieve(int factor[],int prime[],int n)
{
	int top=0;
	memset(factor,0,sizeof(int)*(n+1));
	for(int i=2;i<=n;i++)
	{
		if(0==factor[i])prime[top++]=i;
		for(int j=0;j<top&&prime[j]*i<=n;j++)
		{
			factor[prime[j]*i]=prime[j];
			if(0==(i%prime[j]))break;
		}
	}
	return top;
}
llint getReverse(llint a,llint p,llint rev[]=NULL)
{
	if(rev!=NULL)return rev[a];
	llint x,y;
	assert(1==std::__gcd(a,p));
	__gcd(a,p,x,y);
	return ((x%p)+p)%p;
}

int fact[1000001],prime[1000001];
llint find_next(vector<llint> all,llint p)
{
	if(*max_element(all.begin(),all.end())>=p)return -1;
	if(all.size()==1)return -2;
	if(all.size()==2)
	{
		if(all[0]==all[1])return all[0];
		return -2;
	}
	llint s0=all[0],s1=all[1],s2=all[2];
	llint d1=(s1-s0+p)%p, d2=(s2-s1+p)%p;
	llint A,B;
	if(d1==0)
	{
		for(int i=1;i<all.size();i++)
			if(all[i]!=all[0])return -1;
		return all[0];
	}
	A=(d2*getReverse(d1,p))%p;
	B=(s1-((A*s0)%p)+p)%p;
	assert(s1==(A*s0+B)%p);
	assert(s2==(A*s1+B)%p);
	for(int i=1;i<all.size();i++)
	{
		if(all[i]!=((all[i-1]*A+B)%p))return -1;
	}
	return (all.back()*A+B)%p;
}
int main()
{
	const int top=primeSieve(fact,prime,1000000);
	debug(top);
	int ca=1,tt;
	for(cin>>tt;tt--;ca++)
	{
		int d,n;
		cin>>d>>n;
		int up=1;
		for(int i=0;i<d;i++)up*=10;
		debug(up);
		vector<llint> all(n);
		for(int i=0;i<n;i++)cin>>all[i];
	//	cerr<<d<<" "<<n<<endl;
	//	cerr<<all<<endl;
		vector<llint> ans;
		for(int i=0;i<top;i++)
		{
			if(prime[i]>up)break;
			llint next=find_next(all,prime[i]);
			if(next>=0)ans.push_back(next);
			else if(next==-2)ans.push_back(up+1),ans.push_back(up+2);
	//		cerr<<prime[i]<<" = "<<next<<endl;
		}
		sort(ans.begin(),ans.end());
		assert(ans.size());
		cout<<"Case #"<<ca<<": ";
		if(ans[0]!=ans.back())cout<<"I don't know."<<endl;
		else cout<<ans[0]<<endl;
	}
	return 0;
}
