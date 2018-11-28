#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <sstream>
#include <map>
#include <assert.h>
using namespace std;
typedef long long int llint;
#define EPS 1e-10
#define INF 1e10
#define LOW(x) ((((x)^((x)-1))&x))
#define Debug(x) cout<<#x<<"=\""<<x<<"\""<<endl;
#define Hline() do{cout<<"-------------------------------"<<endl;}while(0)
const int two[]={1,1<<1,1<<2,1<<3,1<<4,1<<5,1<<6,1<<7,1<<8,1<<9,1<<10,
1<<11,1<<12,1<<13,1<<14,1<<15,1<<16,1<<17,1<<18,1<<19,1<<20,
1<<21,1<<22,1<<23,1<<24,1<<25,1<<26,1<<27,1<<28,1<<29,1<<30};
const int dir[][2]={{-1,0},{0,1},{1,0},{0,-1}};
const char dname[]="NWSE";
//const char dname[]="URDL";
const double PI=acos(-1.0);
//*****************************************//
double Euclid_dis(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}
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
template<class T>
string convert(T vv)
{
	ostringstream re;
	re<<vv;
	return re.str();
}
template<class T>
vector<T> parse(const string& ss,const char* cut)
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
/*
Some common techniques, just try them one by one.
Binary search
Ternary search
Bitwise tricks
subset DP
Network flow
*/
const int N=5000;
int aa[N],bb[N],cc[N];
int main()
{
	int t,ca=1;
	for(cin>>t;t--;)
	{
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>aa[i]>>bb[i]>>cc[i];
		int ans=0;
		for(int a=0;a<n;a++)
		for(int b=0;b<n;b++)
		for(int c=0;c<n;c++)
		{
			if(aa[a]+bb[b]+cc[c]>10000)continue;
			int sum=0;
			for(int i=0;i<n;i++)
				if(aa[a]>=aa[i]&&bb[b]>=bb[i]&&cc[c]>=cc[i])
					sum++;
			ans=max(ans,sum);
		}
		cout<<"Case #"<<ca++<<": "<<ans<<endl;
	}
	return 0;
}
