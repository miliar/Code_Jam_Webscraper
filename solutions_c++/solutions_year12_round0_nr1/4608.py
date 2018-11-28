/*************************************************************************
Author: ziki
Created Time: 2012/4/14 23:19:44
File Name: A.cpp
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

char s[10000];
int main()
{
	freopen("out.txt","w",stdout);
	string a[3][2] = {
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"our language is impossible to understand",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"there are twenty six factorial possibilities",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv",
		"so it is okay if you want to just give up",
	};
	map<char, char> mp;
	for(int i=0; i<3; i++)
		for(int j=0; j<a[i][0].length(); j++)
			mp[ a[i][0][j] ] = a[i][1][j];
	mp['z'] = 'q';
	mp['q'] = 'z';
	//for(char i ='a'; i<='z'; i++)
	//	cout<<mp[i]<<endl;
	int T;
	scanf("%d",&T); getchar();
	for(int cas = 1; cas<=T; cas++)
	{
		gets(s);
		for(int i=0; s[i]; i++)
			s[i] = mp[s[i]];
		printf("Case #%d: ",cas);
		puts(s);
	}
	return 0;
}

