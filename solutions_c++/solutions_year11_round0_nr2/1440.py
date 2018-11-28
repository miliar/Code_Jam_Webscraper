#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <limits>

using namespace std;
#define clr(x,a) memset((x), a, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define REPD(i,a,b) for(i=a-1;i>=b;i--)
#define repd(i,n) REPD(i,n,0)
#define KG <<"	"<<
#define KG2 <<"	"
#define KH cout<<endl;
#define INF 2147483647
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}

typedef long double ld;
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

ifstream fin;
ofstream fout;

typedef struct twochar
{
	char a;
	char b;
	bool operator < (twochar const& _A) const

       {

              //这个函数指定排序策略，按nID排序，如果nID相等的话，按strName排序

              if(a < _A.a)  return true;

              if(a == _A.a) return (b < _A.b);

              return false;

       }
}twochar;

map<twochar, char>com;
	map<twochar, char>cle;
	vector<char>vec;
	map<twochar,char>::iterator it;
	twochar t;

void check(char ch)
{
	int i;
	char ch2, ch3;
			if(vec.empty())
			{
				vec.push_back(ch);
				return;
			}
			ch2 = vec.back();
			t.a = ch;
			t.b = ch2;
			if((it = com.find(t))!= com.end())
			{
				ch3=it->second;
				vec.pop_back();
				check(ch3);
				return;
			}
			t.a = ch2;
			t.b = ch;
			if((it = com.find(t))!= com.end())
			{
				ch3=it->second;
				vec.pop_back();
				check(ch3);
				return;
			}
			rep(i, vec.size())
			{
				ch2 = vec[i];
				t.a = ch;
				t.b = ch2;
				if((it = cle.find(t))!= cle.end())
				{
					vec.clear();
					return;
				}
			}
			rep(i, vec.size())
			{
				ch2 = vec[i];
				t.a = ch2;
				t.b = ch;
				if((it = cle.find(t))!= cle.end())
				{
					vec.clear();
					return;
				}
			}
			vec.push_back(ch);
}


void main()
{
	fin.open("B-large.in",ios::in);
	fout.open("a.out",ios::out);
	int cases,con,i,j,k,sum;

	char ch,ch2,ch3;
	int c;
	int r;
	int n;

	fin>>cases;
	rep(con,cases)
	{
		cout<<"Now in test case "<<con+1<<endl;
		c=0;r=0;n=0;
		com.clear();
		cle.clear();
		vec.clear();

		fin >> c;
		rep(i,c)
		{
			fin>>ch;
			t.a = ch;
			fin>>ch;
			t.b=ch;
			fin>>ch;
			com.insert(pair<twochar, char>(t, ch));
		}
		fin >> r;
		rep(i,r)
		{
			fin>>ch;
			t.a = ch;
			fin>>ch;
			t.b=ch;
			cle.insert(pair<twochar, char>(t, ch));
		}

		fin>>n;
		rep(i,n)
		{
			fin>>ch;
			check(ch);
		}
		fout<<"Case #"<<con+1<<": [";
		int size;
		size = vec.size();
		if(size !=0)
		{
		rep(i, (size -1))
			fout<<vec[i]<<", ";
		fout<<vec[size -1];
		}
		fout<<"]"<<endl;

	}
	char theFix;
	cin>>theFix;
	return;
}
