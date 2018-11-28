#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#pragma comment(linker, "/STACK:16777216")
using namespace std;
#define pb push_back
#define ppb pop_back
#define pi 3.1415926535897932384626433832795028841971
#define mp make_pair
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pii pair<int,int>
#define pdd pair<double,double>
#define sz(x) int((x).size())
#define INF 1000000000
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define L(s) (int)((s).end()-(s).begin())
#define C(a) memset((a),0,sizeof(a))
#define val(ch) (int)(ch)-(int)('0')
#define toch(a) (char)((int)(a)+(int)('0'))
#define VI vector <int>
#define ll long long
int a,b,c,d,i,j,n,m,k,kolt,l;
char str[101];
string s;
pii sm[100001];
string cs[100001];
double w[100001];
void add(int l,int r,int cur)
{
	/*if (cur==1)
	{
		cerr<<"*";
		FOR(i,l,r) cerr<<s[i];
		cerr<<endl;
	}*/
	while (l<L(s) && s[l]==' ') l++;
	while (r>l && s[r]==' ') r--;
	l++;
	string ss="";
	while (l<r && s[l]!='(') ss+=s[l++];
	int l2=l+1;
	int c=1;
	while (l2<r) 
	{
		if (s[l2]=='(') c++; else if (s[l2]==')') c--;
		if (!c) break;
		l2++;
	}
	//cerr<<cur<<" "<<l<<" "<<r<<"  "<<ss<<endl;
	string s2;
	istringstream iss(ss);
	iss>>s2;
	if (l>=r) 
	{
		istringstream iss1(s2);
		double a;
		iss1>>a;
		w[cur]=a;
		return;
	}
	iss>>cs[cur];
	double a;
	istringstream iss1(s2);
	iss1>>a;
	w[cur]=a;
	r--;
	/*if (cur==1)
	{
		cerr<<l2<<" "<<r<<endl;
		FOR(i,l2,r) cerr<<s[i];
		cerr<<endl;
	}*/
	sm[cur].x=k++;
	sm[cur].y=k++;
	add(l,l2,sm[cur].x);
	add(l2+1,r,sm[cur].y);
}
set<string> rr;
double nx(int v,double cur)
{
	if (sm[v].x==-1 && sm[v].y==-1) return cur*w[v];
	if (rr.count(cs[v])) return nx(sm[v].x,cur*w[v]); else
	return nx(sm[v].y,cur*w[v]);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	gets(str);
	sscanf(str,"%d",&kolt);
	rep(hod,kolt)
	{
		gets(str);
		sscanf(str,"%d",&l);
		s="";
		rept(i,l)
		{
			gets(str);
			s+=" ";
			s+=str;
		}
		rept(i,100001) sm[i]=mp(-1,-1);
		a=0;
		k=1;
		//cerr<<s<<endl;
		add(0,L(s)-1,0);
		printf("Case #%d:\n",hod);
		gets(str);
		sscanf(str,"%d",&n);
		rept(i,n)
		{
			rr.clear();
			gets(str);
			istringstream iss(str);
			string s;
			iss>>s;
			iss>>s;
			while (iss>>s)
			{
				rr.insert(s);
			}
			double rz=nx(0,1.0);
			printf("%.7lf\n",rz);
		}
	}
}
