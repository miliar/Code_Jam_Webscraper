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

vector<__int64> m_x,m_y;
__int64 R[3][3];

bool Less(int i1, int j1, int i2, int j2)
{
	if (i1<i2) return true;
	if (i1>i2) return false;
	return j1<j2;
}

int main()
{
	int T;
	cin >> T;
	for(int qq=0;qq<T;++qq)
	{
		__int64 n,A,B,C,D,x0,y0,M;
		m_x.clear();
		m_y.clear();

		FOR(i,3) FOR(j,3) R[i][j]=0;

		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

		__int64 X=x0,Y=y0;
		m_x.pb(X);m_y.pb(Y);
		R[X%3][Y%3]++;
		for(int i=1;i<=n-1;++i)
		{
			X=(A*X+B)%M;
			Y=(C*Y+D)%M;
			m_x.pb(X);m_y.pb(Y);
			R[X%3][Y%3]++;
		}

		__int64 ret=0;
		FOR(i1,3) FOR(j1,3)
			FOR(i2,3) FOR(j2,3) if (Less(i2,j2,i1,j1)==false)
				FOR(i3,3) FOR(j3,3) if (Less(i3,j3,i2,j2)==false && Less(i3,j3,i1,j1)==false)
		{
			__int64 r1=i1+i2+i3;
			__int64 r2=j1+j2+j3;
			if ((r1%3) || (r2%3)) continue;

			__int64 t1=R[i1][j1];
			__int64 t2=R[i2][j2];
			__int64 t3=R[i3][j3];

			if (i2==i1 && j2==j1) --t2;
			if (i3==i1 && j3==j1) --t3;
			if (i3==i2 && j3==j2) --t3;

			__int64 tmp=0;
			if (t1>0 && t2>0 && t3>0) tmp=t1*t2*t3;

			if (i1==i2 && i1==i3 && j1==j2 && j1==j3)
			{
				tmp/=6;
			}
			else
			if ((i1==i2 || i1==i3 || i2==i3) && (j1==j2 || j1==j3 || j2==j3))
			{
				tmp/=2;
			}

			ret+=tmp;
		}

		cout << "Case #" << qq+1 << ": " << ret <<endl;
	}

	return 0;
}