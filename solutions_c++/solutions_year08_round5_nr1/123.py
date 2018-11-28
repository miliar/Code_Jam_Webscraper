#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <fstream>
using namespace std;
#define pb push_back
#define ppb pop_back
#define mp make_pair
//#define pi 2*acos(0.0)
#define mp make_pair
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define pii pair<int,int>
#define pdd pair<double,double>
#define sz(c) (int)((c).size())
#define inf 1000000000
#define all(c) (c).begin(), (c).end()
#define vi vector<int>
#define vpii vector< pii >
#define vpdd vector< pdd >
#define L(s) (int)((s).end()-(s).begin())
#define ll long long
#define C(a,b) memset((a),(b),sizeof((a)))
int cnt,cc;
string s;
int n,i,j,m,cx,cy,w,k,lx,ly;
char ch;
int dx[4]={0,-1,0,1};
int dy[4]={1,0,-1,0};
bool a[6001][6001];
inline void move(char ch)
{
	if (ch=='F')
	{
		cx+=dx[w];
		cy+=dy[w];
	}
	else
		if (ch=='R')
			w=(w+3)%4;
		else
			w=(w+1)%4;
}
class T1
{
public:
	int x,y;
};
vector<T1> v;
class T2
{
public:
	int x,y;
};
vector<T2> h;
T1 e1;
T2 e2;
inline bool operator<(const T1&a,const T1&b)
{
	if (a.y<b.y)
		return true;
	else
		if (a.y>b.y)
			return false;
		else
			return (a.x<b.x);
}
inline bool operator<(const T2&a,const T2&b)
{
	if (a.x<b.x)
		return true;
	else
		if (a.x>b.x)
			return false;
		else
			return (a.y<b.y);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cnt;
	for(cc=1;cc<=cnt;cc++)
	{
		cout<<"Case #"<<cc<<": ";
		C(a,false);
		cin>>n;
		v.clear();
		h.clear();
		cx=0;
		cy=0;
		lx=0;
		ly=0;
		w=0;
		int ii;
		for(ii=0;ii<n;ii++)
		{
			s="";
			cin>>ch;
			while(!(ch==' '))
			{
				s+=ch;
				scanf("%c",&ch);
			}
			cin>>m;
			for(i=0;i<m;i++)
				for(k=0;k<L(s);k++)
				{
					move(s[k]);
					if (cx!=lx||cy!=ly)
					{
						if (cy!=ly)
						{
							e1.y=min(cy,ly);
							e1.x=cx;
							v.pb(e1);
						}
						else
						{
							e2.x=min(cx,lx);
							e2.y=cy;
							h.pb(e2);
						}
						lx=cx;
						ly=cy;
					}
				}

		}
		sort(all(v));
		sort(all(h));
		int cn=0;
		for(i=1;i<L(v)-1;i+=2)
			if (v[i].y==v[i+1].y)
			for(j=v[i].x;j<v[i+1].x;j++)
				a[j+3000][v[i].y+3000]=true;
		for(i=1;i<L(h)-1;i+=2)
			if (h[i].x==h[i+1].x)
			for(j=h[i].y;j<h[i+1].y;j++)
				a[h[i].x+3000][j+3000]=true;
		for(i=0;i<L(v)-2;i+=2)
			if (v[i].y==v[i+1].y)
			for(j=v[i].x;j<v[i+1].x;j++)
				a[j+3000][v[i].y+3000]=false;
		for(i=0;i<L(h)-2;i+=2)
			if (h[i].x==h[i+1].x)
			for(j=h[i].y;j<h[i+1].y;j++)
				a[h[i].x+3000][j+3000]=false;
		int rez=0;
		for(i=-3000;i<=3000;i++)
			for(j=-3000;j<=3000;j++)
				if (a[i+3000][j+3000])
					rez++;
		cout<<rez<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}