/* Asyamov Igor
e-mail: igor9669@gmail.com*/

#include <iostream>
#include <deque>
#include <string>
#include <vector>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <cstdio>
#include <map>
#include <fstream>
#include <cstdlib>
#include <queue>
#include <bitset>
#include <set>
#include <stack>
#include <utility>
#include<cassert>
using namespace std;
#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define MP make_pair
#define PB push_back
#define A first
#define B second
#define Len(a) (int)a.length()
#define Sz(a) (int)a.size()
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI > VVI;
#define MAXN 1000
const double Eps=1e-7;
const double Pi=2*acos(0.0);
const int inf=1000*1000*1000;
int g[MAXN+1];
VVI a;
int main()
{
	//freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	freopen("input.in","r",stdin);freopen("output.out","w",stdout);
	int n,k,R;
	int t;
	scanf("%d",&t);
	
	FOR(c,t)
	{
		scanf("%d%d%d",&R,&k,&n);
		FOR(i,n)scanf("%d",&g[i]);
		LL ans=0;
		a.clear();
		map<int,LL>coll;
		int pos=0;
		LL cur=0,sum=0;
		VI tmp;
		bool finished=false;
		int cnt=0,del=0;
		int last=0;
		while(!finished)
		{
			if(cur+g[pos]<=k && cnt+1<=n)
			{
				cur+=g[pos];
				tmp.PB(pos);
				pos++;
				pos%=n;
				cnt++;
			}
			else
			{
				FOR(i,Sz(a))
				{
					if(a[i]==tmp)
					{
						finished=true;
						last=0;
						FOR(j,i)
						{
							del++;
							ans+=coll[j];
							sum-=coll[j];
							coll.erase(coll.begin());
						}
						break;
					}
				}
				if(!finished)
				{
					coll[Sz(a)]=cur;
					a.PB(tmp);
					tmp.clear();
					sum+=cur;
					cur=0;	
				}
				cnt=0;
			}
		}
		int mod=Sz(coll);
		ans+=((R-del)/mod)*sum;
		map<int,LL>::iterator pp=coll.begin();
		FOR(i,(R-del)%mod)
		{
			ans+=pp->B;
			pp++;
			if(pp==coll.end())pp=coll.begin();
		}
		/*
		int pos=0,cur=0,cnt=0;
		LL sum=0;
		while(R--)
		{
			while(cur+g[pos]<=k && cnt+1<=n)
			{
				cur+=g[pos];
				pos++;
				pos%=n;
				cnt++;
			}
			sum+=cur;
			cur=0;
			cnt=0;
		}
		ans=sum;*/
		printf("Case #%d: %lld\n",c+1,ans);
	}
	/*printf("50\n");
	FOR(i,50)
	{
		R=rand()%100000001;
		k=rand()%1000000001;
		n=rand()%1001;
		printf("%d %d %d\n",R,k,n);
		FOR(i,n)
		{
			int r=rand()%10000001;
			while(r>k)r=rand()%10000001;
			printf("%d ",r);
		}
		printf("\n");
	}*/
	return 0;
}