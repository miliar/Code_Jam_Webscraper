#include<cstdio>
#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<algorithm>
#include<numeric>
#include<cstdlib>
#include<cmath>
#include<set>
#include<map>
#include<ctime>
#include<utility>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz size()
#define all(qq) qq.begin(),qq.end()
#define rall(qq) qq.rbegin(),qq.rend()
#define clr(qq) memset((qq),0,sizeof(qq))
#define fill(qq) memset((qq),0x3F,sizeof(qq))
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define repd(i,n) for(int i=(int)(n-1);i>=0;i--)
#define rep2(i,a,b) for(int (i)=(int)(a);i<(int)(b);i++)
#define fore(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
#define rint(qq) int(floor(qq+0.5))
#define sqr(qq) ((qq) * (qq))
#define ll long long
#define inf 999999999
#define fi first
#define se second
#define PI 3.14159265358979

int n;
double f,R,t,r,g,cele,volne;

double go1(double x,double y0,double y1,double polomer)
{
	return 0.5*sqr(polomer)*(atan(y1/x)-atan(y0/x));
}

double go2(double x,double y0,double y1)
{
	return 0.5*x*(y1-y0);
}

double cast(double x,double y0,double y1,double polomer)
{
	if (abs(x)<1e-9) return 0;
	if (abs(x)>=polomer) return go1(x,y0,y1,polomer); 
	double pom=sqrt(sqr(polomer)-sqr(x));
	if (y0<=-pom)
	{
		if (y1<=-pom) return go1(x,y0,y1,polomer);
		if (y1<=pom) return go1(x,y0,-pom,polomer)+go2(x,-pom,y1);
		return go1(x,y0,-pom,polomer)+go2(x,-pom,pom)+go1(x,pom,y1,polomer);
	}
	else if (y0<pom)
	{
		if (y1<-pom) return go2(x,y0,-pom)+go1(x,-pom,y1,polomer);
		if (y1<=pom) return go2(x,y0,y1);
		return go2(x,y0,pom)+go1(x,pom,y1,polomer);
	}
	if (y1<-pom) return go1(x,y0,pom,polomer)+go2(x,pom,-pom)+go1(x,-pom,y1,polomer);
	if (y1<pom) return go1(x,y0,pom,polomer)+go2(x,pom,y1);
	return go1(x,y0,y1,polomer);
}

double prienik(double vlavo,double vpravo,double dole,double hore,double polomer)
{
	if (vlavo>=vpravo||dole>=hore) return 0;
	if (sqr(dole)+sqr(vlavo)>=sqr(polomer)) return 0;
	if (sqr(hore)+sqr(vpravo)<=sqr(polomer)) return (hore-dole)*(vpravo-vlavo);
	return cast(vpravo,dole,hore,polomer)+cast(hore,-vpravo,-vlavo,polomer)+cast(-vlavo,-hore,-dole,polomer)+cast(-dole,vlavo,vpravo,polomer);
}	

int main ()
{
	cin>>n;
	rep(i,n)
	{
		cin>>f>>R>>t>>r>>g;
		cele=PI*sqr(R);
		volne=0;
		for(double x=r;x<R-t;x+=g+r+r)
		{
			for(double y=r;y<R-t;y+=g+r+r)
			{
				double diera=prienik(x+f,x+g-f,y+f,y+g-f,max(0.,R-t-f));
				//cout<<"diera = "<<diera<<endl;
				if (diera<1e-9) break;
				volne+=diera;
			}
		}
		volne*=4;
		cout<<"Case #"<<i+1<<": ";
		printf("%.6lf\n",1.-volne/cele);
	}
	return 0;
}
