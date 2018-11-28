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
//#define NDEBUG
#include <assert.h>
using namespace std;
#ifndef NDEBUG
    #define debug(x) cerr<<#x<<"=\""<<x<<"\""<<" at line#"<<__LINE__<<endl;
    #define hline() cerr<<"-----------------------------------------"<<endl;
#else
    #define debug(x)
    #define hline()
#endif
typedef long long int llint;
#define low(x) ((((x)^((x)-1))&x))
#define two(x)  ((1)<<(x))
#define PB(x) push_back((x))
#define SORT(x) sort(x.begin(),x.end())
const int dir[][2]={{-1,0},{0,-1},{0,1},{1,0},{1,1},{1,-1},{-1,1},{-1,-1}};
const char dname[]="NWSE";
typedef vector<vector<int> > vector2D;
int get_root(int a,vector<int>& root)
{
	stack<int> st;
	while(root[a]!=-1)st.push(a),a=root[a];
	while(st.size())root[st.top()]=a,st.pop();
	return a;
}


int main()
{
	int ca=1,T;
	for(cin>>T;T--;ca++)
	{
		int H,W;
		cin>>H>>W;
		vector2D height(H,vector<int>(W));
		vector<int> root(H*W,-1);
		for(int i=0;i<H;i++)
		for(int j=0;j<W;j++)
			cin>>height[i][j];

		for(int i=0;i<H;i++)
		for(int j=0;j<W;j++)
		{
			int lowest=10000000,ind=-1;
			for(int d=0;d<4;d++)
			{
				int r=i+dir[d][0];
				int c=j+dir[d][1];
				if(r<0||r>=H||c<0||c>=W)continue;
				if(lowest>height[r][c])lowest=height[r][c],ind=d;
			}
			if(ind==-1||lowest>=height[i][j])continue;
			int a=get_root(i*W+j,root);
			int b=get_root((i+dir[ind][0])*W+j+dir[ind][1],root);
			root[a]=b;
			//cerr<<a<<"-->"<<b<<endl;
		}
		cout<<"Case #"<<ca<<":"<<endl;
		map<int,int> flag;
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				int a=get_root(i*W+j,root);
				if(flag.count(a)==0)flag[a]=flag.size()-1;
				char ff=flag[a]+'a';
				cout<<(j?" ":"")<<ff;
			}
			cout<<endl;
		}
	}
	return 0;
}
