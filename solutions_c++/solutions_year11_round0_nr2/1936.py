#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<assert.h>
#include<cmath>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<stack>
using namespace std;
typedef long long ll;
const int inf=1000000000;
const double pi=acos(-1.0);
#define eps (1e-15)
#define L(x) ((x)<<1)
#define R(x) ((x)<<1|1)
#ifdef DBG
#define see(x) (cerr<<"[Line : "<< __LINE__<<"] : "<<#x<<"="<<x<<endl)
#define se(x) cerr<<x<<" "
#else
#define see(x) //
#define se(x) //
#endif

inline int to_i(const string& s){int n;sscanf(s.c_str(),"%d",&n);return n;}
inline string to_s(int n){char buf[32];sprintf(buf,"%d",n);return string(buf);}
#define maxn  300
int n,m,p;

map<string,string>mp;
int ch[maxn],flag[maxn];
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in","r",stdin);
	freopen("out","w",stdout);
#endif
    int i,j,k;
	int t,cas=0;
	scanf("%d", &t);
	while(t--)
	{
		string s,a,b;
		memset(ch,0,sizeof(ch));
		memset(flag,0,sizeof(flag));
		mp.clear();
		printf("Case #%d: ",++cas);
		scanf("%d", &n);
		for(i=0; i<n; i++)
		{
			cin>>s;
			a.clear(); b.clear();
			a+=s[0];a+=s[1];b+=s[2];
			mp[a]=b;
			reverse(a.begin(),a.end());
			mp[a]=b;
		}
		scanf("%d",&m);
		for(i=0; i<m; i++)
		{
			cin>>s;
			ch[s[0]]=s[1];
			ch[s[1]]=s[0];
		}
		cin>>p;
		cin>>s;
		a.clear(); b.clear();
		
		string now;
		for(i=0; i<s.size();i ++)
		{
			now=s[i];
			if(b.size()==0)
			{
				flag[now[0]]++;
				b+=s[i];
			}
			else
			{
				while(1)//b>=1
				{
					a.clear();a=b[b.size()-1]+now;
					b=b.substr(0,b.size()-1);
					if(mp.find(a)!=mp.end())
					{
						flag[a[0]]--;
						now=mp[a];
					}
					else 
					{
						b+=a[0];
						break;
					}
					if(b.size()==0)break;
				}
				if(flag[ch[now[0]]])	
				{
					b.clear();
					memset(flag,0,sizeof(flag));
				}
				else
				{
					b+=now;
					flag[now[0]]++;
				}
			}
		}
		printf("[");
		for(i=0; i<b.size(); i++)
		{
			if(i==0)	cout<<b[i];
			else cout<<", "<<b[i];
		}printf("]");
		cout<<endl;
	}
}
