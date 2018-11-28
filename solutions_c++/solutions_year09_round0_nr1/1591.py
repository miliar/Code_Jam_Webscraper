#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <limits>
#include <map>
#include <cmath>
#include <numeric>
using namespace std;
 
#define pb push_back
#define REP(i,n) for(int i=0; i<(n); ++i)   
#define ALL(X) (X).begin(),(X).end()
#define present(c,x) ((c).find(x) != (c).end())
typedef long long ll;
template<class T>inline int sz(T& x){return (int)x.size();}
int stoi(string a){int len=sz(a);if(len==1)return a[0]-'0';return a[len-1]-'0'+10*stoi(a.substr(0,len-1));}
template<class T>inline string tostring(T& i){ostringstream oss; oss << i; return oss.str();}
template <class T> void make_unique(T& v){sort(ALL(v)); v.resize(unique(ALL(v)) - v.begin());}

int len;
int ans;
vector<string> p;
map<string,bool> d;
vector<string> d_h;
vector<string> h;

void go()
{
	for(int de=0;de<len;de++)
	{
		vector<string> t;
		for(int i=0;i<sz(p[de]);i++)
		{
			for(int j=0;j<sz(h);j++)
			{
				if(h[j][de] == p[de][i])
				{
					t.push_back(h[j]);
					h.erase(h.begin() + j);
					j--;
				}
			}
		}
		h = t;
		if(sz(h) == 0) break;
	}
	ans = sz(h);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>len;
	int dic; cin>>dic;
	int test; cin>>test;
	for(int i=0;i<dic;i++)
	{
		string str;
		cin>>str;
		d[str] = true;
		d_h.push_back(str);
	}
	for(int tt=1;tt<=test;tt++)
	{
		p.clear();
		ans = 0;
		string str; cin>>str;
		for(int i=0;i<sz(str);i++)
		{
			if(str[i] == '(')
			{
				string t;
				for(int j=i+1;j<sz(str);j++)
				{
					if(str[j] == ')')
					{
						i = j;
						break;
					}
					else
					{
						t += str[j];
					}
				}
				p.push_back(t);
			}
			else
			{
				p.push_back(tostring(str[i]));
			}
		}
		h.clear();
		for(int i=0;i<sz(d_h);i++)
			h.push_back(d_h[i]);
		go();
		cout << "Case #"<<tt<<": "<< ans << endl;
	}
	return 0;
} 