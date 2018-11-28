#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <cfloat>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
#define pb push_back
#define L(s) (int)(s).size()
#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define fr(i,st,fn) for(int (i)=(st);(i)<=(fn);++(i))
#define VI vector<int>
#define inf 1000000000
#define ll long long
#define C(a) memset((a),0,sizeof((a)))
#define all(s) (s).begin(),s.end()
#define pi 3.1415926535897932384626433832795
#define pii pair<int,int>
#define mp make_pair
//#define x first
//#define y second
int n,m,k;
string name[111*111*2];
vector<int> child[111*111*2];
vector<string> split(string t)
{
	for(int i=0;i<L(t);++i)
		if (t[i]=='/')
			t[i]=' ';
	istringstream iss(t);
	vector<string> rez;
	rez.clear();
	string add;
	while(iss>>add)
		rez.pb(add);
	return rez;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int testcount;
	scanf("%d",&testcount);
	for(int testnum=1;testnum<=testcount;++testnum)
	{
		cerr<<testnum<<endl;
		scanf("%d%d",&n,&m);
		k=1;
		name[0]='!';
		child[0].clear();
		for(int i=0;i<n;++i)
		{
			string s;
			cin>>s;
			vector<string> sp=split(s);
			int cur=0;
			int pos=0;
			for(pos=0;pos<L(sp);)
			{
				string now=sp[pos];
				for(int j=0;j<L(child[cur]);++j)
					if (name[child[cur][j]]==now)
					{
						cur=child[cur][j];
						++pos;
						goto p1;
					}
				break;
				p1:;
			}
			for(;pos<L(sp);++pos)
			{
				string now=sp[pos];
				child[cur].pb(k);
				name[k]=now;
				cur=k;
				child[k].clear();
				k++;
			}
		}
		int rez=0;
		for(int i=0;i<m;++i)
		{
			string s;
			cin>>s;
			vector<string> sp=split(s);
			int cur=0;
			int pos=0;
			for(pos=0;pos<L(sp);)
			{
				string now=sp[pos];
				for(int j=0;j<L(child[cur]);++j)
					if (name[child[cur][j]]==now)
					{
						cur=child[cur][j];
						++pos;
						goto p2;
					}
				break;
				p2:;
			}
			for(;pos<L(sp);++pos)
			{
				++rez;
				string now=sp[pos];
				child[cur].pb(k);
				name[k]=now;
				cur=k;
				child[k].clear();
				k++;
			}
		}
		printf("Case #%d: %d\n",testnum,rez);
	}
}