/*
ID: imranka1
PROG: test
LANG: C++
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

#include <fstream>
using namespace std;
#define all(x) (x).begin(),(x).end()

#define vs vector <string>
#define vi vector <int>
#define vvi vector < vi >
#define p(X) push_back((X))

#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define fire(i,j,n) for(int (i)=(j);(i)<=(n);(i)++)
#define firr(i,j,n) for(int (i)=(j);(i)>(n);(i)--)
#define firre(i,j,n) for(int (i)=(j);(i)>=(n);(i)--)
#define tr(v,it) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)

#define srt(v) sort((v).begin(),(v).end())
#define srtc(v) sort(v.begin(),v.end(),cmp)

#define _bc(i) __builtin_popcount(i)
#define INF 0x3f3f3f3f
#define ipow(a,b) (int)pow((double)a,(double)b)
#define fill(a,b) memset(a,b,sizeof(a))
#define maxr(num,a,b) max_element(num.begin()+a,num.begin()+b);
#define minr(num,a,b) min_element(num.begin()+a,num.begin()++b)
#define maxi(v) max_element(all(v))
#define mini(v) min_element(all(v))


string lower(string s) {for(int i=0;i<s.size();i++) s[i]=tolower(s[i]);return s;}
vector<string> sep(string s,char c) { string temp;vector<string> res;for(int i=0;i<s.size();i++) { if (s[i]==c) {if (temp!="") res.push_back(temp);temp="";continue;}temp=temp+s[i];}if (temp!="") res.push_back(temp);return res;}
int toint(string s) { stringstream s1(s);int n;s1>>n;return n;}
string tostr(int n) {stringstream s;s<<n;return s.str();}
string trim(string s)
{
	int p=0;
	while(s[p]==' ')
	{
	p++;
	}
	s.erase(0,p);
	p=s.size()-1;
	while(s[p]==' ')
	{
		p--;
	}
	s.erase(p+1,s.size()-p-1);
	return s;
}
template<class T> void D(T A[],int n) {for(int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
template<class T> void D(vector<T> A,int n=-1) {if (n==-1) n=A.size();for(int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
//#define cin fin
//#define cout fout
int get(int x0,int y0,int x1,int y1,int x2,int y2)
{
	return abs((x1-x0)*(y2-y0)-(x2-x0)*(y1-y0));
}
#define cout fout
int main() {
	ofstream fout("test.out");
    int tc;
	cin>>tc;int cas=0;
	while(tc--)
	{
		cas++;
		int n,m,a;
		cin>>n>>m>>a;
		int x0,y0,x1,y1,x2,y2;
		x0=0;
		y1=0;
		bool fnd=0;
		fire(iy,0,m)
		{
			fire(ix,0,n)
			{
				fire(j,0,n)
				fire(k,0,m)
				{
					if (fnd) break;
					y0=iy;
					x1=ix;
					x2=j;
					y2=k;
					int ar=get(x0,y0,x1,y1,x2,y2);
					if (ar==a)
					{fnd=1;break;}
					//if (x0==0&&y0==0&&x1==0&&y1==1&&x2==1&&y2==1)
					//cout<<fnd<<endl;
				}
				if (fnd) break;
			}
			if (fnd) break;
		}
		cout<<"Case #"<<cas<<": ";
		if (!fnd)
		cout<<"IMPOSSIBLE"<<endl;
		else
		cout<<x0<<" "<<y0<<" "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<endl;
	}
    return 0;
}