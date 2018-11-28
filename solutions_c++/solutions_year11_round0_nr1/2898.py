#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define read(x) freopen(x,"r",stdin);
#define rite(x) freopen(x,"w",stdout);

#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)

#define on(bit,pos) (bit)|1<<(pos-1)
#define off(bit,pos) (bit)& ~(1<<(pos-1))
#define check(bit,pos) ((bit)==((bit)|1<<(pos-1)))

using namespace std;

typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef map<int,st> mis;
typedef set<int> si;
typedef set<st> ss;

template<class T> inline T gcd(T a,T b) {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b) {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline T sqr(T x){return x*x;}
template<class T> inline T power(T x,T p){if(!p) return 1;return x*power(x,p-1);}

const int mx=0;

struct node 
{
	int RED,BLUE;
	int point;
};
struct data
{
	string clr;
	int B;
};

#define NOTVIS vis[temp.RED][temp.BLUE][temp.point]==false
#define vip { vis[temp.RED][temp.BLUE][temp.point]=true; w.push(temp);  if(temp.point==Q+1){found=1;break;} }
#define VALID temp.RED>=1 && temp.RED<=100 && temp.BLUE>=1 && temp.BLUE<=100

int main()
{
	read("in"); rite("out");
	int T,kas=0;
	cin>>T;
	while(T--)
	{
		vector<data>VW;
		int Q;
		cin>>Q;
		data dtemp;
		VW.push_back(dtemp);
		for(int i=1;i<=Q;i++)
		{
			string S;
			int val;
			
			cin>>S>>val;
			dtemp.clr=S; dtemp.B=val;
			VW.push_back(dtemp);
		}
		
		queue<node>q,w;
		node temp;
		bool vis[101][101][101];
		memset(vis,0,sizeof(vis));
		temp.RED=1; temp.BLUE=1; temp.point=1;	
		vis[1][1][1]=true;
		q.push(temp);
		int found=0;
		int cnt=0;
		 while(1)
		 {
			while(!q.empty())
			{
				node top=q.front(); q.pop();
				
				temp.RED=top.RED; temp.BLUE=top.BLUE; temp.point=top.point;
				if(VW[temp.point].clr=="O" and VW[temp.point].B==temp.RED)
				{
					temp.point++;
					if(NOTVIS)vip;
				}
						
				temp.RED=top.RED; temp.BLUE=top.BLUE; temp.point=top.point;
				if(VW[temp.point].clr=="B" and VW[temp.point].B==temp.BLUE)
				{
					temp.point++;
					if(NOTVIS)vip;
				}
				  
				temp.RED=top.RED; temp.BLUE=top.BLUE+1; temp.point=top.point;
				if(VALID)
				{
					if(VW[temp.point].clr=="O" and VW[temp.point].B==temp.RED) temp.point++;
					if(NOTVIS)vip;
				}
				
				temp.RED=top.RED; temp.BLUE=top.BLUE-1; temp.point=top.point;
				if(VALID)
				{
					if(VW[temp.point].clr=="O" and VW[temp.point].B==temp.RED) temp.point++;
					if(NOTVIS)vip;
				}
				
				temp.RED=top.RED+1; temp.BLUE=top.BLUE; temp.point=top.point;
				if(VALID)
				{
					if(VW[temp.point].clr=="B" and VW[temp.point].B==temp.BLUE) temp.point++;
					if(NOTVIS)vip;
				}
				
				temp.RED=top.RED-1; temp.BLUE=top.BLUE; temp.point=top.point;
				if(VALID)
				{
					if(VW[temp.point].clr=="B" and VW[temp.point].B==temp.BLUE) temp.point++;
					if(NOTVIS)vip;
				}
							
				temp.RED=top.RED-1; temp.BLUE=top.BLUE+1; temp.point=top.point;
				if(VALID)   {if(NOTVIS){	vip;;}}
				
				temp.RED=top.RED+1; temp.BLUE=top.BLUE+1; temp.point=top.point;
				if(VALID)   {if(NOTVIS){	vip;}}
				
				temp.RED=top.RED+1; temp.BLUE=top.BLUE-1; temp.point=top.point;
				if(VALID)   {if(NOTVIS){	vip;}}
				
				temp.RED=top.RED-1; temp.BLUE=top.BLUE-1; temp.point=top.point;
				if(VALID)   {if(NOTVIS){	vip;}}
			
			}
			cnt++;
			if(found) break;
			if(w.empty()) break;
			while(!w.empty())
			{
				q.push(w.front());
				w.pop();
			}
			
		}
		if(found) printf("Case #%d: %d\n",++kas,cnt);
	}	
	return 0;
}
