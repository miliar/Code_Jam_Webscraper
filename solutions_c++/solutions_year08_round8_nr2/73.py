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
	cin >> T1;
	for(int qq=0;qq<T1;++qq)
	{
		int N;
		cin >> N;

		VS C;
		VI A,B;
		FOR(i,N)
		{
			string c;
			int a,b;
			cin >> c >> a >> b;
			C.pb(c);
			A.pb(a);
			B.pb(b);
		}
/*
		FOR(i,N)
			FOR(j,N-1)
		{
			if (B[j]>B[j+1])
			{
				swap(C[j],C[j+1]);
				swap(A[j],A[j+1]);
				swap(B[j],B[j+1]);
			}
		}
*/
		/*
		int best=-1;
		int num=0;
		for(int i=1;i<=10000;++i)
		{
			FOR(j,N) if (A[j]<=i && i<=B[j]) {++num;break;}
		}
		if (num<10000)
		{
			cout << "Case #" << qq+1 << ": IMPOSSIBLE" << endl;
			continue;
		}
*/
		int best=-1;
		for(int i=1;i<(1<<N);++i)
		{
			int number=0;
			set<string> S;
			FOR(j,N)
			{
				if (i&(1<<j))
				{S.insert(C[j]);
				++number;
				}
			}
			if (S.size()>3) continue;

			int num=0;
			for(int j=1;j<=10000;++j)
			{
				FOR(k,N) if ((i&(1<<k)) && A[k]<=j && j<=B[k]) {++num;break;}
			}

			if (num==10000)
			{
				if (best==-1 || number<best)
					best=number;
			}
		}

		if (best==-1)
			cout << "Case #" << qq+1 << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << qq+1 << ": " << best << endl;
	}

	return 0;
}