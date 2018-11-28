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

#define SZ 1000100
bool P[SZ];

lint GetParent(map<lint,lint> &M, lint t)
{
	lint ret=t;
	while(M[ret]!=ret) ret=M[ret];
	return ret;
}

void SetParent(map<lint,lint> &M, lint t, lint nt)
{
	lint ret=t;
	while(M[ret]!=ret) ret=M[ret];
	M[ret]=nt;
}

int main()
{
	memset(P,1,sizeof(P));
	P[0]=P[1]=false;
	for(int i=2;i<SZ;++i) if (P[i])
		for(int j=i+i;j<SZ;j+=i) P[j]=false;

	int T;
	cin >> T;
	for(int qq=0;qq<T;++qq)
	{
		map<lint,lint> M;

		lint a,b,i_p;
		cin >> a >> b >> i_p;

		for(lint i=a;i<=b;++i) M[i]=i;

		lint ret=b-a+1;

		for(lint i=i_p;i<SZ;++i) if (P[i])
		{
			lint t1=i*lint((a+i-1)/i);
			lint t2=i*lint(b/i);
			if (t1>=t2) continue;

			lint np = GetParent(M,t1);

			for(lint j=t1+i;j<=b;j+=i)		
			{
				lint cp = GetParent(M,j);
				if (cp!=np)
				{
					SetParent(M,j,np);
					--ret;
				}
			}

		}

		cout << "Case #" << qq+1 << ": " << ret << endl;
	}

	return 0;
}