#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<string>
#include<set>
#include<map>
using namespace std;
#define vi vector<int>
#define vvi vector<vi>
#define vp vector< pair<int,int> >
#define vvp vector< vp >
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef long long lli;
int __sign;
int __ch;
inline void S( int &x )
{
			x=0;
			while((__ch<'0' || __ch>'9') && __ch!='-' && __ch!=EOF)	__ch=getchar_unlocked();
			if (__ch=='-')
				__sign=-1 , __ch=getchar_unlocked();
			else
				__sign=1;
			
			do
				x=(x<<3)+(x<<1)+__ch-'0';
			while((__ch=getchar_unlocked())>='0' && __ch<='9');
			x*=__sign;
}
int main()
{
	int t, n, pos, i, cnt=1;
	char bot[3], pbot;
	int rpos[2], ans, moves, b;
	S(t);
	while(t--)
	{
		rpos[0]=rpos[1]=1;
		ans=moves=0;
		S(n);
		scanf("%s%d",bot,&pos);
		pbot=bot[0];
		ans+=pos;
		moves=pos;
		rpos[pbot=='O']=pos;
		for(i=1;i<n;i++)
		{
			scanf("%s%d",bot,&pos);
			b=(bot[0]=='O');
			if(pbot==bot[0])
			{
			ans+=abs(rpos[b]-pos)+1;
			moves+=abs(rpos[b]-pos)+1;
			}
			else
			{
				if(moves>abs(pos-rpos[b]))
				moves=1;
				else
				moves=abs(pos-rpos[b])+1-moves;
				ans+=moves;
				pbot=bot[0];
			}
			rpos[b]=pos;
		//	printf("--> %c %d\n",bot[0],moves);
		}
		printf("Case #%d: %d\n",cnt++,ans);
	}
	return 0;
}
