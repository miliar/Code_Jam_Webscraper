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
#define maxn  3000000;
int n,m;
pair<int,int> p;
struct node
{
	pair<int,int>p;
	int a,b;
	node(){}
	node(pair<int,int> pp,int aa,int bb){
		p=pp; a=aa; b=bb;
	}
};
set<node >st,sv;
set<node >::iterator it;
bool operator <(const node &a,const node &b)
{
	a.a<b.a;
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in","r",stdin);
 	freopen("out","w",stdout);
#endif
int i,j,cas=0;
	int t;
	scanf("%d", &t);
	
	while(t--)
	{
		printf("Case #%d: ",++cas);
		p=make_pair(0,0);
		st.clear();	sv.clear();
		st.insert(node(p,0,0));
		scanf("%d", &n);
		for(i=0; i<n; i++)
		{
			scanf("%d", &m);
			for(it=st.begin(); it!=st.end(); it++)
			{
				p=it->p;
	sv.insert(node(make_pair(p.first^m,p.second),it->a+m,it->b));
	sv.insert(node(make_pair(p.first,p.second^m),it->a,it->b+m));
/*	
printf("!%d %d %d %d %d\n",m,p.first,p.second,it->a,it->b);
printf("@%d %d %d %d %d\n",m,p.first^m,p.second,(it->a)+m,it->b);
printf("#%d %d %d %d %d\n",m,p.first,p.second^m,it->a,(it->b)+m);
	*/		}
			st=sv;
			sv.clear();
		}
		int ans=-1;
		for(it=st.begin(); it!=st.end(); it++)
		{
			p=it->p;
			if(p.first==p.second && it->a!=0 && it->b!=0)
			{
				ans=max(ans,it->a);
				ans=max(ans,it->b);
			}
		}
		if(ans==-1)
		{
			cout<<"NO"<<endl;
		}
		else cout<<ans<<endl;
	}
}
