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
#define cin fin
#define cout fout
int ar[14];
string _num;
long long cnt=0;
void backtrak(int k,int n)
{
	if (k==n)
	{
		long long res=0;
		long long th=_num[0]-'0';
		int pro=1;
		fir(i,0,n)
		{
			if (ar[i]==0)
			{
				th=(th*10)+_num[i+1]-'0';
			}
			else
			{
				switch(pro)
				{
					case 1:
					res+=th;
					break;
					case 2:
					res-=th;
					break;
				}
				pro=ar[i];
				th=_num[i+1]-'0';
			}
		}
		switch(pro)
				{
					case 1:
					res+=th;
					break;
					case 2:
					res-=th;
					break;
				}
		res=abs(res);
		if (res%2==0||res%3==0||res%5==0||res%7==0)
		{
			cnt++;
		}
		return;
	}
	ar[k]=0;
	backtrak(k+1,n);
	ar[k]=1;
	backtrak(k+1,n);
	ar[k]=2;
	backtrak(k+1,n);
}
int main() {
	ios_base::sync_with_stdio(false);
    ofstream fout ("test.out");
    ifstream fin ("test.in");
	int tc;
	cin>>tc;
	int cs=0;
	while(tc--)
	{
		cs++;
		cout<<"Case #"<<cs<<": ";
		string na;
		cin>>na;
		if (na.size()==1)
		{
			int th=toint(na);
			if (th%2==0||th%3==0||th%5==0||th%7==0)
			cout<<1<<endl;
			else
			cout<<0<<endl;
			continue;
		}
		cnt=0;
		_num=na;
		backtrak(0,na.size()-1);
		cout<<cnt<<endl;
	}
    return 0;
}
