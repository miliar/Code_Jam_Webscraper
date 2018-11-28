#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <cctype>
#include <algorithm>
#include <functional>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(i,n) for(i=0;i<(n);++i)

typedef vector<int> vi ;
typedef vector<string> vs ;
typedef vector<double> vd ;
#define sz(x) ((int)(x).size())
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
typedef long long ll;
int lst(string a)
{
	for(int i = sz(a)-1 ; i >= 0 ; i-- )
		if(a[i]=='1')return i;
	return 0;
}


int calc(vector<int> st)
{
	int res = 0;
	for(int i = 0,j ; i < sz(st) ; i++)
	{
		for(j = i ; j < sz(st) && st[j]>i; j++);
		res+=j-i;
		for(int k = j ; k > i ; k--)
			swap(st[k],st[k-1]);
	}
	return res;
}

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

	int t;
	cin>>t;
	int n;
	string tmp;
	for(int i = 0 ; i < t; i ++)
	{
		cin>>n;
		vector<int> v(n);
		for(int j= 0 ; j < n ; j++)
		{
			cin>>tmp;
			v[j]=lst(tmp);
		}
		printf("Case #%d: %d\n",i+1,calc(v));
	}


	return 0;
}
