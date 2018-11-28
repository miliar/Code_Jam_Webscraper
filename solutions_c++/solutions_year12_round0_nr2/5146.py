/*************************************************************************
Author: ziki
Created Time: 2012/4/14 23:39:58
File Name: B.cpp
Description: 
************************************************************************/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <string.h>


using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double pi=acos(-1.0);
const double eps=1e-11;
const int inf=0x7FFFFFFF;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define zero(a) memset(a, 0, sizeof(a))
#define out(x) (cout<<#x<<": "<<x<<endl)
template<class T>void show(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a, int r, int l){for(int i=0; i<r; ++i)show(a[i],l);cout<<endl;}

int a[11111];
int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("B.out","w",stdout);
	int n,s,tt;
	int T;
	cin>>T;
	for(int cas = 1; cas<=T; cas++)
	{
		cin>>n>>s>>tt;
		for(int i=0; i<n; i++)
			cin>>a[i];
		int ans = 0;
		for(int i=0; i<n; i++)
		{
			if(tt == 0 && a[i]>=0) ans++;
			else if(tt == 1 && a[i]>0)ans++;
			else if(a[i] > (tt-1)*3) ans++;
			else if(tt>=2 && a[i] > (tt-2)*3 + 1 && s>0){
				s--;
				ans++;
			}
		}
		printf("Case #%d: ",cas);
		cout<<ans<<endl;
		//cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}

