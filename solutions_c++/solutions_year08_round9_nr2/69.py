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
#include <queue>
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
			re.push(tmp);
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
template<class T>
T extendGcd(T a,T b,T& x,T& y)
{
	T r,g;
	if(b==0)
	{
		x=1;y=0;
		return a;
	}
	r=a%b;
	g=extendGcd(b,r,x,y);
	r=x;x=y;y=r-a/b*y;
	return g;
}
void update(llint a,llint b,llint& low,llint &high)
{
	if(a==0&&b>0)low=high+1;
	if(a==0)return ;
	if(a>0)
	{
		if(b>=0)low=max(low,(b+a-1)/a);
		else low=max(low,b/a);
	}
	else
	{
		a=-a;b=-b;
		if(b>=0)high=min(high,b/a);
		else high=min(high,(b-a+1)/a);
	}
}
bool visited[100][100];
int BFS(int x,int y,int a1,int b1,int a2,int b2,int n,int m)
{
	queue<int> qq;
	memset(visited,false,sizeof(visited));
	qq.push((x<<8)^y);
	visited[x][y]=true;
	int re=0;
	while(qq.size())
	{
		int x=qq.front()>>8;
		int y=qq.front()&0xff;
		qq.pop();
		re++;
		int xx=x+a1,yy=y+b1;
		if(xx>=0&&xx<n&&yy>=0&&yy<m&&!visited[xx][yy])qq.push((xx<<8)^yy),visited[xx][yy]=true;
		xx=x+a2,yy=y+b2;
		if(xx>=0&&xx<n&&yy>=0&&yy<m&&!visited[xx][yy])qq.push((xx<<8)^yy),visited[xx][yy]=true;
	}
	return re;
}
int main()
{
	int t,ca=1;
	for(cin>>t;t--;)
	{
		llint a1,b1,a2,b2,n,m;
		cin>>n>>m>>a1>>b1>>a2>>b2;
		llint xx,yy;
		cin>>xx>>yy;
		cout<<"Case #"<<ca++<<": "<<BFS(xx,yy,a1,b1,a2,b2,n,m)<<endl;
		continue;
		llint k1,k2;
		llint x1=-xx,x2=n-1-xx;
		llint y1=-yy,y2=m-1-yy;
		llint ga=extendGcd(abs(a1),abs(a2),k1,k2);
//		Debug(ga);
		if(a1<0)k1=-k1;
		if(a2<0)k2=-k2;
		assert(k1*a1+k2*a2==ga);
		assert(ga);
		llint ans=0;
		for(llint dx=x1;dx<=x2;dx++)
		{
			if(dx%ga)continue;
			llint kk1=k1*(dx/ga);
			llint kk2=k2*(dx/ga);
//			cout<<"kk1="<<kk1<<" kk2="<<kk2<<endl;
//			Debug(dx);
			assert(a1*kk1+a2*kk2==dx);
			llint dy1=y1-kk1*b1-kk2*b2;
			llint dy2=y2-kk1*b1-kk2*b2;
//			cout<<dy1<<" to "<<dy2<<endl;
			llint cof=b1*(a2/ga)-b2*(a1/ga);
//			Debug(cof);
			llint low=-1000000000000000LL,high=100000000000000LL;
			update(a2/ga,-kk1,low,high);
		//	cout<<low<<" to "<<high<<endl;
			update(a1/ga,-kk2,low,high);
		//	cout<<low<<" to "<<high<<endl;
			update(cof,dy1,low,high);
		//	cout<<low<<" to "<<high<<endl;
			update(-cof,-dy2,low,high);
		//	cout<<low<<" to "<<high<<endl;
//			if(low>high)continue;
			cout<<low<<"  ------  "<<high<<endl;
			for(llint k=low;k<=high;k++)
			{
				llint k1=kk1+(a2/ga)*k;
				llint k2=kk2-(a1/ga)*k;
				assert(k1*a1+k2*a2==dx);
				assert(k1*b1+k2*b2<=y2);
				assert(k1*b1+k2*b2>=y1);

			}
			//if(low<=high)ans+=(high+1-low);
			//assert(high+1-low<=m);
		//	cout<<ans<<endl;
		}
//		assert(ans<=n*m);
	}
	return 0;
}
