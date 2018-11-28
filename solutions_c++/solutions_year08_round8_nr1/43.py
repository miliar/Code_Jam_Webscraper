#include <string> 
#include <vector> 
#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <stdio.h> 
#include <math.h> 
#include <stdlib.h> 
using namespace std; 

#ifdef __GNUC__ 
typedef long long lint;typedef unsigned long long ulint; 
#else 
typedef __int64 lint;typedef unsigned __int64 ulint; 
#endif 

#define VI vector<int> 
#define VVI vector<VI> 
#define VD vector<double> 
#define VVD vector<VD> 
#define VS vector<string> 
#define VVS vector<VS> 
#define pb push_back 
#define sz size() 
#define mp make_pair

#define FOR(i,m) for(int i=0;i<m;i++) 
#define FORA(i,v) for(int i = 0; i < (v).size(); i++) 
#define all(v) (v).begin(), (v).end() 

inline string i2s(int val) {char buf[256];sprintf(buf,"%d",val);return buf;} 
inline string d2s(double val) {char buf[256];sprintf(buf,"%.2f",val);return buf;} 
inline int s2i(string s) {int val;sscanf(s.c_str(),"%d",&val);return val;} 
inline double s2d(string s) {double val;sscanf(s.c_str(),"%lf",&val);return val;} 
VS s2vs( string s, string c = " ", bool empty_string = false) 
{ 
  VS res; 
  string t = ""; 
  FORA(i, s) if ( c.find(s[i]) != -1 ) {if (t!=""||empty_string) res.pb( t );t = "";} else t += s[i];   
  if (t!=""||empty_string) res.pb( t ); 
  return res; 
} 
VI vs2vi(VS vs) {VI res;FOR(i,vs.sz) res.pb(atoi(vs[i].c_str()));return res;} 
inline VI s2vi(string s, string t=" ") {return vs2vi(s2vs(s,t));} 
inline vector <vector<string> > vs2vvs(vector <string> vs, string t=" ") {vector <vector<string> > res;for (int i=0;i<vs.size();i++) res.push_back(s2vs(vs[i],t));return res;} 
inline vector <vector<int> > vs2vvi(VS vs, string t=" ") {vector <vector<int> > res;FOR(i,vs.sz) res.pb(s2vi(vs[i],t));return res;} 

int main()
{
	int T1;
	scanf("%d",&T1);
	for(int qq=0;qq<T1;++qq)
	{
		int Ax,Ay,Bx,By,Cx,Cy;
		int Ax1,Ay1,Bx1,By1,Cx1,Cy1;

		scanf("%d %d %d %d %d %d",&Ax,&Ay,&Bx,&By,&Cx,&Cy);
		scanf("%d %d %d %d %d %d",&Ax1,&Ay1,&Bx1,&By1,&Cx1,&Cy1);

		if (Ax==Ax1 && Ay==Ay1 && Bx==Bx1 && By==By1 && Cx==Cx1 && Cy==Cy1)
		{
		printf("Case #%d: %.6lf %.6lf\n",qq+1,double(Ax),double(Ay));
		continue;
		}

		int a1=Ax-Ax1,b1=Bx-Bx1,c1=Cx-Cx1;
		int a2=Ay-Ay1,b2=By-By1,c2=Cy-Cy1;

		int delta=a1*(b2-c2)-b1*(a2-c2)+c1*(a2-b2);
		if (delta==0)
		{
		printf("Case #%d: No Solution\n",qq+1);
		continue;
		}

		int d1=-b1*(-c2)+c1*(-b2);
		int d2=a1*(-c2)+c1*(a2);
		int d3=a1*(b2)-b1*(a2);

		double alfa=double(d1)/double(delta);
		double betta=double(d2)/double(delta);
		double gamma=double(d3)/double(delta);

		double X=alfa*Ax+betta*Bx+gamma*Cx;
		double Y=alfa*Ay+betta*By+gamma*Cy;

		printf("Case #%d: %lf %lf\n",qq+1,X,Y);
	}

	return 0;
}